from database.tables import TablesFactory


if __name__ == '__main__':
  
  TablesFactory(operation="delete-operational")
  TablesFactory(operation="create-operational")
  TablesFactory(operation="insert-operational")