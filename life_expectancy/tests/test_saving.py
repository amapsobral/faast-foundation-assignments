"""Tests for saving data"""

from unittest.mock import Mock

import pandas as pd

from life_expectancy.saving import save_data


def test_saving(monkeypatch):
    """Test that the save_data function calls to_csv with the correct arguments"""
    data = pd.DataFrame({"value": [1]})
    to_csv = Mock()
    monkeypatch.setattr(data, "to_csv", to_csv)

    save_data(data, "output.csv")

    to_csv.assert_called_once_with("output.csv", index=False)
