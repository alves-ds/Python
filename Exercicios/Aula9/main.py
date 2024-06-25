from repositorio import Repositorio
from databases import PostgresDB, MysqlDB

db_conn_post = PostgresDB()
db_conn_mysql = MysqlDB()
repo = Repositorio()

repo.insert(db_conn_post)
print()
repo.insert(db_conn_mysql)