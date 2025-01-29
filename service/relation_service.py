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
            self.cursor.execute(
                f"""SELECT  `IDRelation`, `IDHardware1`, `IDHardware2` FROM `relation_hardware` 
                WHERE `IDHardware1` = {id_hardware} OR `IDHardware2` = {id_hardware}""")
            data = self.cursor.fetchall()
            print("data : ", data)
            liste_relation = []
            for element in data:
                if element[1] == id_hardware:
                    relation = {'id_relation': element[0], 'id_hardware1': element[1], 'id_hardware2': element[2]}
                else:
                    relation = {'id_relation': element[0], 'id_hardware1': element[2], 'id_hardware2': element[1]}
                liste_relation.append(relation)
            self.cursor.close()
            self.connection.close()
            return 'success', liste_relation
        except Exception as e:
            return 'error', e
