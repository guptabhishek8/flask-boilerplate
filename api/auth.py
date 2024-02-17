from flask import request, Response
from settings import BASIC_AUTH_USERNAME, BASIC_AUTH_PASSWORD

basicAuthUsername = BASIC_AUTH_USERNAME 
basicAuthPassword = BASIC_AUTH_PASSWORD

def check_auth(username, password):
    # Replace these with your actual username and password
    return username == basicAuthUsername and password == basicAuthPassword


def requires_auth(f):
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth:
            return Response('Unauthorized', 401, {'WWW-Authenticate': 'Basic realm="Login Required"'})
        if not check_auth(auth.username, auth.password):
            return Response('Unauthorized', 401, {'WWW-Authenticate': 'Basic realm="Login Required"'})
        return f(*args, **kwargs)
    return decorated