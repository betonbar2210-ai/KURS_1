import json
from datetime import datetime
from src.services import filter_date_services, filter_nan_services, sort_cashhbac
from src.utils import currency_rates, stock_prices, reader_excel, reader_json
from src.views import new_filter_pay_list, greeting, filter_pay, group_number_card, sort_pay, new_sort_pay_list
from config import WAY_JSON, WAY_EXCEL





def home_page(date_now):
    excel_file = reader_excel(WAY_EXCEL)
    filter_pay_df = filter_pay(excel_file)
    group_df = group_number_card(filter_pay_df)
    filter_result = new_filter_pay_list(group_df)
    sort_data = sort_pay(filter_pay_df)
    result_sort = new_sort_pay_list(sort_data)
    greet = greeting(date_now)
    config = reader_json(WAY_JSON)
    currency = currency_rates(config)
    stock = stock_prices(config)
    result = {
            "greeting": greet,
            "cards": filter_result,
            "top_transactions": result_sort,
            "currency_rates": currency,
            "stock_prices": stock
        }
    json_home_page = json.dumps(result, ensure_ascii=False)
    return json_home_page


def services_page(df, year, month):
    filtered_df = filter_date_services(df, year, month)
    clear_df = filter_nan_services(filtered_df)
    group_df = sort_cashhbac(clear_df)
    result_dict = group_df.to_dict()
    result_json = json.dumps(result_dict, ensure_ascii=False)
    return result_json
