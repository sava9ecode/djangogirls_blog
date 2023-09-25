# Complete Django Girls Tutorial
This repository contains the code and some of my changes that one would eventually have were they to go through the [Django Girls tutorial](https://tutorial.djangogirls.org/en/).
## Differences
Expressing my authorial rights, some things are a bit different from the tutorial:
* Templates are a little bit different
* Button for delete all comments in your own posts
* Button for hide your own comments
* Button for edit your own comments before approve
* Maybe something else =)
## Setup
In a python virtual environment, run:
* `pip install -r requirements.txt`
* `python manage.py migrate blog`
* `python manage.py createsuperuser` (to create user that you'll use to log in)
## Run the application
```
python manage.py runserver
```
Now, you are good to go. Your blog is ready.
## Docker
To spin up the application using docker, ensure that Docker is installed. Then run:
```
sudo docker compose up -d --build
```
The application will be live at 0.0.0.0:8000
## Blog entry
* Log in
* Click on the `+` button, enter the title and text
* Finally hit the `Save` button
