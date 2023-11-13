"""
生成测试报告的步骤：
1. 创建测试套件实例。 suite
2. 添加 测试类
3. 创建 HTMLTestReport 类实例。 runner
4. runner 调用 run(), 传入 suite
"""
import unittest

from config import BASE_DIR
from scripts.test_emp_add_params import TestEmpAddParams
from scripts.test_ihrm_login_params import TestIhrmLoginParams

from htmltestreport import HTMLTestReport

# 1. 创建测试套件实例。 suite
suite = unittest.TestSuite()

# 2. 添加 测试类, 组装测试用例
suite.addTest(unittest.makeSuite(TestIhrmLoginParams))
suite.addTest(unittest.makeSuite(TestEmpAddParams))

# 3. 创建 HTMLTestReport 类实例。 runner
# runner = HTMLTestReport(BASE_DIR + "/report/ihrm.html")  # 绝对路径
runner = HTMLTestReport("./report/ihrm.html", description="描述", title="标题")  # 相对路径

# 4. runner 调用 run(), 传入 suite
runner.run(suite)