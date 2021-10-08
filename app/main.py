from database.tables.ddl import DDLFactory


if __name__ == '__main__':
  
  DDLFactory(operation="delete-operational")
  DDLFactory(operation="create-operational")
  DDLFactory(operation="insert-operational")
  DDLFactory(operation="delete-dw")
  DDLFactory(operation="create-dw")
