from datetime import datetime
from unittest.mock import Mock, patch

from src.views import greeting, filter_pay


@patch("src.views.datetime")
def test_greeting(mock_time):
    mock_time.now.return_value = datetime(1, 1,1,10, 50)
    assert greeting() == 'Доброе утро'
    mock_time.now.return_value = datetime(1, 1, 1, 13, 50)
    assert greeting() == "Добрый день"
    mock_time.now.return_value = datetime(1, 1, 1, 22, 50)
    assert greeting() == "Добрый вечер"
    mock_time.now.return_value = datetime(1, 1, 1, 23, 50)
    assert greeting() == "Доброй ночи"


def test_filter_pay(test_read_ex):
    with patch("src.utils.reader_excel", return_value = test_read_ex):
        assert filter_pay().to_dict() == {
            "Дата операции": ["2024-10-01"],
            "Сумма операции": [-100],
            "Категория": ["Супермаркеты"],
            "Описание": ["Магнит"],
            "Номер карты": ["*5091"]
        }


