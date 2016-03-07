from cgi import parse_qs, escape

def app(environ, start_response):
    # Returns a dictionary in which the values are lists
    data = parse_qs(environ['QUERY_STRING'])
    status = '200 OK'
    response_headers = [
        ('Content-type','text/plain'),
        ('Content-Length', str(len(data)))
    ]
    start_response(status, response_headers)
    return iter([data])