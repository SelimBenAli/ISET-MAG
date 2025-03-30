import pymysql


class DatabaseConnection:
    def __init__(self):
        self.pwd = "isetnmagdb"
        self.db = "isetn2025tracker$default"
        self.user = "isetn2025tracker"
        self.port = 3306
        self.host = "isetn2025tracker.mysql.pythonanywhere-services.com"

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

if __name__ == '__main__':
    database_tools = DatabaseConnection()
    print(database_tools.execute_request("SELECT * FROM admin"))