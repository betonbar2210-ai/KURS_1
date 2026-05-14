import functools
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
                if isinstance(result, list):
                    file.write('\n'.join(map(str, result)))
                else:
                    file.write(str(result))
            return result
        return inner
    return wrapper
