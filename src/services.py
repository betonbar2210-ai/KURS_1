import pandas as pd

from config import modul_log

logger_services = modul_log("services")


def filter_date_services(df, year, month):
    """Функция фильтрации dataFrame по году и месяцу"""
    logger_services.info(f"Фильтруем DataFrame по году {year} и месяцу {month}")
    df["Дата операции"] = pd.to_datetime(df["Дата операции"], format="%d.%m.%Y %H:%M:%S", errors="coerce")
    filtered_df = df[(df["Дата операции"].dt.year == int(year)) & (df["Дата операции"].dt.month == int(month))]
    return filtered_df


def filter_nan_services(dataframe):
    """Принимаем DataFrame из filter_date_services
    удаление строк с пустыми значениями кэшбэка"""
    logger_services.info("Удаляем строки с пустыми значениями кэшбэка")
    return dataframe.dropna(subset=["Кэшбэк"])


def sort_cashhbac(dataframe):
    """Принимает DataFrame из filter_nan_services
    Группируем по по категориям
    Выводим топ 3"""
    logger_services.info("Группируем по категориям")
    group_sort_df = dataframe.groupby(by=["Категория"])
    logger_services.info("Суммируем кэшбэк")
    z = group_sort_df["Кэшбэк"].sum()
    logger_services.info("Выводим топ 3")
    return z.head(3)
