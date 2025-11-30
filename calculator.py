def my_sum(a, b):
    result = a+b
    print(f"a + b = {result}")

def my_sub(a, b):
    result = a-b
    print(f"a - b = {result}")

def my_mul(a, b):
    result = a*b
    print(f"a * b ={result}")

def my_div(a, b):
    result = a/b
    print(f"a / b = {result}")

def my_pow(a, b):
    result = a**b
    print(f"a**b = {result}")

def my_sqrt(a):
    result = a**0.5
    print(f"sqrt({a}) = {result}")

def my_word():
    print("\033[31m Amalgare morede nazar poshtibani nemishavad!! \n \033[0m")

def my_calculator():
    a = float(input("\033[33m Adade avale morede nazar ra vared konid \n \033[0m"))
    b = float(input("\033[34m Adade dovome morede nazar ra vared konid \n \033[0m"))

    operator = input("\033[32m Amalgere morede nazar ra vared konid: (+ , -, **, /, sqrt) \n \033[0m")

    if operator=="+":
        my_sum(a, b)
    elif operator=="-":
        my_sub(a, b)
    elif operator=="*":
        my_mul(a, b)
    elif operator=="/":
        my_div(a, b)
    elif operator=="**":
        my_pow(a, b)
    elif operator=="sqrt":
        my_sqrt(a)
    else:
        my_word()

my_calculator()