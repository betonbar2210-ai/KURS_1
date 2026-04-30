import os
import pandas as pd
import json


def reader_json(way = '../user_settings.json'):
    """Читаем файл JSON и возвращает словарь с настройками."""
    with open(way,'r', encoding='utf-8') as x:
        setting = json.load(x)
    return setting


def reader_excel():
    """Функция чтения EXCEL файла с помощью pandas"""
    way_excel = os.path.abspath("../data/operations.xlsx")
    data_excel = pd.read_excel(way_excel)
    return data_excel

if __name__ == '__main__':
    print(reader_json())