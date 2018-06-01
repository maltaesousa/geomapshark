# geomapshark - a powerful geoform tool built with django

## Getting started

Clone the repository.

For windows:

`python -m pipenv install`

## Documentation

Rename `sample.env.yaml` to `env.yaml` and modifiy it according to your specific configuration.

### Setup database

`psql -U postgres -p PORTNUMBER`

```sql
DROP DATABASE geomapshark;
CREATE DATABASE geomapshark;
\c geomapshark
CREATE EXTENSION postgis;
CREATE SCHEMA geomapshark AUTHORIZATION geomapshark;
\q
```

Apply migrations

`python .\manage.py migrate`

Create a superuser to administrate you application:

`python .\manage.py createsuperuser`

### Populate database

Dump and restore existing data:

```
pg_dump -p PORTNUMBER -h HOSTNAME -U USERNAME -F c --no-privileges -f temp.sql -n geomapshark DATABASE
pg_restore -U postgres -d geomapshark -p PORTNUMBER --no-owner -a temp.sql
rm temp.sql
```

And reset sequences:

```
psql -p PORTNUMBER -U USERNAME -Atq -f reset_sequences.sql -o temp
psql -p PORTNUMBER -h HOSTNAME -U USERNAME -f temp
rm temp
```
