from src.reports import spending_by_category


def test_spending_by_category(df_transactions):
    assert spending_by_category(df_transactions, "Супермаркеты", "15.10.2020") == [
        {"Сумма операции с округлением": 100.0, "Дата платежа": "15.10.2020"}
    ]

    assert (
        spending_by_category(df_transactions, "Супермаркеты", "15/10/2020")
        == "Ошибка: Неверный формат даты. Используйте 'ДД.ММ.ГГГГ'"
    )

    assert (
        spending_by_category(df_transactions, "Супермаркеты", 2020)
        == "Ошибка: Дата должна быть строкой или объектом datetime"
    )
