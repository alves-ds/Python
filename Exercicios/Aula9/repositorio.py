class Repositorio:

    def select(self, db_connection: any) -> None:
        conection = db_connection.conectar()
        print('Conectei ao banco de dados {}'.format(conection))
        print('Fazendo um SELECT * FROM...')
        db_connection.desconectar()

    def insert(self, db_connection: any) -> None:
        conection = db_connection.conectar()
        print('Conectei ao banco de dados {}'.format(conection))
        print('Fazendo um Insert values...')
        db_connection.desconectar()