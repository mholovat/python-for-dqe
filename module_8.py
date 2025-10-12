import os

import module_6
import json

class JsonInput:
    def __init__(self, filename):
        self.filename = filename

    def read_from_json(self, filename):
        with open(self.filename, 'r') as f:
            json_dic = json.load(f)
            for pub_id, pub in json_dic:
                if pub['publication_type'].lower() == 'news' or publication_type.lower() == 'new':
                    news = module_6.News(pub['pub_text'], pub['news_city'])
                    news.publish(filename)
                elif pub['publication_type'].lower() == 'privatead':
                    privatead = module_6.PrivateAd(pub['pub_text'], pub['expiration_date'])
                    privatead.publish(filename)
                elif pub['publication_type'].lower() == 'birthdaywish':
                    birthdaywish = module_6.BirthdayWish(pub['pub_text'], pub['name'])
                    birthdaywish.publish(filename)

if __name__ == '__main__':
    filename = '/Users/Mykhailo_Holovatiuk/Downloads/publication.csv'

    print('Please enter the source for publications\n')
    print('1 - User input\n')
    print('2 - CSV file\n')
    print('3 - JSON file\n')

    user_input = input()
    if user_input == '1':
        module_6.read_from_input(filename)
    elif user_input == '2':
        input_folder = input("Please provide folder, otherwise the default folder will be used.: ")
        input_filename = input("Please provide your filename: ")
        input_file = module_6.InputFile(os.path.join(input_folder, input_filename))
        module_6.read_from_file(input_file.read_file(), filename)
    elif user_input == '3':
        input_folder = input("Please provide folder, otherwise the default folder will be used.: ")
        input_filename = input("Please provide your filename: ")
        json_input = JsonInput(os.path.join(input_folder, input_filename))
        json_input.read_from_json(filename)
