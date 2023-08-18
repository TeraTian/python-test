from bottle import get, run

@get('/get')
def getName():
    return 'Hello World';

run(host='0.0.0.0', port='8888')