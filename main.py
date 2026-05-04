from src.views import new_filter_pay_list, greeting, filter_pay, group_number_card, sort_pay, new_sort_pay_list
from src.utils import currency_rates, stock_prices, reader_excel, reader_json


def home_page():
    excel_file = reader_excel('data/operations.xlsx')
    filter_pay_df = filter_pay(excel_file)
    group_df = group_number_card(filter_pay_df)
    filter_result = new_filter_pay_list(group_df)
    sort_data = sort_pay(filter_pay_df)
    result_sort = new_sort_pay_list(sort_data)
    greet = greeting()
    config = reader_json('user_settings.json')
    currency = currency_rates(config)
    stock = stock_prices(config)
    result = {
        "greeting": greet,
        "cards": filter_result,
        "top_transactions": result_sort,
        "currency_rates": currency,
        "stock_prices": stock
    }
    return result

if __name__ == '__main__':
    print(home_page())