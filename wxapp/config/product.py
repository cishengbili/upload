# coding: utf-8

import os


class Config(object):

        # 数据库连接
        SQLALCHEMY_DATABASE_URI = "mysql://root:111@localhost/newhand?unix_socket=/tmp/mysql.sock"
        SQLALCHEMY_POOL_SIZE = 32

        # ClassAPIDB:
        API_HOST = "rm-2ze86y2gl92wo2xw2o.mysql.rds.aliyuncs.com"
        API_PORT = 3306
        API_USER = "class"
        API_PASSWORD = "17_ccvideo-class"
        API_DATABASE = "liveclass"

        # RedisPubSub:
        REDIS_PSUB =  [('101.132.146.57', 16380)]
        REDIS_HOST = [('101.132.163.12', 16379)]
        REDIS_PASSWORD = "cc%_live^&redis36@ol"
        CHANNEL_FRONTEND = "meta_frontend.*"
        CHANNEL_BACKEND = "chat_backend.*"
        RESUB_TIMEOUT = 60

        #日志记录
        DEBUG = True
        LOG_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "var")

        THQS_KEY = "hand#rt_class@"
