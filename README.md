# PYTHON_FLASK_BOILERPLATE

This repository contains:

1. [Colledge Flask Backend](/app/__init__.py) and modular structure.

Colledge project is aim to connect students around the world with they best match College.

## Table of content
- [Installation project in local enviroment](#install)
  
## Install

This project use [python](https://python.org) and [flask](https://flask.palletsprojects.com/en/1.1.x/). Also, using [virtualenv](https://virtualenv.pypa.io/) and [docker](https://docker.com) to setup **local development enviroment**. Go check them out if you don't have them locally installed. If you are done on install there things, please following:

Clone the project from github:

```sh
git clone 
```

Then go to our project root folder, to initialize local python (this will make all change like install library, update python version, … only affect to current project) use following command:

```sh
virtualenv venv # this will embed a small python enviroment on to venv folder
```

Activate local python envoriment we just created:

```sh
source venv/bin/activate
```

Install libraries listed in [requirements.txt](./requirements.txt):

```sh
pip install -r requirements.txt
```

At this step, our backend is really to run, but still require a Database. Using Docker, we will setup our database:

```sh
docker-compose -f docker-compose.dev.yml up --build -d # gonna take a white, one done we will have a postgresql
```

Then we need migrate database model from our backend application onto your local postgresql:

```sh
flask db init # one this done you will see the migration folder
flask db migrate -m "Initial migrate"
flask db upgrade
```

All set, your local development enviroment all set 🎉🎉🎉
  
Now, to start local development server:

```sh
sh ./scripts/start.sh
```

Or local production server:

```sh
sh ./scripts/serve.sh
```

Thanks you and happy hacking.
