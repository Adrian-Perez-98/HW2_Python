def calculator(number1, number2, operator):
    """This function is a calculator for two numbers"""
    if operator == '+':
        x = float(number1) + float(number2)
        print(x)
        return x
    if operator == '-':
        x = float(number1) - float(number2)
        print(x)
        return x
    if operator == '*':
        x = float(number1) * float(number2)
        print(x)
        return x
    if operator == '/':
        x = float(number1) / float(number2)
        print(x)
        return x
    if operator == '//':
        x = int(number1) / int(number2)
        print(x)
        return x
    if operator == '**':
        x = pow(float(number1), float(number2))
        print(x)
        return x
    return False


def input_output():
    """This function prompts user for input and calculates those inputs"""
    x = True
    while x:
        num1 = input('Enter the first number: ')
        num2 = input('Enter the second number: ')
        op = input('Enter the operation: ')
        calculator(num1, num2, op)

        print()
        close = input('Do you wish to exit? ')
        if close == 'y':
            x = False
        print()


if __name__ == '__main__':
    input_output()
