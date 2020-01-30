## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
This project is simple blog site.
	
## Technologies
Project is created with:
* Python: 3+
* Django version: 2.2
* Postgresql
* psycopg2
	
## Setup

Clone project:
```
$ git clone https://github.com/dendy1922/app.git
```
Packaging up model changes into individual migration files:
```
$ python manage.py makemigrations
```
Applying changes:
```
$ python manage.py migrate
```
Run server:
```
$ python manage.py runserver
```
