import os
from functools import wraps

# def writer(file_name):
#     file_name = os.path.abspath('../data/result.txt')
#     def wrapper(func):
#         @wraps(func)
#         def inner(*args, **kwargs):
#             result = func(*args, **kwargs)
#             with open(file_name, 'a', encoding='utf-8') as x:
#                 x.write(result)
#             return result
#         return inner
#     return wrapper

