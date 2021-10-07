import os
from os.path import join, dirname, abspath
import dotenv


class Settings:
  
  dotenv.load_dotenv(dotenv.find_dotenv())
  
  ORACLE_USER = os.getenv('ORACLE_USER')
  ORACLE_PASS = os.getenv('ORACLE_PASS')
  ORACLE_HOST = os.getenv('ORACLE_HOST')
  ORACLE_PORT = os.getenv('ORACLE_PORT')
  ORACLE_SERVICE_NAME = os.getenv('ORACLE_SERVICE_NAME')
  
