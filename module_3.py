str = """homEwork:
tHis iz your homeWork, copy these Text to variable.

You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.

last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""

# Normalize text by putting all letters to lowercase and replace word iz with is
normalised_str = str.lower().replace(" iz ", " is ")

# Initialize list with sentences
sentences = []

# Iterate over all sentences in the normalized text
for sentence in normalised_str.split('.'):

    # Convert sentence to list as string is immutable and we need to manipulate with it's elements
    sentence_list = list(sentence)

    # Iterate over characters
    for i in range(len(sentence_list)-1):

        # If the symbol is alphanumeric (numeric needed to cover cases when sentence starts with number
        # convert it to uppercase and exit the loop
        if sentence_list[i].isalnum():
            sentence_list[i] = sentence_list[i].upper()
            break

    # Add the formatted sentence to the list of sentences
    sentences.append(''.join(sentence_list))

# Initialize list for last words
last_words = []

# Iterate over all sentences to get last words
for sentence in sentences:
    last_words.append(sentence.split(' ')[-1])

# Make sure that the first word in the list of last words is capitalized
last_words[0] = last_words[0].capitalize()

# Merge all sentences into the final text, including the last words
final_text = '.'.join(sentences) + ' '.join(last_words).rstrip(' ') + '.'

# Initialize counter for whitespaces
count_spaces = 0

# Iterate over characters in the final text and increase counter when whitespace is identified
for char in final_text:
    if char.isspace():
        count_spaces += 1

# Print the results
print("Normalized text is: ", final_text)
print("Number of spaces is: ", count_spaces)