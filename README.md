# Test task booking

RESTful API service

# Run application
1. Update .env file with your data

2. With docker: `docker-compose up` (docker should be installed)

3. Run tests: `docker-compose exec web python manage.py test`

Application will be available at http://127.0.0.1:8000


# Request example

`GET /reservation/`

##### List of reservation.

http://127.0.0.1:8000/reservation/  

