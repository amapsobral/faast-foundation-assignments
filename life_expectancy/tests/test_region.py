"""Tests for region codes."""

from life_expectancy.region import Region


def test_list_countries():
    """Return country codes while excluding non-country regions."""
    expected = set(
        """
        AL AM AT AZ BE BG BY CH CY CZ DE DK EE EL ES FI
        FR GE HR HU IE IS IT LI LT LU LV MD ME MK MT
        NL NO PL PT RO RS RU SE SI SK SM TR UA UK XK
        """.split()
    )
    assert set(Region.list_countries()) == expected
