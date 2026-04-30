import requests
import yfinance as yf
from datetime import datetime


def currency_rates(currency_code):
    """Получает курс валюты к рублю через API ЦБ РФ."""
    url = "https://www.cbr-xml-daily.ru/daily_json.js"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if currency_code.upper() in data['Valute']:
            valute_data = data['Valute'][currency_code.upper()]
            return {
                "CharCode": valute_data['CharCode'],
                "Value": valute_data['Value'],
            }
        else:
            return {"error": f"Валюта {currency_code} не найдена"}

    except Exception as e:
        return {"error": str(e)}


# def stock_prices(tickers_list):
#     """
#     Получает данные по акциям.
#     Возвращает словарь, совместимый с JSON (даты преобразованы в строки).
#     """
#     all_data = {}
#
#     try:
#         # Скачиваем данные. group_by='ticker' упрощает доступ
#         hist_data = yf.download(tickers_list, period="1d", group_by='ticker', auto_adjust=True)
#     except Exception as e:
#         print(f"Ошибка при скачивании исторических данных: {e}")
#         return None
#
#     for ticker_name in tickers_list:
#         try:
#             ticker = yf.Ticker(ticker_name)
#             info = ticker.info
#
#             current_price = "Нет данных"
#             date_str = "Нет данных"
#
#             if not hist_data.empty:
#                 # Обработка случая с одним тикером и несколькими
#                 if len(tickers_list) > 1:
#                     if ticker_name in hist_data.columns.levels[0]:
#                         price_series = hist_data[ticker_name]['Close']
#                         if not price_series.empty:
#                             current_price = float(price_series.iloc[-1])
#                             # !!! ГЛАВНОЕ ИСПРАВЛЕНИЕ: Преобразуем индекс (дату) в строку !!!
#                             date_obj = price_series.index[-1]
#                             date_str = date_obj.strftime('%Y-%m-%d')
#                 else:
#                     # Если тикер один
#                     if not hist_data['Close'].empty:
#                         current_price = float(hist_data['Close'].iloc[-1])
#                         date_obj = hist_data.index[-1]
#                         date_str = date_obj.strftime('%Y-%m-%d')
#
#             all_data[ticker_name] = {
#                 'stock': all_data[ticker_name],
#                 'price': current_price
#             }
#
#         except Exception as e:
#             print(f"Не удалось получить данные для {ticker_name}: {e}")
#             all_data[ticker_name] = {'error': str(e)}
#
#     return all_data


if __name__ == '__main__':
    # Тест
    print(stock_prices(['AAPL', 'MSFT']))
