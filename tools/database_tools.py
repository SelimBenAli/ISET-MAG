import pymysql


class DatabaseConnection:
    def __init__(self):
        self.pwd = ""
        self.db = "iset_mag_db"
        self.user = "root"
        self.port = 3306
        self.host = "localhost"

    def find_connection(self):
        conn = pymysql.connect(host=self.host,
                               port=self.port,
                               user=self.user,
                               password=self.pwd,
                               database=self.db)
        return conn, conn.cursor()

    def execute_request(self, request):
        try:
            connection, cursor = self.find_connection()
            cursor.execute(request)
            connection.commit()
            cursor.close()
            connection.close()
            return 'success'
        except Exception as e:
            return 'error', e
