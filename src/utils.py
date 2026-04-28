import os
import pandas as pd

def reader_excel(way_excel):
    """Функция чтения EXCEL файла с помощью pandas"""
    data_excel = pd.read_excel(way_excel)
    return data_excel

way = os.path.abspath('../data/operations.xlsx')
df = reader_excel(way)

def filter_pay(data_frame):
    """Убираем пополнения оставляя расходы,
    Группируем по номеру карты, Суммируем, Меняем минус на плюс"""
    df_filter = data_frame.loc[data_frame['Сумма операции'] < 0]
    df_group = df_filter.groupby(by=['Номер карты'])
    result = df_group['Сумма операции'].sum().abs()
    return result #добавить cashback = result/100


def sort_pay(data_frame):
    sort_df = data_frame.sort_values(by=['Сумма операции с округлением'], ascending=False)
    return sort_df[['Дата платежа', 'Сумма операции с округлением', 'Категория', 'Описание']]





if __name__ == '__main__':
     #print(f"Количество уникальных карт: {len(group_card(df))}")
     # print(filter_pay(df))
     # print(sort_pay(df).head())
     print(round(69284.00/100, 2))
