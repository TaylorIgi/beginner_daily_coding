import pandas as pd
import requests

api_main_url = "http://apiadvisor.climatempo.com.br/api/v1/locale/city?"
my_token = "1766b03ce7ea5fbb097b15f4ef065905"
my_country = ""
my_name = "São P"
my_state = ""
my_province = ""

# Retorna a url completa se main_url e token forem não nulos
def get_full_url(main_url, token="", name="", state=""):
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

# Faz o request para a API
def api_get_data(url):
    response = requests.get(url)
    return response

# Checa se o request foi bem sucedido
def check_api_get_data(response_sts_code):
    if response_sts_code == 200:
        return True
    return False

# Transforma os dados da API em um dataframe
def from_api_get_to_dataframe(my_object):
    return pd.DataFrame(my_object.json())

api_response = api_get_data(get_full_url(api_main_url, my_token, my_name, my_state))

if not check_api_get_data(api_response.status_code):
     print("Erro ao carregar os dados da API")
     exit

print(from_api_get_to_dataframe(api_response).head(10))
