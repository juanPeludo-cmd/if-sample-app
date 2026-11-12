from decimal import Decimal

from app.ledger import balance, postings

EXPORT = "P-1;7;10.00\nP-2;7;2.50\nP-1;7;10.00\nP-3;8;1.00"


def test_a_posting_exported_twice_counts_once() -> None:
    assert [p[0] for p in postings(EXPORT)] == ["P-1", "P-2", "P-3"]


def test_a_customers_balance_sums_their_postings() -> None:
    assert balance(7, EXPORT) == (2, Decimal("12.50"))
    assert balance(9, EXPORT) == (0, Decimal("0"))


def test_the_nightly_export_has_every_customer() -> None:
    count, total = balance(1)
    assert count == 100
    assert total > 0
