from tools.database_tools import DatabaseConnection
from tools.date_tools import DateTools


class RelationService:
    def __init__(self):
        self.cursor = None
        self.connection = None
        self.database_tools = DatabaseConnection()
        self.date_tools = DateTools()

    def find_relation_by_hardware(self, id_hardware):
        try:
            self.connection, self.cursor = self.database_tools.find_connection()
            req = (f"""
SELECT 
    CASE 
        WHEN rh1.IDHardware1 = {id_hardware} THEN rh1.IDHardware2
        WHEN rh1.IDHardware2 = {id_hardware} THEN rh1.IDHardware1
        END AS LinkedHardwareID
FROM 
    relation_hardware rh1
WHERE 
    {id_hardware} IN (rh1.IDHardware1, rh1.IDHardware2)
UNION
SELECT 
    CASE 
        WHEN rh2.IDHardware1 = LinkedHardwareID THEN rh2.IDHardware2
        WHEN rh2.IDHardware2 = LinkedHardwareID THEN rh2.IDHardware1
        END AS LinkedHardwareID
FROM 
    relation_hardware rh2,
    (
        SELECT 
            CASE 
                WHEN rh1.IDHardware1 = {id_hardware} THEN rh1.IDHardware2
                WHEN rh1.IDHardware2 = {id_hardware} THEN rh1.IDHardware1
                END AS LinkedHardwareID
        FROM 
            relation_hardware rh1
        WHERE 
            {id_hardware} IN (rh1.IDHardware1, rh1.IDHardware2)
    ) AS subquery
WHERE 
    LinkedHardwareID IN (rh2.IDHardware1, rh2.IDHardware2);
            """)
            self.cursor.execute(req)
            data = self.cursor.fetchall()
            liste_relation = []
            for element in data:
                if element[0] != id_hardware:
                    liste_relation.append(element[0])
            self.cursor.close()
            self.connection.close()
            return 'success', liste_relation
        except Exception as e:
            return 'error', e

    def add_relation(self, id_hardware1, id_hardware2):
        try:
            self.connection, self.cursor = self.database_tools.find_connection()
            self.cursor.execute(
                f"INSERT INTO relation_hardware (IDHardware1, IDHardware2) VALUES ({id_hardware1}, {id_hardware2})")
            self.connection.commit()
            self.cursor.close()
            self.connection.close()
            return 'success'
        except Exception as e:
            return 'error', e

    def delete_relation(self, id_hardware1, id_hardware2):
        try:
            self.connection, self.cursor = self.database_tools.find_connection()
            self.cursor.execute(
                f"DELETE FROM relation_hardware WHERE (IDHardware1 = {id_hardware1} AND IDHardware2 = {id_hardware2}) OR (IDHardware1 = {id_hardware2} AND IDHardware2 = {id_hardware1})")
            self.connection.commit()
            self.cursor.close()
            self.connection.close()
            return 'success'
        except Exception as e:
            return 'error', e


if __name__ == '__main__':
    relation_service = RelationService()
