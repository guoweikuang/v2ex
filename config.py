# -*- coding: utf-8 -*-
"""
v2ex config module

"""
import os

base_path = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """ 配置基类，所有其它配置类都要继承该类.
    """

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    """ 开发环境配置 """
    DEBUG = True


class ProductionConfig(Config):
    """ 生产环境配置 """
    DEBUG = False


class TestingConfig(Config):
    """ 测试环境配置 """
    TESTING = True
    DEBUG = True


config = {
    'development': DevelopmentConfig,
    'product': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig,
}