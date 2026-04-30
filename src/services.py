import requests
import yfinance as yf
from utils import reader_json



def currency_rates():
    """Получает курс валюты к рублю через API ЦБ РФ."""
    config = reader_json()
    currency_code =config.get('user_currencies')
    url = "https://www.cbr-xml-daily.ru/daily_json.js"
    result = []
    for currency in currency_code:
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            if currency.upper() in data['Valute']:
                valute_data = data['Valute'][currency.upper()]
                new_dict = {
                    "currency": valute_data['CharCode'],
                    "rate" : valute_data['Value'],
                }
                result.append(new_dict)
            else:
                return {"error": f"Валюта {currency_code} не найдена"}

        except Exception as e:
            return {"error": str(e)}
    return result

def stock_prices():
    """
    Получает данные по акциям.
    Возвращает список словарей
    """
    config = reader_json()
    tickers_list = config.get('user_stocks')
    stock_list = []
    for ticker in tickers_list:
        try:
            stock = yf.Ticker(ticker)
            info = stock.info
            stock_data = {
                "ticker": ticker,
                "price": info.get('previousClose')
            }
            stock_list.append(stock_data)
        except Exception as e:
            print(f"Не удалось получить данные для {ticker}: {e}")
            continue
    return stock_list

if __name__ == '__main__':
    # Тест
    print(currency_rates())
