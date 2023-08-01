from re import match


def is_palidrome_recursion(word: str) -> bool:
    if len(word) <= 0:
        return True

    if word[0] == word[len(word)-1]:
        return is_palidrome_recursion(word[1:len(word)-1])

    return False


def main():
    word_pattern = r"^[a-zA-Z0-9]+$"

    while True:
        word = input(
            'Please type a word to see if it is a palindrome(reads the same backward as forward, e.g., madam): ')

        if not match(word_pattern, word):
            print('Special characteres or white spaces are not allowed.')
            continue

        if is_palidrome_recursion(word):
            print(f'the word "{word}" is a palindrome')
        else:
            print(f'the word "{word}" is NOT a palindrome')


if __name__ == '__main__':
    main()
