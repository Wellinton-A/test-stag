from re import match
from time import sleep

print('Welcome to the simple calculator!\n Our calculator\'s operators are limited to addition, subtraction, multiplication, and division (+, -, /, *).\n Please follow the pattern "firstNumber operator secondNumber" (e.g., 42.42 + 42).')


def calculate(expression: str) -> float:
    try:
        return eval(expression)
    except ZeroDivisionError:
        print('A number cannot be divided by 0, please type another expression.')
    except Exception as e:
        print(f'Invalid input or expression. Error: {e}')


def main():
    pattern_operators = {
        r"^-?\d+(\.\d+)?\+\-?\d+(\.\d+)?$": '+',
        r"^-?\d+(\.\d+)?-\-?\d+(\.\d+)?$": '-',
        r"^-?\d+(\.\d+)?/\-?\d+(\.\d+)?$": '/',
        r"^-?\d+(\.\d+)?\*\-?\d+(\.\d+)?$": '*',
    }

    while True:
        sleep(1)
        user_expression = input(
            'Please type your required expression: ').replace(' ', '').strip()

        if not user_expression:
            print('Invalid input, please try another expression. (e.g., 42.42 * 42)')
            continue

        operator = None
        for pattern, op in pattern_operators.items():
            if match(pattern, user_expression):
                operator = op
                break

        if operator is None:
            print('Invalid input, please try another expression. (e.g., 42.42 * 42)')
            continue

        try:
            result = calculate(user_expression)
            print(f'Result is: {result}')
        except Exception as e:
            print(f'Error occurred while calculating the expression: {e}')


if __name__ == "__main__":
    main()
