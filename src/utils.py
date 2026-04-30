import os
import pandas as pd


def reader_excel():
    """Функция чтения EXCEL файла с помощью pandas"""
    way_excel = os.path.abspath("../data/operations.xlsx")
    data_excel = pd.read_excel(way_excel)
    return data_excel


def filter_pay():
    """Убираем пополнения оставляя расходы"""
    data_frame = reader_excel()
    df_filter = data_frame.loc[data_frame["Сумма операции"] < 0]
    return df_filter


def group_number_card():
    """Группируем по номеру карты, Суммируем, Меняем минус на плюс"""
    df_filter = filter_pay()
    df_group = df_filter.groupby(by=["Номер карты"])
    result = df_group["Сумма операции"].sum().abs()
    return result


def new_filter_pay_list():
    """Принимаем df из group_number_card преобразуем в список словарей
    добавляем кэшбэк из расчета 1 руб на 100 руб затрат
    пример
    {
      "last_digits": "5814",
      "total_spent": 1262.00,
      "cashback": 12.62
    }
    """
    my_dict = group_number_card()
    cards = []
    for key, value in my_dict.items():
        new_dict = {"last_digits": key[-4:], "total_spent": value, "cashback": round(value / 100, 2)}
        cards.append(new_dict)
    return cards


def sort_pay():
    """Сортируем по суммам затрат и выводим 5 самых крупных"""
    data_frame = filter_pay()
    sort_df = data_frame.sort_values(by=["Сумма операции с округлением"], ascending=False)
    result = sort_df[["Дата платежа", "Сумма операции с округлением", "Категория", "Описание"]]
    return result.head()


def new_sort_pay_list():
    """Принимаем df из sort_pay преобразуем в список словарей для правильного вывода
    пример
    [{
      "date": "21.12.2021",
      "amount": 1198.23,
      "category": "Переводы",
      "description": "Перевод Кредитная карта. ТП 10.2 RUR"
    }]
    """
    df = sort_pay()
    sort_list = []
    for name, data in df.iterrows():
        sort_dict = {
            "date": data["Дата платежа"],
            "amount": data["Сумма операции с округлением"],
            "category": data["Категория"],
            "description": data["Описание"],
        }
        sort_list.append(sort_dict)
    return sort_list
