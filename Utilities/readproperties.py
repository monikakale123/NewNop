import configparser

config = configparser.RawConfigParser()

config.read("C:\\Users\\HP\\PycharmProjects\\NoCommerce Demo Project\\Configuration\\config.ini")


class Readconfig:

    @staticmethod
    def geturl():
        url = config.get('common info', 'Url')
        return url

    @staticmethod
    def getemail():
        email = config.get('common info', 'Email')
        return email

    @staticmethod
    def getpassword():
        password = config.get('common info', 'Password')
        return password
