# coding: utf-8

import os
import sys


def _load_config():
    try:
        mode = os.environ.get('MODE')
        print("MODE: %s" % mode)
        if mode == 'PRODUCTION':
            sys.path.append("/var/www/dream/webapp/conf")
            from .product import Config
            return Config
        else:
            from .default import Config 
            return Config
    except ImportError:
        from default import Config
        return Config


config = _load_config()
