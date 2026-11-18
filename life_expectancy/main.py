"""Command-line entry point for cleaning life expectancy data."""

from argparse import ArgumentParser

from .cleaning import clean_data
from .loading import load_data
from .saving import save_data

DEFAULT_DATA_FILE_PATH = "life_expectancy/data/eu_life_expectancy_raw.tsv"
DEFAULT_REGION = "PT"


def main():
    """Load, clean, and save life expectancy data for the selected region."""
    parser = ArgumentParser(description="Clean the life expectancy dataset")
    parser.add_argument(
        "--region",
        default=DEFAULT_REGION,
        help="Region to filter for",
        type=str,
    )
    args = parser.parse_args()

    data = load_data(DEFAULT_DATA_FILE_PATH)
    cleaned_data = clean_data(data, region=args.region)
    save_data(
        cleaned_data,
        f"life_expectancy/data/{args.region.lower()}_life_expectancy.csv",
    )
    return cleaned_data


if __name__ == "__main__":  # pragma: no cover
    main()
