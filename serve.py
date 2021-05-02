from wsgiref.simple_server import make_server

def application(env, start_response):
    headers = [ ('Content-type', 'text/plain') ]
    start_response('200 OK', headers)
    return ['hello world :v'.encode('utf-8')]

server = make_server('localhost', 9000, application)
server.serve_forever()
