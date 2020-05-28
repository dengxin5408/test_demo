import os
import configparser

file = os.path.join(os.path.dirname(os.path.dirname(__file__)), "config", "config.ini")
config = configparser.ConfigParser()  # 调用外部的读取配置文件的方法，实例化config
config.read(file, encoding='utf-8')


class ReadConfig():
    def get_http(self, name):
        value = config.get('HTTP', name)
        return value
    def get_email(self, name):
        value = config.get('EMAIL', name)
        return value

    def get_mysql(self, name):
        value = config.get('DATABASE', name)
        return value