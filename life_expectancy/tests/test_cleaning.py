"""Tests for the cleaning module"""
import pandas as pd

from life_expectancy import cleaning


def test_clean_data(eu_life_expectancy_raw, pt_life_expectancy_expected):
    """Run the `clean_data` function and compare the output to the expected output"""
    clean_df = cleaning.clean_data(eu_life_expectancy_raw)

    pd.testing.assert_frame_equal(
        clean_df, pt_life_expectancy_expected
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

    cleaned_df = cleaning.main()

    assert loaded_paths == [cleaning.DEFAULT_DATA_FILE_PATH]
    assert saved["path"] == "life_expectancy/data/fr_life_expectancy.csv"
    assert saved["df"]["region"].tolist() == ["FR"]
    pd.testing.assert_frame_equal(cleaned_df, saved["df"])
