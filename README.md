### Introduction
This is a very simple Django web app to send Wake on Land magic packets to a computer to start it.
* Target computer can be managed by the simple django admin interface
* Page is password protected, users can be added on the django admin interface

### Production Setup
The easiest way to run this is with docker:
```
# build the container
docker built -t wakeonland .

# setup container and run it
docker run --name wakeonlan -d \
    -v wakeonlan_data:/data \
    -p 8000:8000 \
    -e ALLOWED_HOSTS=localhost \
    -e SECRET_KEY=a-secret-key \
    -e DATABASE_URL=sqlite:////data/db.sqlite3 \
    wakeonlan
```
Change the ALLOWED_HOSTS variable to how the app will be accessed, e.g. "localhost", wakeonlan.mydomain.com or an ip address.

Update the database: `docker exec -it wakeonlan /code/manage.py migrate`
Create a user: `docker exec -it wakeonlan /code/manage.py createsuperuser`

### Local development
* Copy the file `.env.dist` and name it `.env`.
* Install pipenv (e.g. `pip install pipenv`)
* Install dependencies: `pipenv install`
* Run the server: `./manage.py runserver`

### License
Licensed under the MIT license.
