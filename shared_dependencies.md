Shared dependencies between the generated files:

index.html:
- app.js
- style.css

app.js:
- jQuery
- backend_logic.py
- frontend_tests.py

style.css:
- index.html

components.py:
- database_schema.sql

compatibility_rules.py:
- database_schema.sql

custom_configs.py:
- database_schema.sql

database_schema.sql:
- components.py
- compatibility_rules.py
- custom_configs.py

backend_logic.py:
- components.py
- compatibility_rules.py
- custom_configs.py

frontend_tests.py:
- app.js

deployment.sh:
- Git
- Odoo V16 CE