def vowel_counter(sentence: str) -> int:
    vowels = 'AEIOU'
    upper_sentence = sentence.upper()
    counter = 0
    for i in upper_sentence:
        if vowels.find(i) >= 0:
            counter += 1
    return counter


def main():
    while True:
        sentence = input(
            'Please type a sentence to see how many vowels(a,e,i,o,u) it has: ')

        if not sentence:
            print('Please type something.')
            continue

        counter = vowel_counter(sentence)
        print(counter)


if __name__ == '__main__':
    main()
