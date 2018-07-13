# coding: utf-8

import os


class Config(object):

        # 数据库连接
        SQLALCHEMY_DATABASE_URI = "mysql://root:111@localhost/wxapp"
        SQLALCHEMY_POOL_SIZE = 32

        #日志记录
        DEBUG = True
        LOG_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "var")
        LOCAL_HOST = "0.0.0.0"
        LOCAL_PORT = 9922


