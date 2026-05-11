import pytest
import pandas as pd

@pytest.fixture
def test_read_ex():
    return pd.DataFrame(
        {
            "Дата платежа": [
                "2024-10-01",
                "2024-10-02"
            ],
            "Сумма операции": [-100, 200],
            "Категория": [
                "Супермаркеты",
                "Кафе"
            ],
            "Описание": [
                "Магнит",
                "Пятерочка"
            ],
            "Номер карты": ["*5091", "*1111"],
            "Сумма операции с округлением": [100, 200],
        }
    )

@pytest.fixture
def utils_json():
    return {'user_currencies': ['USD', 'EUR'], 'user_stocks': ['AAPL']}

@pytest.fixture
def test_api_ok():
    return {
        "Valute": {
            "USD": {
                "CharCode": "USD",
                "Value": 92.50,
            },
            "EUR": {
                "CharCode": "EUR",
                "Value": 100.20,
            }
        }
    }

@pytest.fixture
def test_api_no():
    return {
        "Valute": {
            "CLL": {
                "CharCode": "CLL",
                "Value": 92.50,
        }}}


@pytest.fixture
def test_stocs():
    return {
                "stock": "AAPL",
                "price": 20
            }

@pytest.fixture
def group_dict():
    return {'*1112': 46207.08, '*4556': 1768837.24}


@pytest.fixture
def sort_dict():
    df = pd.DataFrame({
        'Дата платежа': ['2024-10-01'],
        'Категория': ['Супермаркеты'],
        'Описание': ['Магнит'],
        'Сумма операции с округлением': [100]
    })
    return df