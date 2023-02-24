import mysql.connector
import os

from mysql.connector import MySQLConnection, CMySQLConnection
from mysql.connector.cursor import MySQLCursor
from mysql.connector.cursor_cext import CMySQLCursor
from mysql.connector.pooling import PooledMySQLConnection


class MysqlService:
    def __init__(self) -> None:
        self.db = MysqlService.connection()
        # self.create_table()

    @staticmethod
    def connection() -> PooledMySQLConnection | MySQLConnection | CMySQLConnection:
        return mysql.connector.connect(
            host=os.environ.get('MYSQL_HOST'),
            user=os.environ.get('MYSQL_USER'),
            password=os.environ.get('MYSQL_PASS'),
            database=os.environ.get('MYSQL_DBNAME')
        )

    def get_cursor(self) -> MySQLCursor | CMySQLCursor:
        return self.db.cursor(dictionary=True)

    def get_tb_results(self) -> str:
        return os.environ.get('MYSQL_TB_RESULTS')

    def create_table(self) -> None:
        try:
            self.get_cursor().execute("""CREATE TABLE IF NOT EXISTS {}(
                          id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
                          concurso INT NOT NULL,
                          data_do_sorteio VARCHAR(255) NOT NULL,
                          coluna1 INT NOT NULL,
                          coluna2 INT NOT NULL,
                          coluna3 INT NOT NULL,
                          coluna4 INT NOT NULL,
                          coluna5 INT NOT NULL,
                          coluna6 INT NOT NULL,
                          ganhadores_faixa_1 INT,
                          ganhadores_faixa_2 INT,
                          ganhadores_faixa_3 INT,
                          rateio_faixa_1 FLOAT,
                          rateio_faixa_2 FLOAT,
                          rateio_faixa_3 FLOAT,
                          cidade VARCHAR(255),
                          valor_arrecadado FLOAT,
                          estimativa_para_o_proximo_concurso FLOAT,
                          valor_acumulado_proximo_concurso FLOAT,
                          acumulado FLOAT,
                          sorteio_especial VARCHAR(255),
                          observacao VARCHAR(255)
                  )""".format(self.get_tb_results()))
        except mysql.connector.Error as err:
            print("Failed creating table: {}".format(err))
            exit(1)

    def find_all(self, cursor: MySQLCursor | CMySQLCursor):
        query = "SELECT * FROM `{}`".format(self.get_tb_results())
        try:
            cursor.execute(query)
            results = cursor.fetchall()
        except mysql.connector.Error as err:
            print("Failed get all results: {}".format(err))
            exit(1)
        cursor.close()
        self.db.close()
        return results

    def create_database(self):
        try:
            self.get_cursor().execute(
                "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8' DEFAULT COLLATE 'utf8_general_ci'".format(
                    os.environ.get('DB_NAME')))
        except mysql.connector.Error as err:
            print("Failed creating database: {}".format(err))
            exit(1)

    def insert_many(self) -> None:
        pass

    def insert_one(self, mega_sena) -> None:
        query = """INSERT INTO {}(concurso, data_do_sorteio, coluna1, coluna2, coluna3, coluna4, coluna5, coluna6, 
                                    ganhadores_faixa_1, ganhadores_faixa_2, ganhadores_faixa_3, rateio_faixa_1, 
                                    rateio_faixa_2, rateio_faixa_3, cidade, valor_arrecadado, estimativa_para_o_proximo_concurso, 
                                    valor_acumulado_proximo_concurso, acumulado, sorteio_especial, observacao)values(
                                    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""".format(
            self.get_tb_results())
        try:
            self.get_cursor().execute(query, mega_sena)
            self.db.commit()
        except mysql.connector.Error as err:
            print("Failed insert: {}".format(err))
            exit(1)
