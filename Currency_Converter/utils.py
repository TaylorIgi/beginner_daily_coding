import requests
import pandas as pd

main_url = "http://data.fixer.io/api/latest"
access_key = "38c5db7cd2251ee9ee082d6d60b2fa35"

def api_get_data(url_path):
    response = requests.get(url_path)
    return response

def check_api_get_data(response_sts_code):
    if response_sts_code in range(200, 300):
        return True
    return False

def from_api_get_to_dataframe(my_object):
    return pd.DataFrame(my_object.json())

def get_eur_rate(currency_code_from, currency_code_to):
    api_url = f"{main_url}?access_key={access_key}&symbols={currency_code_from}, {currency_code_to}"
    response = api_get_data(api_url)
    if not check_api_get_data:
        return -1
    df_currency = from_api_get_to_dataframe(response)
    rates = []
    for row in range(0, len(df_currency)):
        rates.append({"currency_name": df_currency.iloc[row].name, "currency_rate": df_currency.iloc[row]["rates"]})
    return rates

def converter(value, currency_code_from, currency_code_to, rates):
    if rates[0]["currency_name"] == currency_code_from:
        return value * rates[1]["currency_rate"] / rates[0]["currency_rate"]
    return value * rates[0]["currency_rate"] / rates[1]["currency_rate"]