from api.restplus import api
from flask_restx import Resource
import json
import time

import logging
logger = logging.getLogger("flask_app")

system_ns  = api.namespace('system', description = 'calling from system endpoints')

@system_ns.route('/health')
class HealthCheck(Resource):
    def get(self):
        health_status = "Flask App is up"  # You can customize this based on your checks
        return {"status": health_status}