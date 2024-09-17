'''
My First website with bottle.py
'''
import pytz
from bottle import run,route,template
from datetime import datetime
import requests

@route('/')
def index():
    now = datetime.now(pytz.timezone('Pacific/Auckland'))
    current_time = now.strftime("%H:%M:%S:%A2")
    time = current_time
    name = 'David'
    response = requests.get(f"https://api.agify.io/?name={name}")
    response = response.json()
    age = response['age']   
    return template('homepage', time=time, name = name, age=age)


#main routine1
run(reloader=True)