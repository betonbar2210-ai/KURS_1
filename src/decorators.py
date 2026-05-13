import functools
import json

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
                actual_file_name = file_name
            full_path = set_reports(actual_file_name)
            if isinstance(result, dict):
                text_to_write = json.dumps(result, ensure_ascii=False, indent=4)
            else:
                text_to_write = str(result)
            with open(set_reports(full_path), "a", encoding="utf-8") as file:
                file.write(text_to_write + "\n\n")
            return result
        return inner
    return wrapper
