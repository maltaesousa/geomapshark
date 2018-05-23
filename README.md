# geomapshark - a powerful geoform tool built with django

## Documentation

### Windows specific configuration:
set GDAL_DATA environnement variable (for example: C:\Program Files\QGIS 3.0\share\gdal)

### Setup database

`psql -U postgres -p 5434`

```sql
DROP DATABASE geomapshark;
CREATE DATABASE geomapshark;
\c geomapshark
CREATE EXTENSION postgis;
\q
```

`py -3 .\manage.py createsuperuser`