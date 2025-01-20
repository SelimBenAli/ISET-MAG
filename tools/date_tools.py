class DateTools:
    def __init__(self):
        pass

    @staticmethod
    def convert_date(date):
        if date is None:
            return None
        return date.strftime("%Y-%m-%d")

    @staticmethod
    def convert_date_time(date):
        if date is None:
            return None
        return date.strftime("%Y-%m-%d %H:%M:%S")
