from decimal import Decimal

from app.statements import statement_totals


def test_an_empty_statement_is_all_zero() -> None:
    zero = Decimal("0.00")
    assert statement_totals([]) == {"open": zero, "overdue": zero, "fees": zero, "due": zero}


def test_open_and_overdue_invoices_with_their_fees() -> None:
    totals = statement_totals([(Decimal("100.00"), 0), (Decimal("200.00"), 31),
                               (Decimal("10.005"), 45)])  # fmt: skip
    assert totals == {
        "open": Decimal("100.00"),
        "overdue": Decimal("210.01"),
        "fees": Decimal("6.30"),
        "due": Decimal("216.31"),
    }
