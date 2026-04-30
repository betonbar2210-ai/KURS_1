from src.views import new_filter_pay_list, new_sort_pay_list, greeting
from src.services import currency_rates, stock_prices


def home_page(date_time):
    filter_data = new_filter_pay_list()
    sort_data = new_sort_pay_list()
    greet = greeting()
    currency = currency_rates()
    stock = stock_prices()
    result = {
        "greeting": greet,
        "cards": filter_data,
        "top_transactions": sort_data,
        "currency_rates": currency,
        "stock_prices": stock
    }
    return result
