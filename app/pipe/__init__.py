from time import time
from database.tables.ddl import DDLFactory


class DataPipeline:
  
  @staticmethod
  def __oltp():
    start_time = time()
    DDLFactory(operation="delete-operational")
    DDLFactory(operation="create-operational")
    DDLFactory(operation="insert-operational")
    execution_time = (time() - start_time)
    return execution_time
    
  @staticmethod
  def __olap():
    start_time = time()
    DDLFactory(operation="delete-dw")
    DDLFactory(operation="create-dw")
    execution_time = (time() - start_time)
    return execution_time
          
  @property
  def execute(self):
    oltp = self.__oltp()
    olap = self.__olap()
    
    return f"Process Time: " \
          f"\nOLTP Process:{oltp}" \
          f"\nOLAP Process:{olap}" \
          f"\nTotal:{oltp + olap}"