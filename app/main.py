from core.config import settings
from cx_Oracle import connect, makedsn, init_oracle_client

if __name__ == '__main__':
  init_oracle_client(lib_dir=r"C:\oracle\instantclient_19_12")
  
  dsn_tns = makedsn(settings.ORACLE_HOST, 
                    settings.ORACLE_PORT, 
                    service_name=settings.ORACLE_SERVICE_NAME)
  conn = connect(user=settings.ORACLE_USER, 
                 password=settings.ORACLE_PASS,
                 dsn=dsn_tns)
  
  cursor = conn.cursor()

  #Rodando uma Query para teste
  cursor.execute("select * from global_name")
  result = cursor.fetchall()
  for row in result:
      print(result)
  
  print("Database version:", conn.version)
  print()
  print(settings.ORACLE_USER)
  print(settings.ORACLE_PASS)
  print(settings.ORACLE_HOST)
  print(settings.ORACLE_PORT)
  print(settings.ORACLE_SERVICE_NAME)