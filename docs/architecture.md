# sample-app architecture

One FastAPI service over one database. Routers: `app/invoices.py`, `app/customers.py`,
`app/payroll/service.py` and `app/partner.py`. Partner API keys are checked by `app/auth/keys.py`. Persistence is SQLAlchemy (`app/db.py`, `app/models.py`).

`app.payroll.service.overtime_pay(hourly: Decimal, hours: int) -> Decimal` (app/payroll/service.py): Overtime pay in payroll.

Updated the description of `app.auth.keys.check_key` function to reflect the new implementation.

`app.invoices.reminder_fee(days_late: int) -> Decimal` (app/invoices.py): Reminder fee for overdue invoices.

The late fee is computed by `late_fee` in `app/invoices.py`; see ADR-0002 for why money is
`Decimal`.
