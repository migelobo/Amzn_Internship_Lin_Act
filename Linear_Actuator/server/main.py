from bottle import route,run,static_file, template
import time
from datetime import datetime

HOST = '192.168.35.213'

@route('/')
def serve_homepage():
    lol = 'lmfao u thot'
    lol2 = 'hedgehog 4 life'
    time = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    
    my_data = {
        'temp_value' : lol,
        'humid_value': lol2,
        'my_time': time
        }
    return template('main.tpl', **my_data)

run(host=HOST, port=80,debug=True,reloader=True)