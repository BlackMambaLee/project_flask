import os
from configparser import ConfigParser
from modules.db_module.postgresql import *

class db_conn:
    pwd = os.path.dirname(os.path.abspath(__file__))
    initFile = os.path.join(pwd, 'database.ini')

    config = ConfigParser()
    config.read(initFile)
    
    dbname   = config.get('database', 'databaseName')
    user     = config.get('database', 'user')
    host     = config.get('database', 'host')
    password = config.get('database', 'password')
    port     = config.get('database', 'port')

    def __init__(self):
        self.connects(db_conn.dbname, db_conn.user, db_conn.host, db_conn.password, db_conn.port)

    def connects(self, dbname, user, host, password, port):
        Postgresql(dbname=dbname, user=user, host=host, password=password, port=port)

    # def create_connect(self):
    #     config = configparser.ConfigParser()
    #     config.read('./database.ini')
    #     self.cursor  = self.conn.cursor()
    #     self.connect = psycopg2.connect(  dbname   = config.GET('database', 'databaseName')
    #                                     , user     = config.GET('user', 'user')
    #                                     , host     = config.GET('host', 'host')
    #                                     , password = config.GET('password', 'password')
    #                                     , port     = config.GET('port', 'port'))

    def excute(self, query, args={}):
        # self.cursor.excuse(query)
        # self.cursor.close()
        self.connects().cursor().excuse(query)
