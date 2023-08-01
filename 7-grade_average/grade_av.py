from re import match


def grade_average(
    first_subject: str,
    second_subject: str,
    third_subject: str,
    first: float,
    second: float,
    third: float
) -> dict:
    grade = dict()
    grade[first_subject] = first
    grade[second_subject] = second
    grade[third_subject] = third

    grade_quantity = 0
    total_grades = 0

    for _, numb in grade.items():
        total_grades += numb
        grade_quantity += 1

    av = total_grades / grade_quantity
    grade['average'] = av

    return grade


def validate_input(input_str, pattern, error_message):
    while True:
        if match(pattern, input_str):
            return input_str
        else:
            print(error_message)
            input_str = input('Retry: ')


def main():
    subject_pattern = r"^[a-zA-Z0-9]+$"
    grade_pattern = r"^(?:10|[1-9](?:\.\d+)?)$"

    while True:
        print('Please type 3 subjects and 3 grades to see your average grade.')

        first_subject = validate_input(
            input('Type the first subject: '),
            subject_pattern,
            'Only letters and numbers are allowed in subject input.'
        )
        first_grade = validate_input(
            input('Type the first grade between 0 and 10: '),
            grade_pattern,
            'Only numbers between 0 and 10 are allowed in grade input.'
        )

        second_subject = validate_input(
            input(
                'Type the second subject: '),
            subject_pattern,
            'Only letters and numbers are allowed in subject input.'
        )
        second_grade = validate_input(
            input('Type the second grade between 0 and 10: '),
            grade_pattern,
            'Only numbers between 0 and 10 are allowed in grade input.'
        )

        third_subject = validate_input(
            input('Type the third subject: '),
            subject_pattern,
            'Only letters and numbers are allowed in subject input.'
        )
        third_grade = validate_input(
            input('Type the third grade between 0 and 10: '),
            grade_pattern,
            'Only numbers between 0 and 10 are allowed in grade input.'
        )

        first_float = float(first_grade)
        second_float = float(second_grade)
        third_float = float(third_grade)

        grade = grade_average(
            first_subject,
            second_subject,
            third_subject,
            first_float,
            second_float,
            third_float
        )

        for subject, grade in grade.items():
            print(f'{subject} -> {grade}')


if __name__ == '__main__':
    main()
