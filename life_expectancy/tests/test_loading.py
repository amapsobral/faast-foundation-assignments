"""Tests for loading data"""

import pandas as pd

from life_expectancy.disk_ops import load_data


def test_loading(eu_life_expectancy_raw, tmp_path):
    """Test loading the raw fixture from a temporary TSV file."""
    source_path = tmp_path / "eu_life_expectancy_raw.tsv"
    eu_life_expectancy_raw.to_csv(source_path, sep="\t", index=False)

    loaded = load_data(str(source_path))

    pd.testing.assert_frame_equal(loaded, eu_life_expectancy_raw)
