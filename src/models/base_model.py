"""
Base class for ML models (train, predict, save, load)
Provides a common interface for progression, fatigue, or future models.
"""

from __future__ import annotations

from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any, Iterable, Optional, Sequence
from datetime import datetime

import joblib
import numpy as np
import pandas as pd


def _repo_root() -> Path:
	# src/models/base_model.py -> src -> repo root
	return Path(__file__).resolve().parents[2]


def _user_models_dir(username: str) -> Path:
	return _repo_root() / "users" / username / "models"


@dataclass
class ModelMetadata:
	model_name: str
	version: str = "0.1.0"
	created_at: str = datetime.utcnow().isoformat()
	feature_columns: Optional[Sequence[str]] = None
	target_column: Optional[str] = None
	random_state: Optional[int] = None
	extra: Optional[dict] = None


class BaseModel:
	"""
	Generic base wrapper around an estimator.

	- Provides fit/predict and regression evaluation helpers
	- Saves/loads per-user models under users/<username>/models/
	- Stores metadata (features, target, version, created_at)
	"""

	def __init__(
		self,
		estimator: Any,
		model_name: str,
		*,
		feature_columns: Optional[Sequence[str]] = None,
		target_column: Optional[str] = None,
		version: str = "0.1.0",
		random_state: Optional[int] = None,
		extra: Optional[dict] = None,
	) -> None:
		self.estimator = estimator
		self.metadata = ModelMetadata(
			model_name=model_name,
			version=version,
			feature_columns=tuple(feature_columns) if feature_columns else None,
			target_column=target_column,
			random_state=random_state,
			extra=extra or {},
		)
		self._fitted: bool = False

		# Apply random_state if estimator supports it
		if random_state is not None and hasattr(self.estimator, "random_state"):
			try:
				setattr(self.estimator, "random_state", random_state)
			except Exception:
				pass

	# -------------------------------
	# Data handling helpers
	# -------------------------------
	def _select_X(self, X: Any) -> Any:
		cols = self.metadata.feature_columns
		if isinstance(X, pd.DataFrame) and cols:
			missing = [c for c in cols if c not in X.columns]
			if missing:
				raise ValueError(f"Missing required feature columns: {missing}")
			return X.loc[:, list(cols)]
		return X

		# -------------------------------
		# Feature engineering hook
		# -------------------------------
		def build_features(self, df: pd.DataFrame) -> pd.DataFrame:
			"""Placeholder for feature engineering; override in subclasses.

			For now, returns a shallow copy unchanged. Downstream models can override to
			add rolling stats, lags, or domain-specific aggregates before fit/predict.
			"""
			return df.copy()

	# -------------------------------
	# Core API
	# -------------------------------
	def fit(self, X: Any, y: Optional[Iterable] = None, **fit_kwargs: Any) -> "BaseModel":
		X_sel = self._select_X(X)
		if y is None:
			# Some unsupervised estimators do not need y
			self.estimator.fit(X_sel, **fit_kwargs)
		else:
			self.estimator.fit(X_sel, y, **fit_kwargs)
		self._fitted = True
		return self

	def predict(self, X: Any, **predict_kwargs: Any) -> np.ndarray:
		if not self._fitted:
			# Best-effort check for scikit-learn style attribute
			if not hasattr(self.estimator, "predict"):
				raise RuntimeError("Estimator is not fitted and does not support predict().")
		X_sel = self._select_X(X)
		return self.estimator.predict(X_sel, **predict_kwargs)

	# -------------------------------
	# Evaluation (regression)
	# -------------------------------
	def evaluate_regression(self, X: Any, y_true: Iterable, **predict_kwargs: Any) -> dict:
		y_pred = self.predict(X, **predict_kwargs)
		y_true = np.asarray(list(y_true), dtype=float)
		y_pred = np.asarray(y_pred, dtype=float)
		mae = float(np.mean(np.abs(y_true - y_pred)))
		mse = float(np.mean((y_true - y_pred) ** 2))
		rmse = float(np.sqrt(mse))
		# r2 guard against zero variance
		var = np.var(y_true)
		r2 = float(1.0 - mse / var) if var > 0 else float("nan")
		return {"mae": mae, "mse": mse, "rmse": rmse, "r2": r2}

	# -------------------------------
	# Persistence (per-user)
	# -------------------------------
	def save(self, username: str, *, overwrite: bool = True) -> Path:
		models_dir = _user_models_dir(username)
		models_dir.mkdir(parents=True, exist_ok=True)
		path = models_dir / f"{self.metadata.model_name}.pkl"
		if path.exists() and not overwrite:
			raise FileExistsError(f"Model already exists: {path}")
		payload = {
			"estimator": self.estimator,
			"metadata": asdict(self.metadata),
			"fitted": self._fitted,
		}
		joblib.dump(payload, path)
		return path

	@classmethod
	def load(cls, username: str, model_name: str) -> "BaseModel":
		path = _user_models_dir(username) / f"{model_name}.pkl"
		if not path.exists():
			raise FileNotFoundError(f"No saved model for user '{username}': {path}")
		payload = joblib.load(path)
		md = payload.get("metadata", {})
		obj = cls(
			estimator=payload.get("estimator"),
			model_name=md.get("model_name", model_name),
			feature_columns=md.get("feature_columns"),
			target_column=md.get("target_column"),
			version=md.get("version", "0.1.0"),
			random_state=md.get("random_state"),
			extra=md.get("extra"),
		)
		obj._fitted = bool(payload.get("fitted", False))
		# Preserve original created_at if present
		if "created_at" in md:
			obj.metadata.created_at = md["created_at"]
		return obj

	# -------------------------------
	# Utilities
	# -------------------------------
	def set_feature_columns(self, columns: Sequence[str]) -> None:
		self.metadata.feature_columns = tuple(columns)

	def set_target_column(self, column: str) -> None:
		self.metadata.target_column = column

	def info(self) -> dict:
		return asdict(self.metadata)

	def __repr__(self) -> str:
		cls = self.__class__.__name__
		return f"{cls}(name={self.metadata.model_name!r}, version={self.metadata.version!r}, fitted={self._fitted})"