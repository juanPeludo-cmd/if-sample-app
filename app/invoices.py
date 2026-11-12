"""Invoices: create, read, and the late fee (ADR-0002: money is Decimal, never float)."""

from decimal import ROUND_HALF_UP, Decimal

from fastapi import APIRouter, HTTPException

from app.db import get_session
from app.models import Invoice

router = APIRouter(prefix="/invoices")

LATE_FEE_RATE = Decimal("0.015")  # per 30 days late
LATE_FEE_CAP = Decimal("0.10")


def late_fee(amount: Decimal, days_late: int) -> Decimal:
    """1.5% of the amount per started 30 days late, capped at 10%."""
    periods = -(-days_late // 30) if days_late > 0 else 0
    rate = min(LATE_FEE_RATE * periods, LATE_FEE_CAP)
    return (amount * rate).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def invoice_total(invoice: Invoice) -> Decimal:
    return invoice.amount + late_fee(invoice.amount, invoice.days_late)


@router.post("")
def create_invoice(customer_id: int, amount: Decimal) -> dict[str, int]:
    session = get_session()
    invoice = Invoice(customer_id=customer_id, amount=amount)
    session.add(invoice)
    session.commit()
    return {"id": invoice.id}


@router.get("/reminder-fee")
def read_reminder_fee(days_late: int) -> dict[str, str]:
    """The reminder fee for an invoice this many days late; 501 until `reminder_fee` exists."""
    fee = globals().get("reminder_fee")
    if fee is None:
        raise HTTPException(501, "not implemented yet")
    try:
        return {"days_late": str(days_late), "reminder_fee": str(fee(days_late))}
    except ValueError as exc:
        raise HTTPException(400, str(exc)) from exc


@router.get("/{invoice_id}")
def read_invoice(invoice_id: int) -> dict[str, str]:
    invoice = get_session().get(Invoice, invoice_id)
    if invoice is None:
        raise HTTPException(404)
    return {"id": str(invoice.id), "total": str(invoice_total(invoice))}


def reminder_fee(days_late: int) -> Decimal:
    if days_late < 0:
        raise ValueError("days_late cannot be negative")
    if days_late <= 14:
        return Decimal("0.00")
    elif days_late <= 44:
        return Decimal("5.00")
    else:
        return Decimal("10.00")
