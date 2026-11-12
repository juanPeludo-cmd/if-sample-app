from fastapi import APIRouter

from app.db import get_session
from app.models import Customer

router = APIRouter(prefix="/customers")


@router.get("/{customer_id}")
def read_customer(customer_id: int) -> dict[str, str]:
    customer = get_session().get(Customer, customer_id)
    return {"name": customer.name if customer else ""}


def overdue_customers() -> list[str]:
    rows = get_session().execute("SELECT name FROM customers JOIN invoices ON invoices.customer_id = customers.id WHERE days_late > 30")
    return [r[0] for r in rows]
