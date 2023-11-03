# 生成测试报告
import unittest
from htmltestreport import HTMLTestReport

# 1、创建 suite 实例
from unitest_demo import TestAdd
suite = unittest.TestSuite()

""" 
1、实例化测试集对象 suite = unittest.TestSuite()
2、添加指定类的全部测试方法。
suite.addTest(unittest.makeSuite(类名))
"""
# 2、指定测试类，添加 测试方法
suite.addTest(unittest.makeSuite(TestAdd))

# 3、创建 HTMLTestReport 实例
runner = HTMLTestReport("测试报告.html")

# 4、调用 run() 传入 suite
runner.run(suite)
