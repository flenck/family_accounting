# Database Migrations

## 001 - Add category to transactions

- Date: 2025-12-26
- Reason: Support transaction classification (expense/income/category)
- SQLite: ALTER TABLE ADD COLUMN
- MySQL/Postgres: same logic, different syntax if needed