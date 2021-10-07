class TablesOperator:
  
  def __init__(self, connection, queries) -> None:
    self.__conn = connection
    self.__queries = queries
  
  @property
  def execute(self):
    try:
      cursor = self.__conn.cursor()

      for command in self.__queries:
        cursor.execute(command)

      self.__conn.commit()
    except Exception as exception:
      return f"Error: {exception}"