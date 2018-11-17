# -*- coding: utf-8 -*-
"""
v2ex main

@author guoweikuang
"""
from flask import Flask
from config import config


def create_app(config_name: str):
    """ 工厂函数，用于延迟创建 Flask 实例，可用于创建多个实例.

    :param config_name: 配置名称，可根据开发环境、测试环境、生产环境区分
    :return: Flask 示例
    """
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    return app

