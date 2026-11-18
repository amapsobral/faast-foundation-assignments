"""Functions for saving life expectancy data to disk."""

import pandas as pd


def save_data(data: pd.DataFrame, file_path: str) -> None:
    """Save life expectancy data to a CSV file."""
    data.to_csv(file_path, index=False)
