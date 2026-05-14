import functools
import json
import os

from config import set_reports
def save_reports(file_name = None):
    """Функция декоратора для сохранения в файл"""
    def wrapper(func):
        functools.wraps(func)
        def inner(*args, **kwargs):
            result = func(*args, **kwargs)
            if file_name is None:
                actual_file_name = func.__name__
            else:
                actual_file_name = os.path.splitext(file_name)[0]
            full_path = set_reports(actual_file_name)
            with open(set_reports(full_path), "a", encoding="utf-8") as file:
                file.write(result)
            return result
        return inner
    return wrapper
