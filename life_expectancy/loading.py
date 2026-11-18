"""Functions for loading life expectancy data from disk."""

import pandas as pd


def load_data(file_path: str) -> pd.DataFrame:
    """Load life expectancy data from a TSV file."""
    return pd.read_csv(file_path, sep="\t")
