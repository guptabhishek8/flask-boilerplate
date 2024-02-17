from api.restplus import api
from flask_restx import Resource
from ..serializers.flask_logic1_serializer import flask_logic1_serializer, flask_logic1_response_model
from ..serializers.common_serializer import bad_request_response, unauthorized_response
from ...auth import requires_auth

import logging

logger = logging.getLogger("flask_app")


flask_logic1_ns  = api.namespace('flask_logic1-api', description = 'calling from flask_logic1-api')

@flask_logic1_ns.route('/route')
class ClassName(Resource):

    @requires_auth
    @api.expect(flask_logic1_serializer, validate = True)
    @api.marshal_with(flask_logic1_response_model, skip_none = True)
    @api.doc(responses = {401: ("Unautorized access", unauthorized_response),
                          400: ("Bad Request", bad_request_response)
                          })
    def post(self):
        # post api logic for this router
        
        return {"success":"success", "message": "message"}
