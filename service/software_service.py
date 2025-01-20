from tools.database_tools import DatabaseConnection


class SoftwareService:
    def __init__(self):
        self.cursor = None
        self.connection = None
        self.database_tools = DatabaseConnection()

    # TO CONTINUE
