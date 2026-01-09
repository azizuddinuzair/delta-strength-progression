# Repository Cleanup Audit

## USED FILES (Keep)

### Core Application
- ✅ run_app.py – Main CLI entry point
- ✅ src/auth.py – User authentication
- ✅ src/ui.py – Terminal UI
- ✅ src/session_logger.py – Session logging
- ✅ src/model_quality.py – Quality metrics
- ✅ src/recommendation_engine.py – Recommendations
- ✅ src/plot_generator.py – Plot generation

### Active Data Processing
- ✅ src/data_pipeline.py – Feature engineering
- ✅ src/data_store.py – Data persistence
- ✅ src/personalized_prediction.py – Calibration
- ✅ src/rule_based.py – Fallback logic

### Models
- ✅ src/models/base_model.py – Base class
- ✅ src/models/compound_models.py – Trained models
- ✅ src/utils/user_personalization.py – User registry
- ✅ src/utils/exercise_mapping.py – Exercise mapping

### Testing (Active)
- ✅ test_workflow.py – Integration test
- ✅ test_app_modules.py – Module validation
- ✅ test_plot_generation.py – Plot testing
- ✅ test_plot_workflow.py – Plot workflow

### Documentation (Active)
- ✅ README.md – Project overview
- ✅ DEVELOPER_GUIDE.md – Dev guide
- ✅ APP_README.md – User guide
- ✅ QUICKSTART.py – Setup automation
- ✅ PLOTS_QUICK_START.md – Plot quick ref
- ✅ PLOT_FEATURE_SUMMARY.md – Plot details
- ✅ IMPLEMENTATION_COMPLETE.md – Feature complete

### Configuration
- ✅ requirements.txt – Dependencies
- ✅ setup.py – Package setup
- ✅ .gitignore – Git excludes

---

## UNUSED/LEGACY FILES (DELETE)

### Obsolete CLI
- ❌ src/cli.py – OLD CLI (superseded by run_app.py)
  - "Legacy CLI" per documentation
  - Functionality now in run_app.py
  - Not imported by active code
  - Can train models with src.cli but not essential

### Unused Model Files
- ❌ src/models/dev_diagnostic.py – Development diagnostic tool
  - Not imported anywhere
  - Used for development debugging
  
- ❌ src/models/fatigue_model.py – Not implemented
  - Empty or partial implementation
  - Not used by compound models
  
- ❌ src/models/progression_model.py – Stub/partial
  - Not integrated
  - Superseded by compound_models.py

### Unused Utilities
- ❌ src/utils.py – Old plotting utilities
  - Duplicates functionality
  - matplotlib functions replaced by plot_generator.py
  - Not imported by active code

- ❌ src/workout_generator.py – Not integrated
  - Not imported anywhere
  - Stub implementation

### Obsolete Stub Files
- ❌ src/gui.py – GUI stub (KEEP per user request but unused)
  - Keep as placeholder for future

### Unorganized Root-Level Files (Move to docs/)
- ⚠️ DELIVERY_COMPLETE.md – Delivery summary (move to docs/ARCHIVE/)
- ⚠️ IMPLEMENTATION_SUMMARY.md – Tech summary (move to docs/ARCHIVE/)
- ⚠️ MANIFEST.txt – File manifest (move to docs/ARCHIVE/)
- ⚠️ README_APP.txt – Text summary (move to docs/ARCHIVE/)
- ⚠️ COMPOUND_MODELS.md – Old doc (move to docs/ARCHIVE/)

### Obsolete Test Files
- ⚠️ test_diagnostic.py – Diagnostic test (move to docs/ARCHIVE/)
- ⚠️ tests/final_validation_cv.py – Validation test (move to docs/ARCHIVE/)
- ⚠️ tests/squat_model_example.py – Example (move to docs/ARCHIVE/)
- ⚠️ tests/test_calibrated_user2_squat.py – Specific test (move to docs/ARCHIVE/)
- ⚠️ tests/test_compound_models.py – Old unit test (move to docs/ARCHIVE/)
- ⚠️ tests/test_models.py – Old test (move to docs/ARCHIVE/)
- ⚠️ tests/test_personalized_prediction.py – Old test (move to docs/ARCHIVE/)
- ⚠️ tests/test_pipeline.py – Old test (move to docs/ARCHIVE/)
- ⚠️ tests/test_rule_based.py – Old test (move to docs/ARCHIVE/)
- ⚠️ tests/test_user2_squat.py – Specific test (move to docs/ARCHIVE/)
- ⚠️ tests/test_workout_generator.py – Old test (move to docs/ARCHIVE/)

### Debug/Dev Scripts (Move to scripts/ARCHIVE/)
- ⚠️ scripts/*.py – All dev scripts (10+ files)
  - These are for development/debugging
  - Not essential for running app
  - Move to scripts/ARCHIVE/ if keep

### Init Scripts
- ⚠️ init_session_audit.py – One-time setup (move to docs/ARCHIVE/ or data/auth/)
  - Used once for DB setup
  - Now handled by QUICKSTART.py
  
- ⚠️ data/auth/init_auth_db.py – Already moved to right place

### Notebooks (Keep, Move Old to Archive)
- ✅ notebooks/model_workflow_user2_squat.ipynb – Keep (active demo)
- ⚠️ notebooks/baseline_model.ipynb – Move to docs/notebooks_archive/
- ⚠️ notebooks/random_forest.ipynb – Move to docs/notebooks_archive/
- ⚠️ notebooks/data_exploration/ – Move to docs/notebooks_archive/

### Session/Local Files
- ⚠️ .local/SESSION_LOG.md – Move to docs/ARCHIVE/

### Cache Files (Already in .gitignore)
- ⚠️ .pytest_cache/ – Not tracked, auto-generated

---

## ORGANIZATION PLAN

### Structure After Cleanup

```
Personalized-Workout-Progression-System/
├── src/                          # Active code only
│   ├── __init__.py
│   ├── auth.py
│   ├── ui.py
│   ├── session_logger.py
│   ├── model_quality.py
│   ├── recommendation_engine.py
│   ├── plot_generator.py
│   ├── data_pipeline.py
│   ├── data_store.py
│   ├── personalized_prediction.py
│   ├── rule_based.py
│   ├── gui.py                    # Stub kept
│   ├── models/
│   │   ├── __init__.py
│   │   ├── base_model.py
│   │   └── compound_models.py
│   └── utils/
│       ├── __init__.py
│       ├── user_personalization.py
│       └── exercise_mapping.py
│
├── tests/                        # Active tests only
│   ├── __init__.py
│   ├── test_workflow.py
│   ├── test_app_modules.py
│   ├── test_plot_generation.py
│   └── test_plot_workflow.py
│
├── notebooks/                    # Active notebooks only
│   └── model_workflow_user2_squat.ipynb
│
├── docs/                         # Active + archived docs
│   ├── README.md                 # Moved here
│   ├── MODEL_ASSUMPTIONS_AND_SCOPE.md
│   ├── observations.txt
│   ├── ARCHIVE/                  # New: old docs
│   │   ├── DELIVERY_COMPLETE.md
│   │   ├── IMPLEMENTATION_SUMMARY.md
│   │   ├── COMPOUND_MODELS.md
│   │   ├── MANIFEST.txt
│   │   ├── README_APP.txt
│   │   ├── test_diagnostic.py
│   │   ├── test_*.py (all old tests)
│   │   └── SESSION_LOG.md
│   └── notebooks_archive/       # New: old notebooks
│       ├── baseline_model.ipynb
│       ├── random_forest.ipynb
│       └── data_exploration/
│
├── scripts/                      # Dev only
│   ├── ARCHIVE/                  # New: dev scripts
│   │   └── *.py (all dev scripts)
│   └── README.md                 # Explain they're for dev
│
├── data/
│   ├── auth/
│   │   ├── init_auth_db.py       (keep, or move to scripts)
│   │   └── app_users.db
│   ├── baseline/
│   ├── processed/
│   ├── user_inputs/
│   ├── user_data.db
│   └── README.md
│
├── models/                       # Keep structure
│   └── compounds/
│
├── users/
│
├── data_plots/
│
├── Root-level files
│   ├── README.md                 # Main entry
│   ├── DEVELOPER_GUIDE.md        # Keep
│   ├── PLOTS_QUICK_START.md      # Keep
│   ├── PLOT_FEATURE_SUMMARY.md   # Keep
│   ├── IMPLEMENTATION_COMPLETE.md # Keep
│   ├── APP_README.md             # Keep or move to docs/
│   ├── QUICKSTART.py             # Keep
│   ├── run_app.py                # Keep
│   ├── setup.py
│   ├── requirements.txt
│   └── .gitignore
│
├── LICENSE
└── .git/
```

---

## DELETION LIST

Delete these files (they're not imported, obsolete):
1. src/cli.py
2. src/models/dev_diagnostic.py
3. src/models/fatigue_model.py
4. src/models/progression_model.py
5. src/utils.py
6. src/workout_generator.py

---

## MOVE TO docs/ARCHIVE/

Move these old documentation/test files:
1. DELIVERY_COMPLETE.md
2. IMPLEMENTATION_SUMMARY.md
3. MANIFEST.txt
4. README_APP.txt
5. COMPOUND_MODELS.md (from docs/)
6. test_diagnostic.py
7. All tests/* files except test_*.py in tests/ (keep integration tests)
8. .local/SESSION_LOG.md

---

## MOVE TO docs/notebooks_archive/

1. notebooks/baseline_model.ipynb
2. notebooks/random_forest.ipynb
3. notebooks/data_exploration/

---

## MOVE TO scripts/ARCHIVE/

1. All scripts/* files (dev/debug scripts)

Create scripts/README.md explaining they're dev-only

---

## Path Updates Needed

After moving files, update imports in:

1. run_app.py
   - FROM: various imports
   - TO: No changes (imports are from src/)

2. QUICKSTART.py
   - Update path to init_auth_db.py if moved

3. docs/README.md
   - Update references to old file locations

4. Any notebooks that reference old file locations

---

## Summary

- **Delete:** 6 obsolete source files
- **Move to archive:** ~20 old test/doc files
- **Move notebooks:** 3 old notebooks + folder
- **Net result:** Clean, focused repo
  - src/ has only active code
  - tests/ has only active tests
  - docs/ organized with archive
  - Root level: only essential files
  - No breaking changes to active system
