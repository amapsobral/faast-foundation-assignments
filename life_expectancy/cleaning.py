"""script to clean the life expectancy dataset"""

from argparse import ArgumentParser
import pandas as pd

from .disk_ops import save_data, load_data

DEFAULT_DATA_FILE_PATH = 'life_expectancy/data/eu_life_expectancy_raw.tsv'
DEFAULT_REGION = "PT"

def clean_data(df: pd.DataFrame, region: str = "PT") -> pd.DataFrame:
    """
    Cleans the tsv data in the data folder, filters
    for the given region and saves it as a CSV file.
    """

    df_info = df.iloc[:, 0].str.split(",", expand=True)
    df_info.columns = ["unit", "sex", "age", "region"]

    wide_df = pd.concat([df_info, df.iloc[:, 1:]], axis=1)

    long_df = wide_df.melt(
        id_vars=["unit", "sex", "age", "region"],
        var_name="year",
        value_name="value",
    )

    long_df["year"] = pd.to_numeric(long_df["year"], errors="coerce")
    long_df["value"] = pd.to_numeric(
        long_df["value"].astype(str).str.extract(r"(\d+\.?\d*)")[0],
        errors="coerce",
    )

    long_df = long_df.dropna(subset=["year", "value"])
    long_df["year"] = long_df["year"].astype(int)
    long_df = long_df[long_df["region"] == region].sort_values(
        "year",
        ascending=False
    )

    return long_df

def main() -> None:
    """Main function to clean the life expectancy dataset based on the given region."""
    parser = ArgumentParser(description="Clean the life expectancy dataset")
    parser.add_argument(
        "--region",
        default=DEFAULT_REGION,
        help="Region to filter for",
        type=str
    )
    args = parser.parse_args()

    df = load_data(DEFAULT_DATA_FILE_PATH)
    cleaned_df = clean_data(df, region=args.region)
    save_data(cleaned_df, f'life_expectancy/data/{args.region.lower()}_life_expectancy.csv')

if __name__ == "__main__":  # pragma: no cover
    main()
