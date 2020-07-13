# -*- coding: utf-8 -*-
from kombu import Connection


class BaseConfig(object):

    @classmethod
    def get_connection(cls):
        connection = Connection(hostname=cls.Hostname, userid=cls.UserId, password=cls.Password,
                                virtual_host=cls.VirtualHost, port=cls.Port)
        return connection


class Develop(BaseConfig):
    Hostname = '192.168.204.30'
    # 以下均为Connection默认值
    UserId = 'guest'
    Password = 'guest'
    Port = 5672
    VirtualHost = '/'


_config_dict = {"develop": Develop}
config_use = _config_dict.get('develop')
# config_use.get_connection()
