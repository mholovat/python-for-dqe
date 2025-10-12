def count_words(file):
    word_count = {}
    with open(file) as f:
        for line in f:
            for word in line.lower().split():
                word_count[word] = word_count.get(word, 0) + 1

    return word_count


def count_letters(file):
    letter_count = {}
    uppercase_count = {}
    uppercase_percentage = {}
    output = {}

    with open(file) as f:
        for line in f:
            for letter in line:
                if letter.isspace():
                    pass
                else:
                    letter_count[letter.lower()] = letter_count.get(letter.lower(), 0) + 1
                    if letter.isupper():
                        uppercase_count[letter.lower()] = uppercase_count.get(letter.lower(), 0) + 1

    for letter in letter_count:
        uppercase_percentage[letter] = uppercase_count.get(letter, 0) / letter_count[letter]

    output['letter_count'] = letter_count
    output['uppercase_count'] = uppercase_count
    output['uppercase_percentage'] = uppercase_percentage

    return output


if __name__ == '__main__':
    filename = '/Users/Mykhailo_Holovatiuk/Downloads/publication.csv'
    word_count_file = '/Users/Mykhailo_Holovatiuk/Downloads/word_count.csv'
    letter_count_file = '/Users/Mykhailo_Holovatiuk/Downloads/letter_count.csv'

    word_count = count_words(filename)

    with open(word_count_file, 'w') as f:
        f.write('Word,Count\n')
        for word, count in word_count.items():
            f.write(word + ',' + str(count) + '\n')


    with open(letter_count_file, 'w') as f:
        f.write('Letter,Count,Uppercase Count,Uppercase Percentage\n')
        for letter in count_letters(filename)['letter_count']:
            f.write(letter + ',' + str(count_letters(filename)['letter_count'][letter])
                    + ',' + str(count_letters(filename)['uppercase_count'].get(letter,0))
                    + ',' + str(count_letters(filename)['uppercase_percentage'].get(letter,0)) + '\n')