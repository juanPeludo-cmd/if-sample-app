# sample-app

A small invoicing service used to demonstrate the Intelligent Flow context fabric.

- `app/invoices.py`: invoice endpoints and the late fee calculation.
- `app/customers.py`: customer lookup.
- `app/payroll/`: payroll runs. **CONFIDENTIAL** in `config/policy/data/repos.json`, so any
  context drawn from it keeps a model call on local models. High risk: one engineer or
  architect approves a change, through the cockpit or the CLI.
- `app/auth/`: partner API keys. **Critical** risk: a change needs two people to approve it.

Run the tests with `pytest`.
