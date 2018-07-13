# coding: utf-8

from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand
from wxapp import app
# 这一行必须要写，写上之后数据库才能同步建表
from wxapp.models import *

manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)
manager.add_command('shell', Shell(make_context=lambda: dict(app=app, db=db)))

if __name__ == '__main__':
    manager.run()
