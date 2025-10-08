# Importing random to generate random numbers and letters
import random

# Importing string to easily access the alphabet
import string

# Generate a random number of dicts (2 to 10)
number_of_dicts = random.randint(2, 10)

# Initialise list to store dictionaries
dicts_list = []

def populate_dictionary(num_keys):
    # Initialise empty dict within loop iteration
    dict_object = {}

    # Initialise counter for dict
    j = 0

    # Populate dictionary with random key-value pairs
    while j < num_keys:
        # Randomly choose a lowercase letter for the key
        key = random.choice(string.ascii_letters).lower()

        # Check if the key already exists
        if not dict_object.get(key):
            pass

        # Randomly choose a number (0-100) for the value
        value = random.randint(1, 100)
        # Add the key-value pair to the dictionary
        dict_object[key] = value

        # Increment counter
        j += 1

    return dict_object


def merge_dictionaries(dictionaries_list):
    # Initialise merged dict

    merged_dict = {}

    for dict in dictionaries_list:
        # Iterate over dictionary
        for key, value in dict.items():
            # Check bigger value for a key, if key already was retrieved from one of the previous dicts
            if key in merged_dict:
                if value > merged_dict[key]:
                    merged_dict[key] = value

            # If the key does not exist in merged dict - add it
            else:
                merged_dict[key] = value

    return merged_dict


# Populate dicts
for i in range(number_of_dicts):
    # Generate a random number of keys for each dict (1 to 26 based on English alphabet)
    number_keys = random.randint(1, 26)

    # Append the dictionary to the list
    dicts_list.append(populate_dictionary(number_keys))


print(merge_dictionaries(dicts_list))