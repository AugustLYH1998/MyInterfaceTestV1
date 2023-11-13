import unittest
from htmltestreport import HTMLTestReport

# 创建 suite 实例
from py10_unittest_demo import TestAdd

suite = unittest.TestSuite()

# 指定测试类，添加 测试方法
suite.addTest(unittest.makeSuite(TestAdd))

# 创建 HTMLTestReport 实例
runner = HTMLTestReport("测试报告.html")

# 调用 run() 传入 suite
runner.run(suite)