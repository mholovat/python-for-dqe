import os
from datetime import date, datetime


class Publication:
    def __init__(self, pub_text, pub_type='Publication'):
        self.pub_text = pub_text
        self.pub_type = pub_type

    def publish(self,filename):
        with open(filename,'a') as f:
            f.write(self.pub_type + '==========\n')
            f.write(self.pub_text + '\n\n\n')


class News(Publication):
    def __init__(self, pub_text, news_city, date=date.today() ,pub_type='News'):
        super().__init__(pub_text, pub_type)
        self.news_city = news_city
        self.date = date

    def publish(self,filename):
        with open(filename,'a') as f:
            f.write(self.pub_type + '==========\n')
            f.write(self.pub_text + '\n')
            f.write(self.news_city + '====' + str(self.date) + '\n\n\n')


class PrivateAd(Publication):
    def __init__(self, pub_text, expiration_date ,pub_type='PrivateAd'):
        super().__init__(pub_text, pub_type)
        self.expiration_date = expiration_date

    def publish(self,filename):
        with open(filename,'a') as f:
            f.write(self.pub_type + '==========\n')
            f.write(self.pub_text + '\n')
            f.write('Days left: ' + str((datetime.strptime(self.expiration_date,'%Y-%m-%d').date() - date.today()).days) + '\n\n\n')


class BirthdayWish(Publication):
    def __init__(self, pub_text, name, pub_type='BirthdayWish'):
        super().__init__(pub_text, pub_type)
        self.name = name

    def publish(self,filename):
        with open(filename,'a') as f:
            f.write(self.pub_type + '==========\n')
            f.write(self.name + '\n')
            f.write(self.pub_text + '\n\n\n')


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


def read_from_input(filename):
    while 1==1:
        publication_type = input("Please provide the publication type out of the list: News, PrivateAd, BirthdayWish: ")
        pub_text = input("Please provide your publication text: ")

        if publication_type.lower() == 'news' or publication_type.lower() == 'new':
            news_city = input("Please provide your city: ")
            news = News(pub_text, news_city)
            news.publish(filename)
        elif publication_type.lower() == 'privatead':
            expiration_date = input("Please provide expiration date: ")
            privatead = PrivateAd(pub_text, expiration_date)
            privatead.publish(filename)
        elif publication_type.lower() == 'birthdaywish':
            name = input("Please provide your name: ")
            birthdaywish = BirthdayWish(pub_text, name)
            birthdaywish.publish(filename)

        if input("Please click Y if you would like to complete").lower() == 'y':
            break


def read_from_file(publications, filename):
    for pub in publications:
        if pub['publication_type'].lower() == 'news' or publication_type.lower() == 'new':
            news = News(pub['pub_text'], pub['news_city'])
            news.publish(filename)
        elif pub['publication_type'].lower() == 'privatead':
            privatead = PrivateAd(pub['pub_text'], pub['expiration_date'])
            privatead.publish(filename)
        elif pub['publication_type'].lower() == 'birthdaywish':
            birthdaywish = BirthdayWish(pub['pub_text'], pub['name'])
            birthdaywish.publish(filename)


if __name__ == '__main__':
    filename = '/Users/Mykhailo_Holovatiuk/Downloads/publication.csv'

    user_selection = input("Put F if you input publications from file, otherwise press enter: ")
    if user_selection.lower() == 'f':
        input_folder = input("Please provide folder, otherwise the default folder will be used.: ")
        input_filename = input("Please provide your filename: ")
        input_file = InputFile(os.path.join(input_folder, input_filename))
        read_from_file(input_file.read_file(), filename)
    else:
        read_from_input(filename)