def factorial_loop(number: int) -> int:
    factorial = 1
    i = number
    while i > 1:
        factorial *= i
        i -= 1
    return factorial


def factorial_recursion(number: int) -> int:
    if number <= 1:
        return 1
    return number * factorial_recursion(number - 1)


def main():
    while True:
        number = int(input('Please type a number to discover its factorial: '))

        if number < 0:
            print(
                'Please type a positive number, factorial of negative number is not defined.')
            break

        factorial = factorial_loop(number)

        if factorial_loop(number) == factorial_recursion(number):
            print(f'The factorial for {number} is: {factorial}')


if __name__ == '__main__':
    main()
