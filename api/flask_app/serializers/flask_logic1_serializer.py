from flask_restx import reqparse, fields, inputs
from api.restplus import api

flask_logic1_serializer = api.parser()

# add argument required in API
flask_logic1_serializer.add_argument("source", type= str, required = True)
flask_logic1_serializer.add_argument("target", type= str, required = True)


flask_logic1_response_model = api.model("FLASK_LOGIC_1_RESPONSE", {
    "success": fields.Boolean(),
    "message": fields.String()
})