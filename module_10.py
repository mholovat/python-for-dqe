import os
import sqlite3

class DBConnection:
    def __init__(self, filename):
        self.filename = filename
        self.conn = sqlite3.connect(filename)


    def insert_news(self, news):
        cursor = self.conn.cursor()
        cursor.execute(f'INSERT INTO news VALUES ({news.text}, {news.city}, {news.date})')
        cursor.close()
        self.conn.commit()
        self.conn.close()


    def insert_privatead(self, privatead):
        cursor = self.conn.cursor()
        cursor.execute(f'INSERT INTO privateads VALUES ({privatead.text}, {privatead.expiration_date})')
        cursor.close()
        self.conn.commit()
        self.conn.close()


    def insert_birthdaywish(self, birthdaywish):
        cursor = self.conn.cursor()
        cursor.execute(f'INSERT INTO birthdaywishes VALUES ({privatead.text}, {privatead.name})')
        cursor.close()
        self.conn.commit()
        self.conn.close()


class Publication:
    def __init__(self, pub_text, pub_type='Publication'):
        self.pub_text = pub_text
        self.pub_type = pub_type


class News(Publication):
    def __init__(self, pub_text, news_city, date=date.today()):
        super().__init__(pub_text, pub_type)
        self.news_city = news_city
        self.date = date

    def publish(self, dbconnection):
        dbconnection.insert_news(self)


class PrivateAd(Publication):
    def __init__(self, pub_text, expiration_date):
        super().__init__(pub_text, pub_type)
        self.expiration_date = expiration_date

    def publish(self, dbconnection):
        dbconnection.insert_privatead(self)


class BirthdayWish(Publication):
    def __init__(self, pub_text, name):
        super().__init__(pub_text, pub_type)
        self.name = name

    def publish(self, dbconnection):
        dbconnection.insert_birthdaywish(self)


class JsonInput:
    def __init__(self, filename):
        self.filename = filename

    def read_from_json(self, dbconnection):
        with open(self.filename, 'r') as f:
            json_dic = json.load(f)
            for pub_id, pub in json_dic:
                if pub['publication_type'].lower() == 'news' or publication_type.lower() == 'new':
                    news = News(pub['pub_text'], pub['news_city'])
                    news.publish(dbconnection)
                elif pub['publication_type'].lower() == 'privatead':
                    privatead = PrivateAd(pub['pub_text'], pub['expiration_date'])
                    privatead.publish(dbconnection)
                elif pub['publication_type'].lower() == 'birthdaywish':
                    birthdaywish = BirthdayWish(pub['pub_text'], pub['name'])
                    birthdaywish.publish(dbconnection)


class XMLInput:
    def __init__(self, input_file):
        self.input_file = input_file

    def read_from_xml(self, dbconnection):
        xml_input = ET.parse(self.input_file)
        root = xml_input.getroot()

        for pub in root.iter('publication'):
            if pub.attrib['id'].lower() == 'news' or pub.attrib['id'].lower() == 'new':
                news = News(pub.find('pub_text').text, pub.find('news_city').text)
                news.publish(dbconnection)
            elif pub.attrib['id'].lower() == 'privatead':
                privatead = PrivateAd(pub.find('pub_text').text, pub.find('expiration_date').text)
                privatead.publish(dbconnection)
            elif pub.attrib['id'].lower() == 'birthdaywish':
                birthdaywish = BirthdayWish(pub.find('pub_text').text, pub.find('name').text)
                birthdaywish.publish(dbconnection)


class InputFile:
    def __init__(self, filename):
        self.filename = filename

    def read_file(self):
        with open(self.filename,'r') as f:
            lines = f.readlines()

        publications = []
        for line in lines:
            publication = {}
            split_line = line.split()
            publication['publication_type'] = split_line[0]
            publication['pub_text'] = split_line[1]
            publication['news_city'] = split_line[2]
            publication['expiration_date'] = split_line[4]
            publication['name'] = split_line[5]

            publications.append(publication)

        return publications


def read_from_input(dbconnection):
    while 1==1:
        publication_type = input("Please provide the publication type out of the list: News, PrivateAd, BirthdayWish: ")
        pub_text = input("Please provide your publication text: ")

        if publication_type.lower() == 'news' or publication_type.lower() == 'new':
            news_city = input("Please provide your city: ")
            news = News(pub_text, news_city)
            news.publish(dbconnection)
        elif publication_type.lower() == 'privatead':
            expiration_date = input("Please provide expiration date: ")
            privatead = PrivateAd(pub_text, expiration_date)
            privatead.publish(dbconnection)
        elif publication_type.lower() == 'birthdaywish':
            name = input("Please provide your name: ")
            birthdaywish = BirthdayWish(pub_text, name)
            birthdaywish.publish(dbconnection)

        if input("Please click Y if you would like to complete").lower() == 'y':
            break


def read_from_file(publications, dbconnection):
    for pub in publications:
        if pub['publication_type'].lower() == 'news' or pub['publication_type'].lower() == 'new':
            news = News(pub['pub_text'], pub['news_city'])
            news.publish(dbconnection)
        elif pub['publication_type'].lower() == 'privatead':
            privatead = PrivateAd(pub['pub_text'], pub['expiration_date'])
            privatead.publish(dbconnection)
        elif pub['publication_type'].lower() == 'birthdaywish':
            birthdaywish = BirthdayWish(pub['pub_text'], pub['name'])
            birthdaywish.publish(dbconnection)


if __name__ == '__main__':
    db_connection = DBConnection('publications.db')

    print('Please enter the source for publications\n')
    print('1 - User input\n')
    print('2 - CSV file\n')
    print('3 - JSON file\n')
    print('4 - XML file\n')

    user_input = input()
    if user_input == '1':
        read_from_input(db_connection)
    elif user_input == '2':
        input_folder = input("Please provide folder, otherwise the default folder will be used.: ")
        input_filename = input("Please provide your filename: ")
        input_file = InputFile(os.path.join(input_folder, input_filename))
        read_from_file(input_file.read_file(), db_connection)
    elif user_input == '3':
        input_folder = input("Please provide folder, otherwise the default folder will be used.: ")
        input_filename = input("Please provide your filename: ")
        json_input = JsonInput(os.path.join(input_folder, input_filename))
        json_input.read_from_json(db_connection)
    elif user_input == '4':
        input_folder = input("Please provide folder, otherwise the default folder will be used.: ")
        input_filename = input("Please provide your filename: ")
        xml_input = XMLInput(os.path.join(input_folder, input_filename))
        xml_input.read_from_xml(db_connection)