import os

import module_6
import module_8
import xml.etree.ElementTree as ET

def read_from_xml(xml_file, filename):
    xml_input = ET.parse(xml_file)
    root = xml_input.getroot()

    for pub in root.iter('publication'):
        if pub.attrib['id'].lower() == 'news' or pub.attrib['id'].lower() == 'new':
            news = module_6.News(pub.find('pub_text').text, pub.find('news_city').text)
            news.publish(filename)
        elif pub.attrib['id'].lower() == 'privatead':
            privatead = module_6.PrivateAd(pub.find('pub_text').text, pub.find('expiration_date').text)
            privatead.publish(filename)
        elif pub.attrib['id'].lower() == 'birthdaywish':
            birthdaywish = module_6.BirthdayWish(pub.find('pub_text').text, pub.find('name').text)
            birthdaywish.publish(filename)


if __name__ == '__main__':
    filename = '/Users/Mykhailo_Holovatiuk/Downloads/publication.csv'

    print('Please enter the source for publications\n')
    print('1 - User input\n')
    print('2 - CSV file\n')
    print('3 - JSON file\n')
    print('4 - XML file\n')

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
        module_8.read_from_json(os.path.join(input_folder, input_filename), filename)
    elif user_input == '4':
        input_folder = input("Please provide folder, otherwise the default folder will be used.: ")
        input_filename = input("Please provide your filename: ")
        read_from_xml(os.path.join(input_folder, input_filename), filename)