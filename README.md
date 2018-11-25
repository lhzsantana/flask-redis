# Flask and Redis
Delevoped as a PoC to a flask server based on Redis

## Create virtual environment and import dependencies
$ virtualenv -p python3 flask-redis
$ cd flask-redis
$ pip import redis
$ pip import flask

## Start server
$ export FLASK_APP=server.py
The server will be on http://localhost:5000
