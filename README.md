# Complete Django Girls Tutorial
This repository contains the code and some of my changes that one would eventually have were they to go through the [Django Girls tutorial](https://tutorial.djangogirls.org/en/).
## Differences
Expressing my authorial rights, some things are a bit different from the tutorial:
* Templates are a little bit different
* Button for delete all comments in your post
* Button for hide your comments
* Button for edit your comments before approve
* Some logicaly/html changes
## Setup
In a python virtual environment, run:
* `pip3 install -r requirements/dev.txt`
* `cp .env.template .env` (copy virtual environment variables to .env and write out them)
* `python manage.py migrate`
* `python manage.py createsuperuser` (to create user that you'll use to log in)
## Before run the application
* Create file called `.env`
* Copy `.env.template` to `.env`
* Fill out `.env` file

If you're going to start the app with docker, fill out all fields. Otherways, fill out only `SECRET_ADMIN_URL` field.
## Run the application localy with db sqlite3
```
python manage.py runserver
```
Now, you are good to go. Your blog is ready.
## Run the application with gunicorn
```
gunicorn mysite.wsgi -b 127.0.0.1:8000
```
That's it.
## Docker
To spin up the application using docker, ensure that docker is installed. Don't forget to fill out .env file. Then run:
```
sudo docker compose up -d --build
```
The application will be live at 127.0.0.1:8000 on gunicorn server with postgresql db.
## Blog entry
* Log in (with your super user credentials)
* Click on the `+` button, enter the title and text
* Finally hit the `paper plane` button
