# Raw data

Place the downloaded public support-ticket CSV in this folder.

Recommended columns:
- ticket_id
- ticket_text
- priority
- category
- team
- created_at
- first_response_at
- resolved_at
- sla_breached

If the dataset uses different names, map them in `src/prepare_data.py`.

Do not commit private tickets, customer names, email addresses, phone numbers, or other personally identifiable information.
