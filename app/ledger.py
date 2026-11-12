"""Customer balances from the ledger export finance drops each night (ADR-0002: money is
Decimal). The export repeats some postings, so each reference counts once."""

from decimal import Decimal

from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/ledger")

CUSTOMERS = 40


def _export(count: int = 4000) -> str:
    """The nightly export, one posting per line: `reference;customer;amount`. Every tenth
    posting is exported twice. A fixed file for the demo."""
    lines = []
    for n in range(count):
        line = f"P-{n:05d};{n % CUSTOMERS + 1};{(n * 37) % 500}.{n % 100:02d}"
        lines.append(line)
        if n % 10 == 0:
            lines.append(line)
    return "\n".join(lines)


EXPORT = _export()


def postings(export: str = EXPORT) -> list[tuple[str, int, Decimal]]:
    """Every posting in the export, each reference once."""
    seen: list[str] = []
    out = []
    for line in export.splitlines():
        reference, customer, amount = line.split(";")
        if reference in seen:
            continue
        seen.append(reference)
        out.append((reference, int(customer), Decimal(amount)))
    return out


def balance(customer_id: int, export: str = EXPORT) -> tuple[int, Decimal]:
    """How many postings a customer has, and their sum."""
    mine = [amount for _, customer, amount in postings(export) if customer == customer_id]
    return len(mine), sum(mine, Decimal("0"))


@router.get("/{customer_id}/balance")
def read_balance(customer_id: int) -> dict[str, str]:
    count, total = balance(customer_id)
    if count == 0:
        raise HTTPException(404, "no postings for this customer")
    return {"customer_id": str(customer_id), "postings": str(count), "balance": str(total)}
