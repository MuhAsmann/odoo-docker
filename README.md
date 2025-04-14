```docker compose exec db psql -U odoo -d postgres -c "CREATE DATABASE odoodb OWNER odoo;"```



```docker compose exec db psql -U odoo -d postgres -c "DROP DATABASE odoo;"```

How To Run
Command
```docker compose up -d```

Access on
http://localhost:8069/
