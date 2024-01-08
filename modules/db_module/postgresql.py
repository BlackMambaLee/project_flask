import psycopg2, os, json
from psycopg2.extras import RealDictCursor
from configparser import ConfigParser

class Postgresql:
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
        self.conn = psycopg2.connect(dbname=Postgresql.dbname, user=Postgresql.user, host=Postgresql.host, password=Postgresql.password, port=Postgresql.port)
        # self.cursor  = self.conn.cursor()

    # def reConnect():
    #     conn = psycopg2.connect(dbname=Postgresql.dbname, user=Postgresql.user, host=Postgresql.host, password=Postgresql.password, port=Postgresql.port)

    def executeSelect(self, query, args={}):
        try:
            self.cursor = self.conn.cursor(cursor_factory=RealDictCursor)
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            self.cursor.close()
            
            return result
        
        except Exception as e:
            self.cursor.close()
            
            return json.dumps({"error": str(e)})
    
    def executeInsert(self,query, args={}):
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute(query, args)
            self.conn.commit()

            return json.dumps({"message": "success"})
        
        except Exception as e:
            self.cursor.close()
            
            return json.dumps({"error": str(e)})
