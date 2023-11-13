
import logging
import os
import unittest
from logging_use import init_log_config

def add(x, y):
    return x+y

class TestAPI(unittest.TestCase):

    # 初始化
    init_log_config(os.path.dirname(__file__)+'/test.log')

    def test_add(self):
        rs = add(10, 30)
        # print(rs)
        logging.debug(f'res={rs}')
        self.assertEquals(40, rs)


if __name__ == '__main__':
    unittest.main()