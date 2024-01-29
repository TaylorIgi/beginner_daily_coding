import pandas as pd
import requests

api_main_city_url = "http://apiadvisor.climatempo.com.br/api/v1/locale/city?"
api_main_weather_url = "http://apiadvisor.climatempo.com.br/api/v1/weather/locale/"
# api_main_weather_url = "http://apiadvisor.climatempo.com.br/api/v1/climate/temperature/locale/"
# api_main_weather_url = "http://apiadvisor.climatempo.com.br/api/v1/climate/rain/locale/"
api_suffix_weather_url = "/current?token="
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
def from_api_get_to_dataframe(api_response):
    return pd.DataFrame(api_response.json())

# api_response = api_get_data(get_full_url(api_main_city_url, my_token, my_name, my_state))

# if not check_api_get_data(api_response.status_code):
#      print("Erro ao carregar os dados da API")
#      exit

# df_cities = from_api_get_to_dataframe(api_response)

# choosen_city_index = int(input("Digite o número da cidade: "))
# choosen_city_id = df_cities.loc[choosen_city_index, "id"]
# choosen_city_name = df_cities.loc[choosen_city_index, "name"]
# choosen_city_state = df_cities.loc[choosen_city_index, "state"]

'''   ----------------------------------------------------   '''

import requests

url = f"http://apiadvisor.climatempo.com.br/api-manager/user-token/{my_token}/locales"
choosen_city_id = 3477

payload = {'localeId[]': choosen_city_id}
headers = {'Content-Type': 'application/x-www-form-urlencoded'}

response_register_city = requests.put(url.replace(':your-app-token', my_token), data=payload, headers=headers)

'''   ----------------------------------------------------   '''

api_response = api_get_data(api_main_weather_url + str(choosen_city_id) + api_suffix_weather_url + my_token)
print(api_main_weather_url + str(choosen_city_id) + api_suffix_weather_url + my_token)
if not check_api_get_data(api_response.status_code):
     print("Erro ao carregar os dados da API")
     exit

print(api_response)
print(api_response.text)

# df_weather = from_api_get_to_dataframe(api_response)

# print(df_weather.head(10))