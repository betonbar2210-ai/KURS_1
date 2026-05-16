from datetime  import datetime

import pandas as pd
from pandas import DateOffset

from config import modul_log
from src.decorators import save_reports

logger_reports = modul_log("reports")

@save_reports()
def spending_by_category(df, category, date = None):
    """Функция для вывода расходов по категориям
    Дату указывыать в формате ДД.ММ.ГГГГ"""
    logger_reports.info(f"Переводим дату в формат datetime")
    df['Дата платежа'] = pd.to_datetime(df['Дата платежа'], dayfirst=True)
    logger_reports.info(f"Если дата не указана, то берем текущую дату")
    if date is None:
        actual_date = datetime.now()
    elif isinstance(date, str):
        logger_reports.info(f"Если дата указана, то преобразуем в формат datetime")
        try:
            actual_date = datetime.strptime(date, "%d.%m.%Y")
        except ValueError:
            logger_reports.error("Ошибка: Неверный формат даты. Используйте 'ДД.ММ.ГГГГ'")
            return "Ошибка: Неверный формат даты. Используйте 'ДД.ММ.ГГГГ'"
    elif isinstance(date, datetime):
        actual_date = date
    else:
        logger_reports.error("Ошибка: Дата должна быть строкой или объектом datetime")
        return "Ошибка: Дата должна быть строкой или объектом datetime"
    start_date = actual_date - DateOffset(months=3)
    logger_reports.info(f"Фильтруем по категории {category} и дате {date}")
    filter_data = df[
                      (df['Категория'] == category) &
                      (df['Дата платежа'] <= actual_date) &
                      (df['Дата платежа'] >= start_date)]
    filter_data['Дата платежа'] = filter_data['Дата платежа'].dt.strftime('%d.%m.%Y')
    logger_reports.info(f"Выводим дату платежа у сумму операции")
    return filter_data[['Дата платежа', 'Сумма операции с округлением']].to_dict(orient='records')
