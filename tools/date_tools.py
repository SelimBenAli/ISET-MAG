class DateTools:
    def __init__(self):
        pass

    @staticmethod
    def convert_date(date):
        try:
            if date is None or date == "" or date == '0000-00-00 00:00:00':
                return None
            return date.strftime("%Y-%m-%d")
        except Exception as e:
            return e, date

    @staticmethod
    def convert_date_time(date):

        try:
            if date is None or date == "" or date == '0000-00-00 00:00:00':
                return None
            return date.strftime("%Y-%m-%d %H:%M:%S")
        except Exception as e:
            return e, date


if __name__ == '__main__':
    pass
