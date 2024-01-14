'''
Goal: create a Python program that emulates a basic calculator
Inspiration: Chat GPT
'''

def my_sum(number1, number2):
    return int(number1) + int(number2)

def my_subtraction(number1, number2):
    return int(number1) - int(number2)

def my_multiplication(number1, number2):
    return int(number1) * int(number2)

def my_division(number1, number2):
    return int(number1) / int(number2)

# def check_operation(character):
#     if character == "+":
#         return "sum"
#     elif character == "-":
#         return "subtraction"
#     elif character == '*':
#         return "multiplication"
#     elif character == '/':
#         return "division"

def main():

    user_math = input("Type your math: ")
    
    number1_array=[]
    number2_array=[]
    operation = "null"
    
    for i in range(0, len(user_math)):
        if user_math[i] not in ["+", "-", "*", "/"] and operation == "null":
            number1_array.append(user_math[i])
        elif user_math[i] not in ["+", "-", "*", "/"] and operation != "null":
            number2_array.append(user_math[i])
        else:
            operation = user_math[i]
    
    number1 = ''.join(map(str, number1_array))
    number2 = ''.join(map(str, number2_array))

    if operation == "+":
        result = my_sum(number1, number2)
    elif operation == "-":
        result = my_subtraction(number1, number2)
    elif operation == "*":
        result = my_multiplication(number1, number2)
    elif operation == "/":
        result = my_division(number1, number2)
    
    print(f"{number1} {operation} {number2} = {round(result, 2)}")
        

main()