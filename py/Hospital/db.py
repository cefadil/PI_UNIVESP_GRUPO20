import mysql.connector as mysql_conn

class DB:
    host="localhost"
    user="user"
    password="password"
    database="db"
    def __init__(self):
        self.conn = self.connect()
    
    def connect(self):
        return mysql_conn.connect(
        host=self.host,
        user=self.user,
        password=self.password,
        database=self.database
        )