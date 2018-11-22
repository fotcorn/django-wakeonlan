### Introduction
This is a very simple Django web app to send Wake on Land magic packets to a computer to start it.


### Production Setup
The easiest way to run this is with docker and docker-compose.

Set the following environment variables:
* DOMAIN: How the app will be accessed, e.g. "localhost", wakeonlan.mydomain.com or an ip address
* SECRET_KEY: A randomly generated key used by django the e.g. encrypt session cookies
* POSTGRES_PASSWORD: A password to authenticate on the postgres server

And the run the following commands:
* Run `docker-compose up -d` to start the app.
* Run `docker-compose exec django /code/manage.py migrate` to generate the database fields
* Run `docker-compose exec django /code/manage.py createsuperuser` to create a user

### Local development
* Copy the file `.env.dist` and name it `.env`.
* Install pipenv (e.g. `pip install pipenv`)
* Install dependencies: `pipenv install`
* Run the server: `./manage.py runserver`

### License
Licensed under the MIT license.
