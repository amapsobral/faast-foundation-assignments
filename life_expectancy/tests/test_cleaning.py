"""Tests for the cleaning module"""
import pandas as pd

from life_expectancy import cleaning
from life_expectancy.disk_ops import load_data, save_data
from . import OUTPUT_DIR


def test_clean_data(pt_life_expectancy_expected):
    """Run the `clean_data` function and compare the output to the expected output"""
    df = load_data(cleaning.DEFAULT_DATA_FILE_PATH)
    clean_df = cleaning.clean_data(df)
    save_data(clean_df, OUTPUT_DIR / "pt_life_expectancy.csv")

    pt_life_expectancy_actual = pd.read_csv(
        OUTPUT_DIR / "pt_life_expectancy.csv"
    )
    pd.testing.assert_frame_equal(
        pt_life_expectancy_actual, pt_life_expectancy_expected
    )

def test_main(monkeypatch):
    """Test the main function of the cleaning module"""
    source = pd.DataFrame({
        "unit,sex,age,region": ["Y,T,TOTAL,FR"],
        "2020": ["82.5"],
    })
    loaded_paths = []
    saved = {}

    def fake_load_data(path):
        loaded_paths.append(path)
        return source

    def fake_save_data(df, path):
        saved["df"] = df
        saved["path"] = path

    monkeypatch.setattr("sys.argv", ["cleaning", "--region", "FR"])
    monkeypatch.setattr(cleaning, "load_data", fake_load_data)
    monkeypatch.setattr(cleaning, "save_data", fake_save_data)

    cleaning.main()

    assert loaded_paths == [cleaning.DEFAULT_DATA_FILE_PATH]
    assert saved["path"] == "life_expectancy/data/fr_life_expectancy.csv"
    assert saved["df"]["region"].tolist() == ["FR"]
