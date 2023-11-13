import unittest
from htmltestreport import HTMLTestReport   # 小写的是包名，大写的是类名
from case.test_login import TestLogin   # 导入测试用例类
from get_base_dir import BASE_DIR    # 获取项目目录


# 2. 创建 测试套件实例
suite = unittest.TestSuite()   # () 不能丢！千万不能丢！

# 3. 测试套件实例，调用 addTest() ，组装测试用例。
suite.addTest(unittest.makeSuite(TestLogin))

# 4. 指定 生成的测试报告的 路径 和 名称
report_path = BASE_DIR + '/report/login测试报告.html'  # 指定目录，如果目录不存在，会报错。 报告的后缀名，必须是 html

# 5. 创建 HTMLTestReport 类的实例，同时，使用上面指定好的报告名、标题（可选）、描述（可选）
ht_report = HTMLTestReport(report_path, title='登录测试报告',
                           description='没有使用验证码，对登录进行测试')

# 6. 运行测试套件组装的测试用例，生成报告
ht_report.run(suite)