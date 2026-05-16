from datetime import datetime
from unittest.mock import Mock, patch

from src.views import greeting, filter_pay, group_number_card, new_filter_pay_list, sort_pay, new_sort_pay_list


def test_greeting():
    assert greeting(datetime(1, 1,1,10, 50)) == 'Доброе утро'
    assert greeting(datetime(1, 1, 1, 13, 50)) == "Добрый день"
    assert greeting(datetime(1, 1, 1, 22, 50)) == "Добрый вечер"
    assert greeting(datetime(1, 1, 1, 23, 50)) == "Доброй ночи"


def test_filter_pay(test_read_ex):
    with patch("src.utils.reader_excel", return_value = test_read_ex):
        assert filter_pay(test_read_ex).to_dict() == {
            "Дата платежа": {0: "2024-10-01"},
            "Сумма операции": {0: -100},
            "Категория": {0: "Супермаркеты"},
            "Описание": {0: "Магнит"},
            "Номер карты": {0: "*5091"},
            "Сумма операции с округлением": {0: 100},
        }


def test_group_number_card(test_read_ex):
        assert group_number_card(test_read_ex).to_dict() == {'*1111': 200, '*5091': 100}


def test_new_filter_pay_list(group_dict):
    assert new_filter_pay_list(group_dict) == [
        {"last_digits": "1112",
        "total_spent": 46207.08,
        "cashback": 462.07
        },
        {"last_digits": "4556",
        "total_spent": 1768837.24,
        "cashback": 17688.37}
        ]


def test_new_filter_pay_list_value_error():
    """Тест блок except при передаче невалидной строки (ValueError)"""
    # Имитируем ситуацию, когда сумма операции - это текст
    invalid_data = {"12345814": "Не число"}

    result = new_filter_pay_list(invalid_data)

    # Ожидаем, что функция не упадет, а заменит значение на 0.0
    expected = [{
        "last_digits": "5814",
        "total_spent": 0.0,
        "cashback": 0.0
    }]

    assert result == expected


def test_new_filter_pay_list_type_error():
    """Тест блок except при передаче None (TypeError)"""
    invalid_data = {"99887766": None}
    assert new_filter_pay_list(invalid_data) == [{
        "last_digits": "7766",
        "total_spent": 0.0,
        "cashback": 0.0
    }]


def test_new_filter_pay_list_mixed():
    """Тест смешанных данных: валидные данные + невалидные"""
    mixed_data = {
        "11112222": 500.0,
        "33334444": "Ошибка",
        "55556666": None
    }
    assert new_filter_pay_list(mixed_data) == [
        {"last_digits": "2222", "total_spent": 500.0, "cashback": 5.0},
        {"last_digits": "4444", "total_spent": 0.0, "cashback": 0.0},
        {"last_digits": "6666", "total_spent": 0.0, "cashback": 0.0}
    ]

def test_sort_pay(test_read_ex):
    assert sort_pay(test_read_ex).to_dict() == {"Дата платежа": {0: "2024-10-01", 1: "2024-10-02"},
                                                "Категория": {0: "Супермаркеты", 1: "Кафе"},
                                                "Описание": {0: "Магнит", 1: "Пятерочка"},
                                                "Сумма операции с округлением": {0: 100, 1: 200},}


def test_new_sort_pay_list(sort_dict):
    assert new_sort_pay_list(sort_dict) == [{
            "date": "2024-10-01",
            "amount": 100,
            "category": "Супермаркеты",
            "description": "Магнит"
        }]