# Changelog

Kept current by the Documentation agent.

## Unreleased

- STORY-205: Moved late fee logic to a new file `app/late_fee.py` and introduced `app.late_fee.late_fee_settings()` to read settings from `app/late_fee.yaml`.
- STORY-201: Added `reminder_fee` function to compute fixed reminder fees for overdue invoices.
