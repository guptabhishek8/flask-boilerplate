import logging

# package
from flask_restx import Api

log = logging.getLogger("flask_app")

api = Api(version='0.0.1', title='Flask App API',
          description='Contains All APIs related to application.', validate=True,
          doc='/doc/')


@api.errorhandler
def default_error_handler(e):
    message = 'An unhandled exception occurred: ' + str(e)
    log.exception(message)
    log.info("Info An unhandled exception occurred: {}".format(str(e)))

    return {'message': message}, 500

