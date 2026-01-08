"""
Command-line interface for the application.
Allows users to log workouts, get predictions, and view progression stats.
"""

import argparse

from .data_pipeline import preprocess_baseline_data, dataset_stats


def main(argv: list[str] | None = None) -> int:
	parser = argparse.ArgumentParser(prog="pwp", description="Personalized Workout Progression System")
	sub = parser.add_subparsers(dest="command", required=True)

	sub.add_parser("preprocess", help="Preprocess baseline datasets and write processed CSVs")
	sub.add_parser("stats", help="Show basic stats for baseline datasets (rows, workouts, avg sets)")

	args = parser.parse_args(argv)

	if args.command == "preprocess":
		df4k, df721, df_all = preprocess_baseline_data(write_outputs=True)
		print(f"Processed 4k rows: {len(df4k)}")
		print(f"Processed 721 rows: {len(df721)}")
		print(f"Combined processed rows: {len(df_all)}")
		return 0
	elif args.command == "stats":
		df4k, df721, df_all = preprocess_baseline_data(write_outputs=False)
		s4k = dataset_stats(df4k)
		s721 = dataset_stats(df721)
		sall = dataset_stats(df_all)
		print("4k:", s4k)
		print("721:", s721)
		print("ALL:", sall)
		return 0

	return 0


if __name__ == "__main__":
	raise SystemExit(main())