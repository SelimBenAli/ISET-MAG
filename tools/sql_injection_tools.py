import re
from datetime import datetime, timedelta
from flask import session


class SQLInjectionTools:
    def __init__(self):
        pass

    @staticmethod
    def string_contains_sql_injection(input_string):
        sql_patterns = [
            r"(\%27)|(\')|(\-\-)|(\%23)|(#)",
            r"\b(select|update|delete|insert|exec|drop|union|create|alter)\b",
            r"(\%22)|(\")|(\%3D)|(=)",
            r"\b(or|and)\b",
            r"\b(union|select|from|where)\b",
            r"(\*|;)",
            r"(\b(0x[0-9a-fA-F]+)\b)",
        ]

        for pattern in sql_patterns:
            if re.search(pattern, input_string, re.IGNORECASE):
                return True
        return False

    def detect_sql_injection(self, my_list):
        for value in my_list:
            try:
                value = str(value)
            except Exception as e:
                return False
            print(value)
            if value != "" and self.string_contains_sql_injection(value):
                return True
        return False

    @staticmethod
    def string_contains_sql_injection_in_descriptions(input_string):
        sql_patterns = [
            r"(\%27)|(\-\-)|(\%23)|(#)",
            r"\b(select|update|delete|insert|exec|drop|union|create|alter)\b",
            r"(\%22)|(\")|(\%3D)|(=)",
            r"\b(union|select|from|where)\b",
            r"(\*|;)",
            r"(\b(0x[0-9a-fA-F]+)\b)",
        ]

        for pattern in sql_patterns:
            if re.search(pattern, input_string, re.IGNORECASE):
                return True
        return False

    def detect_sql_injection_in_descriptions(self, my_list):
        for value in my_list:
            print(value)
            if value != "" and self.string_contains_sql_injection_in_descriptions(value):
                return True
        return False

    @staticmethod
    def sql_injection_detected_actions():
        session['sql_injections'] += 1
        if session['sql_injections'] >= 3:
            session['blocked'] = True
            session['blocked_reason'] = 'SQL Injection detected'
            session['block_start'] = datetime.now()
            session['block_end'] = datetime.now() + timedelta(minutes=int(session['sql_injections']) * 1)
