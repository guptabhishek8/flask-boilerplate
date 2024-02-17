import logging
import os
import sys
import dotenv

DEBUG = True
# ENV = "prod"
# APP_ENV = os.environ.get("APP_ENV", 'local')

dotenv.load_dotenv(os.getcwd() + '/.env')


BASIC_AUTH_USERNAME = os.getenv("BASIC_AUTH_USERNAME")
BASIC_AUTH_PASSWORD = os.getenv("BASIC_AUTH_PASSWORD")

MONGO_PASSCODE=os.getenv("MONGO_PASSCODE")
MONGO_HOST=os.getenv("MONGO_HOST")

MYSQL_UNDERWRITING_HOST = os.getenv("MYSQL_UNDERWRITING_HOST")
MYSQL_UNDERWRITING_USER = os.getenv("MYSQL_UNDERWRITING_USER")
MYSQL_UNDERWRITING_PASSWORD =os.getenv("MYSQL_UNDERWRITING_PASSWORD")
MYSQL_UNDERWRITING_PASSWORD_READ_ONLY=os.getenv("MYSQL_UNDERWRITING_PASSWORD_READ_ONLY")
MYSQL_UNDERWRITING_DB = os.getenv("MYSQL_UNDERWRITING_DB")
MYSQL_UNDERWRITING_USER_READ_ONLY  = os.getenv("MYSQL_UNDERWRITING_USER_READ_ONLY")

POSTGRES_UNDERWRITING_HOST_READ = os.getenv("POSTGRES_UNDERWRITING_HOST_READ")
POSTGRES_UNDERWRITING_USER_READ  = os.getenv("POSTGRES_UNDERWRITING_USER_READ")
POSTGRES_UNDERWRITING_PASSWORD_READ  =os.getenv("POSTGRES_UNDERWRITING_PASSWORD_READ")
POSTGRES_UNDERWRITING_DB_READ  = os.getenv("POSTGRES_UNDERWRITING_DB_READ")

# if APP_ENV == "prod":
#     dotenv.load_dotenv(os.getcwd() + '/.env')

#     GST_BUCKET_NAME = os.getenv("GST_BUCKET_NAME")
#     BASIC_AUTH_USERNAME = os.getenv("BASIC_AUTH_USERNAME")
#     BASIC_AUTH_PASSWORD = os.getenv("BASIC_AUTH_PASSWORD")
    
#     # from .settings_production import *
# else:
#     try:
#         from .settings_local import *
#     except ImportError:
#         logging.error("No local settings detected. add settings/setting_local.py with local configuration setting")
#         sys.exit()