from config import modul_log

logger = modul_log("views")


def greeting(date):
    logger.info("Получаем текущее время")
    time_now = date.hour
    logger.info("Получили из даты часы и перевели в число(int)")
    if 6 <= time_now < 12:
        return "Доброе утро"
    elif 12 <= time_now < 18:
        return "Добрый день"
    elif 18 <= time_now < 23:
        return "Добрый вечер"
    else:
        return "Доброй ночи"


def filter_pay(excel_file):
    """Убираем пополнения оставляя расходы"""
    df_filter = excel_file.loc[excel_file["Сумма операции"] < 0]
    logger.info("Фильтруем DataFrame оставили расходы")
    return df_filter


def group_number_card(excel_file):
    """Группируем по номеру карты, Суммируем, Меняем минус на плюс"""
    df_group = excel_file.groupby(by=["Номер карты"])
    logger.info("Группируем DataFrame по номеру карты")
    result = df_group["Сумма операции"].sum().abs()
    logger.info("Получаем сумму по номеру карты, меняем минус на плюс")
    return result


def new_filter_pay_list(excel_file):
    """Принимаем df из group_number_card преобразуем в список словарей
    добавляем кэшбэк из расчета 1 руб на 100 руб затрат
    пример
    {
      "last_digits": "5814",
      "total_spent": 1262.00,
      "cashback": 12.62
    }
    """
    cards = []
    logger.info("Получаем число из строки")
    for key, value in excel_file.items():
        try:
            numeric_value = float(value)
        except ValueError:
            logger.error("Ошибка при получении числа из строки")
            numeric_value = 0.0
            logger.info("Присваеваем 0.0 если ошибка")

        new_dict = {
            "last_digits": str(key)[-4:],
            "total_spent": numeric_value,
            "cashback": round(numeric_value / 100, 2),
        }
        cards.append(new_dict)
    logger.info("Присваиваем ключи словарю и добавляем в список")
    return cards


def sort_pay(excel_file):
    """Принимает DataFrame из filter_pay.
    Сортируем по суммам затрат и выводим 5 самых крупных"""
    logger.info("Сортируем по суммам затрат")
    sort_df = excel_file.sort_values(by=["Сумма операции с округлением"], ascending=False)
    logger.info("Выводим 5 самых крупных отсортированных затрат с нужными ключами")
    result = sort_df[["Дата платежа", "Сумма операции с округлением", "Категория", "Описание"]]
    return result.head()


def new_sort_pay_list(excel_file):
    """Принимаем df из sort_pay преобразуем в список словарей для правильного вывода
    пример
    [{
      "date": "21.12.2021",
      "amount": 1198.23,
      "category": "Переводы",
      "description": "Перевод Кредитная карта. ТП 10.2 RUR"
    }]
    """
    sort_list = []
    logger.info("Получаем список словарей для правильного вывода")
    for name, row in excel_file.iterrows():
        sort_dict = {
            "date": row["Дата платежа"],
            "amount": row["Сумма операции с округлением"],
            "category": row["Категория"],
            "description": row["Описание"],
        }
        sort_list.append(sort_dict)
    logger.info("Вывели список словарей с верными ключами и присвоили значения")
    return sort_list
