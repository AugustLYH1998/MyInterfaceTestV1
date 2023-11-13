# 导包
import unittest
from htmltestreport import HTMLTestReport

# 创建 suite 实例
from scripts.test_member_service import TestMemberService

suite = unittest.TestSuite()

# 添加测试用例
suite.addTest(unittest.makeSuite(TestMemberService))

# 创建 HTMLTestReport 类对象
runner = HTMLTestReport("./report/传智健康测试报告.html", description="描述", title="标题")

# 调用 run() 传入 suite
runner.run(suite)
