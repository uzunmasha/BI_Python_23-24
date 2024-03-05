def substract(a, b):
    return a - b


def divide(a, b):
    if b == 0:
        return "Error: division by zero"
    return a / b


def multiplication(a, b):
    answer = a * b
    return answer


def summing(a, b):
    return a + b


list_of_operators = ['/', '*', '-', '+']


def main(keyboard_input: str) -> float:
    '''
    Function checks operators, transform numbers to float,
    call math function described above (substract, divide,
    multiplication, summing) and return result. If operators
    are not in list or numbers cannot transform into floats,
    func returns error message.
    '''
    math_sign, operator_position = False, False
    
    for char in range(len(keyboard_input)):
        if keyboard_input[char] in list_of_operators:
            math_sign = keyboard_input[char]
            operator_position = char
            
    if math_sign == False:
        return 'Enter valid expression'
    
    num1 = keyboard_input[:operator_position].strip()
    num2 = keyboard_input[operator_position + 1:].strip()

    try:
        num1 = float(num1)
        num2 = float(num2)
        if math_sign == '/':
            return divide(num1, num2)

        elif math_sign == '-':
            return substract(num1, num2)

        elif math_sign == '+':
            return summing(num1, num2)

        elif math_sign == '*':
            return multiplication(num1, num2)

    except ValueError:
        return 'Enter valid expression'


if __name__ == '__main__':
    print(main(input('Enter expression:')))
