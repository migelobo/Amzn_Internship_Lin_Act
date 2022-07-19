from bottle import route, run, template, redirect, get, post, request, static_file
import time
import RPi.GPIO as GPIO

HOST = '192.168.35.213'

@route('/')
def serve_homepage():
    return template('main.tpl')

@route('/Stepper_motor', method='POST')
def lol():
    lol =  request.forms.get('steps')
    return lol + "WTF"

run(host=HOST, port=80,debug=True,reloader=True)
