def normalize_string(input_str):
    return input_str.lower().replace(" iz ", " is ")

def collect_last_words(sentences):
    last_words = []

    # Iterate over all sentences to get last words
    for sentence in sentences:
        last_words.append(sentence.split(' ')[-1])

    # Make sure that the first word in the list of last words is capitalized
    last_words[0] = last_words[0].capitalize()

    return ' '.join(last_words).rstrip(' ')

def format_sentences(input_str):
    # Initialize list with sentences
    sentences = []

    # Iterate over all sentences in the normalized text
    for sentence in input_str.split('.'):

        # Convert sentence to list as string is immutable and we need to manipulate with it's elements
        sentence_list = list(sentence)

        # Iterate over characters
        for i in range(len(sentence_list) - 1):

            # If the symbol is alphanumeric (numeric needed to cover cases when sentence starts with number
            # convert it to uppercase and exit the loop
            if sentence_list[i].isalnum():
                sentence_list[i] = sentence_list[i].upper()
                break

        # Add the formatted sentence to the list of sentences
        sentences.append(''.join(sentence_list))

    return sentences

def count_spaces(input_str):
    # Initialize counter for whitespaces
    count_sp = 0

    # Iterate over characters in the final text and increase counter when whitespace is identified
    for char in final_text:
        if char.isspace():
            count_sp += 1

    return count_sp

def normalize_text(input_str):
    normalised_str = normalize_string(input_str)

    # Initialize list with sentences
    sentences = format_sentences(normalised_str)

    # Merge all sentences into the final text, including the last words
    return '.'.join(sentences) + collect_last_words(sentences) + '.'


if __name__ == '__main__':

    str = """homEwork:
    tHis iz your homeWork, copy these Text to variable.
    
    You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.
    
    it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.
    
    last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""

    final_text = normalize_text(str)

    # Print the results
    print("Normalized text is: ", final_text)
    print("Number of spaces is: ", count_spaces(final_text))