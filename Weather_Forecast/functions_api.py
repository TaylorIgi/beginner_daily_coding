import pandas as pd
import requests

# Retorna a url completa se main_url e token forem não nulos
def get_city_full_url(main_url="", token="", name="", state=""):
    if main_url == "":
        print("Url is not valid!")
        return ""
    if token == "":
        print("Token is not valid!")
        return ""
    url = main_url + "token=" + token
    if name != "":
            url = url + "&name=" + name
    if state != "":
            url = url + "&state=" + state.upper()
    return url

# Faz o request GET para a API
def api_get_data(url):
    response = requests.get(url)
    return response

# Faz o request PUT para a API
def api_put_data(url, my_data, my_headers):
    response = requests.get(url, data=my_data, headers=my_headers)
    return response

# Checa se o request foi bem sucedido
def check_api_get_data(response_sts_code):
    if response_sts_code == 200:
        return True
    return False

# Cadastra a cidade no token e retorna a resposta do request
def register_city(url_prefix, url_suffix, token, city_id):
    url = f"{url_prefix}{token}{url_suffix}"
    payload = {'localeId[]': city_id}
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    return requests.put(url, data=payload, headers=headers)

# Transforma os dados da API em um dataframe
def from_api_get_to_dataframe(api_response):
    return pd.DataFrame(api_response.json())