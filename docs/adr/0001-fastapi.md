# ADR-0001: FastAPI for the HTTP layer

- Status: Accepted

FastAPI gives typed request validation and OpenAPI docs. Routers live one per domain:
`app/invoices.py`, `app/customers.py`, `app/payroll/service.py`.
