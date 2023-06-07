import configparser

config = configparser.RawConfigParser()
config.read(".\\configurations\\config.ini")


class ReadConfig:

    @staticmethod
    def geturl():
        return config.get('common info', 'LOGIN_URL')

    @staticmethod
    def getusername():
        return config.get('common info', 'USER_NAME')

    @staticmethod
    def getpassword():
        return config.get('common info', 'PASSWORD')
