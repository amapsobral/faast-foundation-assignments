"""Functions for cleaning the life expectancy dataset."""
import pandas as pd

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
    ).reset_index(drop=True)

    return long_df
