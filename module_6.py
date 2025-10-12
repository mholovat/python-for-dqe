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

def read_from_input():
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

if __name__ == '__main__':
    filename = '/Users/Mykhailo_Holovatiuk/Downloads/publication.txt'

    user_selection = input("Put F if you input publications from file, otherwise press enter: ")
    if user_selection.lower() == 'f':
        pass
    else:
        read_from_input()