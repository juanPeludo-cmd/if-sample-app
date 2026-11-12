from fastapi import FastAPI

from app import customers, invoices, ledger, partner
from app.payroll import service as payroll

app = FastAPI(title="sample-app")
app.include_router(invoices.router)
app.include_router(customers.router)
app.include_router(payroll.router)
app.include_router(partner.router)
app.include_router(ledger.router)
