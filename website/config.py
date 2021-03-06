import os

# default config


class BaseConfig(object):
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///production.db'
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False
