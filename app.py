from bottle import get, run, request

@get('/get')
def getName():
    name = request.query.name
    return 'Hello Allied v ' + name;

run(host='0.0.0.0', port='8888')
