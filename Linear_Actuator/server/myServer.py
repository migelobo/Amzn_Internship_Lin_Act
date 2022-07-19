from bottle import route, run

@route('/hello')

def hello():
    return "Hello there..."

run(host='192.168.35.213',port=80,debug=True,reloader=True)
