from re import match


def interest_calculation(initial_value: float, rate: float, time: int):
    final_value = initial_value
    for _ in range(1, time+1):
        final_value += (final_value * rate)
    return final_value


def validate_input(input_str, pattern, error_message):
    while True:
        if match(pattern, input_str):
            return input_str
        else:
            print(error_message)
            input_str = input('Retry: ')


def main():

    initial_value_pattern = r"^\d+(?:\.\d+)?$"
    rate_pattern = r"^\d+(?:\.\d+)?%$"
    time_pattern = r"^\d+$"

    while True:
        initial_value = validate_input(
            input('Please type your initial value: '),
            initial_value_pattern,
            'Only numbers are allowed.'
        )
        interest_rate = validate_input(
            input('Please type your interest rate by month in % (e.g., 15.4%): '),
            rate_pattern,
            'Only percentage number is allowed.'
        )
        time = validate_input(
            input('Please type the investiment time in months: '),
            time_pattern,
            'Only integer numbers are allowed.'
        )

        initial_value_float = float(initial_value)
        rate_float = float(interest_rate[0:len(interest_rate)-1]) / 100
        time_int = int(time)

        total_value = interest_calculation(
            initial_value_float, rate_float, time_int)

        print(f'Your total amount at maturity will be ${total_value:.2f}')


if __name__ == '__main__':
    main()
