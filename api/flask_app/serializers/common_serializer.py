from flask_restx import reqparse, fields
from api.restplus import api
# from settings import ENV, DEBUG

# Unauthenticated response model.
unauthorized_response = api.model('UNAUTHORIZED_MODEL', {
    'message': fields.String("Unauthorized access."),
})
# Bad request response model.
bad_request_response = api.model('BAD_REQUEST_RESPONSE', {
    'errors': fields.Raw({"field_name": "error_message"}),
    'message': fields.String
})

pagination_data_model = api.model('PAGINATION_DATA', {
    'total_pages': fields.Integer(),
    'page': fields.Integer(),
    'per_page': fields.Integer()
})