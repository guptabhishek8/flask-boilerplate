import logging.config
from flask import Blueprint
from logger import setup_logging
# import mysql.connector
# import psycopg2

from api.restplus import api
from api.flask_app.endpoints.coreEndpoints import flask_logic1_ns
from api.flask_app.endpoints.systemEndpoints import system_ns
from api.flask_app.scheduler.scheduler_util import initialize_scheduler, schedule_tasks
from settings import MYSQL_UNDERWRITING_HOST, MYSQL_UNDERWRITING_DB, MYSQL_UNDERWRITING_PASSWORD, MYSQL_UNDERWRITING_USER, POSTGRES_UNDERWRITING_HOST_READ,POSTGRES_UNDERWRITING_DB_READ, POSTGRES_UNDERWRITING_PASSWORD_READ, POSTGRES_UNDERWRITING_USER_READ,MYSQL_UNDERWRITING_USER_READ_ONLY,MYSQL_UNDERWRITING_PASSWORD_READ_ONLY


logger = logging.getLogger("flask_app")

def configure_app(flask_app, config):
    flask_app.config.from_object(config)

def configure_db_sql():
    # cnx =  mysql.connector.connect(user=MYSQL_UNDERWRITING_USER, password=MYSQL_UNDERWRITING_PASSWORD,
    #                           host=MYSQL_UNDERWRITING_HOST, database=MYSQL_UNDERWRITING_DB)
    # return cnx
    pass

def configure_db_sql_read_only():
    # logger.info("MYSQL_UNDERWRITING_USER_READ_ONLY: {}, MYSQL_UNDERWRITING_PASSWORD_READ_ONLY :{}, host=MYSQL_UNDERWRITING_HOST: {}, database=MYSQL_UNDERWRITING_DB: {}".format(MYSQL_UNDERWRITING_USER_READ_ONLY, MYSQL_UNDERWRITING_PASSWORD_READ_ONLY, MYSQL_UNDERWRITING_HOST, MYSQL_UNDERWRITING_DB))
    # cnx =  mysql.connector.connect(user=MYSQL_UNDERWRITING_USER_READ_ONLY, password=MYSQL_UNDERWRITING_PASSWORD_READ_ONLY,
    #                           host=MYSQL_UNDERWRITING_HOST, database=MYSQL_UNDERWRITING_DB)
    
    # return cnx
    pass

def configure_db_postgres():
    # cnx =  psycopg2.connect(user=POSTGRES_UNDERWRITING_USER_READ, password=POSTGRES_UNDERWRITING_PASSWORD_READ,
    #                           host=POSTGRES_UNDERWRITING_HOST_READ, database=POSTGRES_UNDERWRITING_DB_READ)
    # return cnx
    pass

def initialize_app(flask_app,config = 'settings'):
    setup_logging()
    configure_app(flask_app, config=config)

    # Register API blueprint
    blueprint = Blueprint("api", __name__, url_prefix = '/v1')
    api.init_app(blueprint)
    api.add_namespace(flask_logic1_ns)
    api.add_namespace(system_ns)


    # Schedule tasks
    # initialize_scheduler()

    # schedule_tasks()

    # Register API blueprint: FlaskApp
    flask_app.register_blueprint(blueprint)

    return flask_app