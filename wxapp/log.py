# coding: utf-8

import datetime
import logging
import os
import traceback

from visa.config import config

INFO = 'info'
DEBUG = 'debug'
ERROR = 'error'

# print(Logging.LOG_PATH)
_PATH = config.LOG_PATH
_DATE = datetime.datetime.today().strftime('%Y-%m-%d')
info_logging = os.path.join(_PATH, _DATE + '.info.log')
debug_logging = os.path.join(_PATH, _DATE + '.debug.log')
error_logging = os.path.join(_PATH, _DATE + '.error.log')


def _log_handle(log_type):
    """
    获取logging handle
    @params log_type: 日志类型，字符串类型，可选项：'info', 'error'。
    """
    log_name, path, level, template = {
        'info': (
            'INF', info_logging, logging.INFO,
            '[%(asctime)s %(levelname)3s]%(message)s'
        ),
        'debug': (
            'DBG', debug_logging, logging.DEBUG,
            '[%(asctime)s %(levelname)3s %(pathname)s]'
            '[%(module)s.%(funcName)s]%(message)s'
        ),
        'error': (
            'ERR', error_logging, logging.WARNING,
            '[%(asctime)s %(levelname)3s %(pathname)s]'
            '[%(module)s.%(funcName)s in line %(lineno)d %(threadName)s]%(message)s'
        )
    }[log_type]

    _logger = logging.getLogger(log_name)
    _formatter = logging.Formatter(template)

    # 输出到文件
    _f_hdlr = logging.FileHandler(path)
    _f_hdlr.setFormatter(_formatter)
    _logger.addHandler(_f_hdlr)

    # 输出到屏幕
    _c_hdlr = logging.StreamHandler()
    _c_hdlr.setFormatter(_formatter)
    _logger.addHandler(_c_hdlr)

    _logger.setLevel(level)
    return _logger

_RECORDING = config.DEBUG

log_info = _log_handle(INFO).info if _RECORDING else lambda x: ''
log_debug = _log_handle(DEBUG).debug if _RECORDING else lambda x: ''
log_error = _log_handle(ERROR).error if _RECORDING else lambda x: ''


def error_traceback():
    """
    记录错误的具体原因
    """
    if os.path.exists(error_logging):
        f = open(error_logging, "w")
        traceback.print_exc(file=f)
        f.close()
    else:
        traceback.print_exc()
