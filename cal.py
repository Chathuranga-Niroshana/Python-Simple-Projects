a = int(input("Enter First Number: "))
operator = input("Add Operator: ")
b = int(input("Enter Second Number: "))


def user_operator(operator, a, b):
    match operator:
        case "+":
            return add(a, b)
        case "-":
            return subtract(a, b)
        case "*":
            return multification(a, b)
        case "/":
            return devition(a, b)
        case _:
            return "Invalid"


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multification(a, b):
    return a * b


def devition(a, b):
    if b == 0:
        return "Cannot Devide by 0"
    return a / b


result = user_operator(operator, a, b)
print(f"Result= {result}")
