import pandas as pd
import json
import requests
import yfinance as yf


def reader_json(way):
    """Читаем файл JSON и возвращает словарь с настройками."""
    with open(way, 'r', encoding='utf-8') as x:
        setting = json.load(x)
    return setting


def reader_excel(way):
    """Функция чтения EXCEL файла с помощью pandas"""
    data_excel = pd.read_excel(way)
    return data_excel


def currency_rates(setting):
    """Получает курс валюты к рублю через API ЦБ РФ."""
    currency_code = setting['user_currencies']
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
            return {"error": f"{e}"}
    return result


def stock_prices(setting):
    """
    Получает данные по акциям.
    Возвращает список словарей
    """
    tickers_list: list[str] = setting.get('user_stocks')
    stock_list = []
    for ticker in tickers_list:
        try:
            stock = yf.Ticker(ticker)
            info = stock.info
            stock_data = {
                "stock": ticker,
                "price":info.get("previousClose")}
            stock_list.append(stock_data)
        except Exception as e:
            print(f"Не удалось получить данные для {ticker}: {e}")
            continue
    return stock_list
