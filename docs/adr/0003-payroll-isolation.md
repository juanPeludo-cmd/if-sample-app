# ADR-0003: Payroll data stays on the client's infrastructure

- Status: Accepted

`app/payroll/` handles salaries. Its code and data are CONFIDENTIAL: no AI service outside
the client's own infrastructure may process them. The `payroll_entries` table is read and
written only by `run_payroll`.
