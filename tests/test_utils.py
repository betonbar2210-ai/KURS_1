from unittest.mock import Mock, patch, mock_open, MagicMock

from src.utils import reader_json, reader_excel, currency_rates, stock_prices


def test_reader_json(utils_json):
    def fake(df):
        return utils_json

    with patch("builtins.open", mock_open()):
        with patch("src.utils.json.load", side_effect = fake):
            assert reader_json() == utils_json

def test_reader_excel(test_read_ex):
        with patch("src.utils.pd.read_excel", return_value = test_read_ex):
            assert reader_excel().to_dict() == test_read_ex.to_dict()


def test_currency_rates_ok(utils_json, test_api_ok):
    mock_response = Mock()
    mock_response.json.return_value = test_api_ok
    with patch("builtins.open", mock_open()):
        with patch("src.utils.json.load", return_value = utils_json):
            with patch("src.utils.requests.get", return_value=mock_response):
                assert currency_rates() == [
                    {"currency": "USD",
                    "rate" : 92.50},
                    {"currency": "EUR",
                    "rate" : 100.20}
                ]

def test_currency_rates_no(utils_json, test_api_no):
    mock_response = MagicMock()
    mock_response.json.return_value = test_api_no
    with patch("builtins.open", mock_open()):
        with patch("src.utils.json.load", return_value=utils_json):
            with patch("src.utils.requests.get", return_value=mock_response):
                assert currency_rates() == {'error': "Валюта ['USD', 'EUR'] не найдена"}


def test_stock_prices(utils_json, test_stocs):
    mock_response = MagicMock()
    mock_response.info = {

        'previousClose': 20
    }
    with patch("builtins.open", mock_open()):
        with patch("src.utils.json.load", return_value=utils_json):
            with patch("src.utils.yf.Ticker", return_value=mock_response):
                assert stock_prices() == [test_stocs]

