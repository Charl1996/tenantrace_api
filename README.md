# Tenantrace API


## DB setup
- Create a user called `tenantrace`
- Create a database called `tenantrace`
- Run: `GRANT ALL PRIVILEGES ON DATABASE tenantrace TO tenantrace`
- RUN: `GRANT ALL ON schema public TO tenantrace`


## Local development
### Server application in browser
`python manage.py runserver 0.0.0.0:8089`