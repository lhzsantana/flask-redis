import redis
import random
import datetime
from flask import Flask
app = Flask(__name__)

r = redis.Redis(host='127.0.0.1', port=6379, db=0)

LAST_PREFIX="last"
COUNTER_PREFIX="counter"
WINDOW_PREFIX="window"
LIST_PREFIX="list"
all_genders = ['male', 'female', 'undefined']

@app.route("/genders/<clientId>")
def genders(clientId):
    return top(clientId)

def last(clientId):
    return str(r.get(LAST_PREFIX+clientId))  

def top(clientId):
    genders = {}
    top_gender='not a client'
    top_counter=0
    for gender in all_genders:
	c=r.get(COUNTER_PREFIX+":"+str(clientId)+":"+gender)
	if c>top_counter :
		top_gender=gender
		top_counter=c
    return top_gender

def window(clientId):
    top_gender='not a client'
    top_counter=0
    for gender in all_genders:
	c=r.get(WINDOW_PREFIX+":"+str(clientId)+":"+gender)
	if c>top_counter :
		top_gender=gender
		top_counter=c
    return top_gender


