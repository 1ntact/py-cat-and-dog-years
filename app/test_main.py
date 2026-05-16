from app.main import get_human_age


def test_get_human_age_when_values_under_15() -> None:
    animal_ages = get_human_age(14, 14)
    assert animal_ages == [0, 0]


def test_get_human_age_two_values_15() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_get_human_age_values_24() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_get_human_age_values_28() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_get_human_age_values_100() -> None:
    assert get_human_age(100, 100) == [21, 17]
