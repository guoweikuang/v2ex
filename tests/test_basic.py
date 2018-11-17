
# -*- coding: utf-8 -*-
"""
TDD 测试驱动开发

"""
import unittest
from flask import current_app
from server import create_app


class UserTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_app_is_exist(self):
        """测试 Flask 实例是否存在"""
        self.assertFalse(current_app is None)


if __name__ == '__main__':
    unittest.main()
