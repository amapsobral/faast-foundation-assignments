"""Module for handling disk operations related to life expectancy data."""

import pandas as pd

def load_data(file_path: str) -> pd.DataFrame:
    """Load life expectancy data from a CSV file."""
    return pd.read_csv(file_path, sep="\t")

def save_data(data: pd.DataFrame, file_path: str) -> None:
    """Save life expectancy data to a CSV file."""
    data.to_csv(file_path, index=False)
