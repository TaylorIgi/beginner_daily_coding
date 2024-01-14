import requests
import pandas as pd

main_url = "http://data.fixer.io/api/latest"
access_key = "38c5db7cd2251ee9ee082d6d60b2fa35"
base = "EUR"

api_url = f"{main_url}?access_key={access_key}&base={base}"

def api_get_data(url_path):
    response = requests.get(url_path)
    return response

def check_api_get_data(response_sts_code):
    if response_sts_code in range(200, 300):
        return True
    return False

def from_api_get_to_dataframe(my_object):
    return pd.DataFrame(my_object.json())

response = api_get_data(api_url)

df = from_api_get_to_dataframe(response)
print(df.head(5))