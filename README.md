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

You can also use docker compose:
```
export DOMAIN your-domain-or-ip
export SECRET_KEY some_random_key
docker-compose up -d
docker-compose exec django /code/manage.py migrate
docker-compose exec django /code/manage.py createsuperuser
```

### Raspberry Pi Wifi and direct Ethernet cable from PI to PC
My setup is a Raspberry Pi 3 B+ connected via Wifi to my router and via Ethernet cable to my PC
(The PC is also connect by Wifi to the router).
This app runs inside a Docker container as documented above on the Raspberry Pi.
So make this work, some special configuration is required so the app knows on which interface the magic
packet should be sent:

* Configure a static IP for the Ethernet connection with a different subnet than used on your Wifi connection (e.g. 192.168.10.1)
* Configure the broadcast IP of this subnet as the IP Address in the admin interface of the app (e.g. 192.168.10.255)

### Local development
* Copy the file `.env.dist` and name it `.env`.
* Install pipenv (e.g. `pip install pipenv`)
* Install dependencies: `pipenv install`
* Run the server: `./manage.py runserver`

### License
Licensed under the MIT license.
