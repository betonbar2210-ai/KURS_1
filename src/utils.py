import pandas as pd
import json
import requests
import yfinance as yf

from config import modul_log

logger_utils = modul_log("utils")


def reader_json(way):
    """Читаем файл JSON и возвращает словарь с настройками."""
    try:
        with open(way, "r", encoding="utf-8") as x:
            setting = json.load(x)
        logger_utils.info("Получили и открыли json файл")
        return setting
    except Exception as e:
        logger_utils.error(f"Ошибка {e}")
        return f"Ошибка {e}"


def reader_excel(way):
    """Функция чтения EXCEL файла с помощью pandas"""
    try:
        data_excel = pd.read_excel(way)
        logger_utils.info("Прочитали EXCEL")
        return data_excel
    except Exception as e:
        logger_utils.error(f"Ошибка {e}")
        return f"Ошибка {e}"


def currency_rates(setting):
    """Получает курс валюты к рублю через API ЦБ РФ."""
    currency_code = setting["user_currencies"]
    url = "https://www.cbr-xml-daily.ru/daily_json.js"
    result = []
    for currency in currency_code:
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            if currency.upper() in data["Valute"]:
                valute_data = data["Valute"][currency.upper()]
                new_dict = {
                    "currency": valute_data["CharCode"],
                    "rate": valute_data["Value"],
                }
                result.append(new_dict)
                logger_utils.info("Получили курс валют")
            else:
                logger_utils.error(f"Валюта {currency_code} не найдена")
                return {"error": f"Валюта {currency_code} не найдена"}

        except Exception as e:
            logger_utils.error(f"ERROR:{e}")
            return {}
    return result


def stock_prices(setting):
    """
    Получает данные по акциям.
    Возвращает список словарей
    """
    tickers_list: list[str] = setting.get("user_stocks")
    stock_list = []
    for ticker in tickers_list:
        try:
            stock = yf.Ticker(ticker)
            info = stock.info
            stock_data = {"stock": ticker, "price": info.get("previousClose")}
            stock_list.append(stock_data)
            logger_utils.info(f"Получена цена акции {ticker} ")
        except Exception as e:
            logger_utils.error(f"Не удалось получить данные для {ticker}: {e}")
            continue
    return stock_list
