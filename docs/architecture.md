# sample-app architecture

One FastAPI service over one database. Routers: `app/invoices.py`, `app/customers.py`,
`app/payroll/service.py` and `app/partner.py`. Partner API keys are checked by `app/auth/keys.py`. Persistence is SQLAlchemy (`app/db.py`, `app/models.py`).

`app.invoices.reminder_fee(days_late: int) -> Decimal` (app/invoices.py): Reminder fee for overdue invoices.

The late fee is computed by `late_fee` in `app/invoices.py`; see ADR-0002 for why money is
`Decimal`.
