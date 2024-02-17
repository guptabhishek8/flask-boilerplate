import logging
import json
import requests
import boto3

from ..constants import common_constants, sql_db_constants
from datetime import datetime
import factory as fc 
from ..helpers.sql_utils import DatabaseClass

# logging setup
logger = logging.getLogger("flask_app")
#s3 connection
s3 = boto3.client('s3')


TABLES = sql_db_constants.TABLES
HTTPCODES = common_constants.HTTPCODES

# def first_app(input):

#     # Input your Logic here 
#     logger.info(f"First Logic")
#     response = s3.get_object(Bucket=bucket_name, Key=path)
#     return returnData