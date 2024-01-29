import pandas as pd
import functions_api as api
import static_variables as var

# Pega o nome (ou parte dele) da cidade, printa as cidades possíveis e pede o ID da cidade escolhida
def get_user_city_id():
    partial_name = input("Qual a cidade? ")
    response_city = api.api_get_data(api.get_city_full_url(var.city_url_prefix, var.my_token, partial_name))
    if not api.check_api_get_data(response_city.status_code):
        print("Erro ao conectar na lista de cidades!")
        print(response_city.text)
        return -1
    print(api.from_api_get_to_dataframe(response_city))
    return int(input("Digite o ID da cidade: "))

# Retorna um dataframe com os dados do clima da cidade escolhida
def get_city_df(city_id):
    response_register = api.register_city(var.register_url_prefix, var.register_url_suffix, var.my_token, city_id)
    if not api.check_api_get_data(response_register.status_code):
        print(f"Erro no cadastro da cidade! {city_id}")
        print(response_register.text)
        print(response_register.status_code)
        return pd.DataFrame()
    
    response_weather = api.api_get_data(var.weather_url_prefix + str(city_id) + var.weather_url_suffix + var.my_token)
    if not api.check_api_get_data(response_weather.status_code):
        print("Erro ao conectar nos dados do clima!")
        print(response_weather.text)
        return pd.DataFrame()

    return api.from_api_get_to_dataframe(response_weather)