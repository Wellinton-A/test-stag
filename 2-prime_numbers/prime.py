

def is_prime(number: int) -> bool:
    if number <= 1:
        return False
    # We only need to check divisors smaller than the square root of number because if number has a divisor smaller than its square root, it must also have a corresponding divisor greater than its square root.
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def main() -> None:
    prime_numbers = []
    check_numb = 2
    while len(prime_numbers) < 10:
        if is_prime(check_numb):
            prime_numbers.append(check_numb)
        check_numb += 1
    print(*prime_numbers)


print(int(30**0.5))

if __name__ == '__main__':
    main()
