```
su - postgres bash -c "dropdb plants"
su - postgres bash -c "createdb plants"
su - postgres bash -c "psql < /home/workspace/plantsdb/plantsdb-setupsql.sql"
su - postgres bash -c "psql plants < /home/workspace/plantsdb/plants.psql"
```

```
psql -U postgres
CREATE DATABASE plants
\c plants
\i plantsdb_setup.sql
\i plants.psql
```
