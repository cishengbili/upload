# coding: utf-8

import json
import datetime
import copy






from wxapp import db


class imgInfo(db.Model): 
    """ 
    用户对应的公钥存储表
    """
    __tablename__ = "img_info"

    id = db.Column(db.Integer, primary_key=True)
    # 文件名称
    filename = db.Column(db.String(64))
    # 生成时间
    create_time = db.Column(db.DateTime, nullable=True)

    def __str__(self):
        return "filename: %s" % (self.filename)

