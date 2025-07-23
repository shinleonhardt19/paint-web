import mysql.connector
from mysql.connector import Error

class MySQLConnector:
    def __init__(self,host,user,password,database):
        self.host = host
        self.user = user 
        self.password = password
        self.database = database
        self.auth_plugin = 'mysql_native_password'
        self.connection = None

    def create_connection(self, table_query):
        try:
            print("Connecting to MySQL...")
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
                auth_plugin=self.auth_plugin
            )
            cursor = self.connection.cursor()
            cursor.execute(table_query)
            self.connection.commit()
            print("Successfully created!")
        except Error as e:
            print(f"Error: {e}")
        finally:
            if self.connection is not None and self.connection.is_connected():
                cursor.close()
                self.connection.close()
                print("Close connection")   

