# coding: utf-8

from datetime import timedelta
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


from wxapp.config import config

app = Flask(__name__)
CORS(app, resources=[r"/api/.*"], origins=r'.*')

# 数据库设置
app.config["SQLALCHEMY_DATABASE_URI"] = config.SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_SIZE"] = config.SQLALCHEMY_POOL_SIZE
app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"] = True
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["HOST"] = config.LOCAL_HOST
app.config["PORT"] = config.LOCAL_PORT

db = SQLAlchemy(app)

from wxapp.web.views import wxapp

app.register_blueprint(wxapp)
