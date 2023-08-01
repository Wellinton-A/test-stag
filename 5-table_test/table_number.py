from re import match


def table_number(number: int | float) -> dict:
    table = dict()
    for i in range(1, 11):
        table[f"{i}"] = number * i
    return table


def main():

    pattern_number = r"^\d+(\.\d+)?$"

    while True:
        number = input(
            'Please type a number to discover its table from 1 to 10: ')

        if not match(pattern_number, number):
            print('only numbers are allowed, please try again.')
            continue

        if number.find('.') >= 0:
            number = float(number)
        else:
            number = int(number)

        table = table_number(number)
        for numb, result in table.items():
            print(f'{number} x {numb} = {result}')


if __name__ == '__main__':
    main()
