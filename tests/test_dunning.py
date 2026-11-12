from decimal import Decimal

import pytest

from app.dunning import dunning_level


@pytest.mark.parametrize(
    ("days_late", "amount", "disputed", "reminders_sent", "expected"),
    [
        (90, "500.00", True, 3, "hold"),
        (0, "500.00", False, 0, "none"),
        (-5, "500.00", False, 0, "none"),
        (10, "500.00", False, 0, "reminder"),
        (30, "500.00", False, 1, "second_reminder"),
        (31, "500.00", False, 1, "second_reminder"),
        (60, "500.00", False, 2, "final_notice"),
        (61, "500.00", False, 3, "collection"),
        (61, "50.00", False, 3, "collection"),
        (61, "500.00", False, 2, "final_notice"),
        (61, "49.99", False, 3, "final_notice"),
    ],
)
def test_dunning_level(
    days_late: int, amount: str, disputed: bool, reminders_sent: int, expected: str
) -> None:
    assert dunning_level(days_late, Decimal(amount), disputed, reminders_sent) == expected
