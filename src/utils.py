import os
import pandas as pd

def reader_excel():
    """Функция чтения EXCEL файла с помощью pandas"""
    way_excel = os.path.abspath('../data/operations.xlsx')
    data_excel = pd.read_excel(way_excel)
    return data_excel


def filter_pay():
    """Убираем пополнения оставляя расходы,
    Группируем по номеру карты, Суммируем, Меняем минус на плюс"""
    data_frame = reader_excel()
    df_filter = data_frame.loc[data_frame['Сумма операции'] < 0]
    df_group = df_filter.groupby(by=['Номер карты'])
    result = df_group['Сумма операции'].sum().abs()
    return result #добавить в json cashback = round(result/100, 2)


def new_filter_pay_dict():
    """Принимаем df из filter_pay преобразуем в список словарей
    добавляем кэшбэк из расчета 1 руб на 100 руб затрат
    пример
    {
      "last_digits": "5814",
      "total_spent": 1262.00,
      "cashback": 12.62
    }
    """
    my_dict = filter_pay()
    new_dict = {}
    cards = []
    if new_dict not in cards:
        for key, value in my_dict.items():
            new_dict["last_digits"] = key[-4:]
            new_dict["total_spent"] = value
            new_dict["cashback"] = round(value/100, 2)
            cards.append(new_dict)
    return cards


def sort_pay():
    """Сортируем по суммам затрат и выводим 5 самых крупных"""
    data_frame = reader_excel()
    sort_df = data_frame.sort_values(by=['Сумма операции с округлением'], ascending=False)
    result = sort_df[['Дата платежа', 'Сумма операции с округлением', 'Категория', 'Описание']]
    return result.head()

if __name__ == '__main__':
    print(new_filter_pay_dict())