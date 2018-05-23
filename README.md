# geomapshark - a powerful geoform tool built with django

## Getting started

Clone the repository.

For windows:

`python -m pipenv install`

## Documentation

Rename `sample.env.yaml` to `env.yaml` and modifiy it according to your specific configuration.

### Setup database

`psql -U postgres -p 5434`

```sql
DROP DATABASE geomapshark;
CREATE DATABASE geomapshark;
\c geomapshark
CREATE EXTENSION postgis;
\q
```

`python .\manage.py createsuperuser`