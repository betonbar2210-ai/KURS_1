import numpy as np

from src.services import filter_date_services, filter_nan_services
from pandas import Timestamp

def test_filter_date_services(testing_pd):
    assert filter_date_services(testing_pd, 2020, 11).to_dict() ==  {
        'Дата операции': {1: Timestamp('2020-11-05 09:15:00')},
        'Категория': {1: 'Кафе'},
        'Описание': {1: 'Шоколадница'},
        'Сумма операции с округлением': {1: 200},
        'Кэшбэк': {1: 20.0}}



def test_filter_nan_services(testing_pd):
    assert filter_nan_services(testing_pd).to_dict() == {
        'Дата операции': {1: '05.11.2020 09:15:00'},
        'Категория': {1: 'Кафе'},
        'Описание': {1: 'Шоколадница'},
        'Сумма операции с округлением': {1: 200},
        'Кэшбэк': {1: 20.0}}



