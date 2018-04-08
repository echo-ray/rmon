""" rmon.config

"""

import os


class DevConfig():
    """development config
    """

    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATION = False
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    TEMPLATES_AUTO_RELOAD = True

class ProductConfig():
    """product environment config
    """
    DEBUG = False

    path = os.path.join(os.getcwd(), 'rmon.db').replace('\\', '/')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///%s' % path
