
my first website 

from bottle import run,route,template
from datetime import datetime

@route('/')
def index():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return template('homepage', time=current_time)


#main routine
run(reloader=True)