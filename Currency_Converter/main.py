def main():
    
    import utils
    import os

    value = float(input("Enter the amount you want to convert: "))
    currency_from = input("What is the original currency? ").upper()
    currency_to = input("To what currency you want to convert? ").upper()

    converted_value = utils.converter(value, currency_from, currency_to, utils.get_eur_rate(currency_from, currency_to))

    os.system("cls")
    print(f"Original amount= {currency_from} {round(value,2)}")
    print(f"Converted amount= {currency_to} {round(converted_value,2)}")

main()
    