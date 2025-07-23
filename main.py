from modules.mysql_connection import MySQLConnector
config = {
    'host': 'localhost',
    'user': 'shinleonhardt',
    'password': '12345678',
    'database': 'theo_doi_son_thang_5',
    'auth_plugin':'mysql_native_password'
}

conn = MySQLConnector.create_connection(config['host'], 
                                        config['user'], 
                                        config['password'], 
                                        config['database'],
                                        config['auth_plugin'])


