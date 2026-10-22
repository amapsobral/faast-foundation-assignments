"""script to clean the life expectancy dataset"""

from argparse import ArgumentParser
import pandas as pd

def clean_data(region: str = "PT"):
    """
    Cleans the tsv data in the data folder, filters
    for the given region and saves it as a CSV file.
    """

    df = pd.read_csv('life_expectancy/data/eu_life_expectancy_raw.tsv',sep = '\t')

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

    long_df.to_csv('life_expectancy/data/pt_life_expectancy.csv', index=False)

if __name__ == "__main__":  # pragma: no cover
    parser = ArgumentParser(description="Clean the life expectancy dataset")
    parser.add_argument("--region", default="PT", help="Region to filter for")
    clean_data(parser.parse_args().region)
