import os
from database.connector import OracleConnector
from database.queries import Queries
from database.tables.operator import TablesOperator


class TablesFactory:
  
  ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
  SCRIPTS_DIR = os.path.join(ROOT_DIR ,"scripts")
  CREATE_OP_DIR = os.path.join(SCRIPTS_DIR, "02-school-operational-db.sql")
  DROP_OP_DIR = os.path.join(SCRIPTS_DIR, "03-school-operation-drop.sql")
  INSERT_OP_DIR = os.path.join(SCRIPTS_DIR, "04-school-dump-db.sql")
  
  def __init__(self, operation:str) -> None:
      self.__database_connector = self.__get_database_connector()
      if operation == "create-operational":
        TablesOperator(connection=self.__database_connector,
                     queries=self.__get_sql_queries(self.CREATE_OP_DIR)).execute
      elif operation == "delete-operational":
        TablesOperator(connection=self.__database_connector,
                     queries=self.__get_sql_queries(self.DROP_OP_DIR)).execute
      elif operation == "insert-operational":
        TablesOperator(connection=self.__database_connector,
                     queries=self.__get_sql_queries(self.INSERT_OP_DIR)).execute
        
  @staticmethod
  def __get_database_connector():
    return OracleConnector().get
  
  @staticmethod
  def __get_sql_queries(file_path):
    return Queries(file_path=file_path).get