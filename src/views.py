from datetime import datetime
from src.utils import new_filter_pay_list, new_sort_pay_list
import json
from src.services import currency_rates


def greeting():
    date = datetime.now()
    time_now = int(date.strftime('%H'))
    if 6 <= time_now < 12:
        return "Доброе утро"
    elif 12 <= time_now < 18:
        return "Добрый день"
    elif 18 <= time_now < 23:
        return "Добрый вечер"
    else:
        return "Доброй ночи"

def json_conclusion(date_time):
    filter_data = new_filter_pay_list()
    sort_data = new_sort_pay_list()
    greet = greeting()
    currency_usd = currency_rates('USD')
    currency_eur = currency_rates('EUR')
    # stock = stock_prices(['AAPL', 'AMZN', 'GOOGL', 'MSFT', 'TSLA'])
    result = {
        "greeting": greet,
        "cards": filter_data,
        "top_transactions": sort_data,
        #"stock_prices": stock
        "currency_rates": [
            {
                "currency": currency_usd['CharCode'],
                "rate": currency_usd['Value']
            },
            {
                "currency": currency_eur['CharCode'],
                "rate": currency_eur['Value']
            }

        ]
    }
    return result

date = datetime.now().isoformat()
if __name__ == '__main__':
    print(json_conclusion(date))
