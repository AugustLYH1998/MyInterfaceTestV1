import os
import unittest
from scripts.test_crud import TestAdd
from scripts.test_login import TestApi
from htmltestreport import HTMLTestReport
from config import BASE_DIR

if __name__=='__main__':
    # unittest.main()

    # 创建 TestSuite 对象
    suite = unittest.TestSuite()

    # 将要运行的测试方法添加到 TestSuite 中
    # suite.addTest(TestAdd('test01_add'))
    # suite.addTest(unittest.makeSuite(TestEmpAddParams))
    
    suite.addTest(unittest.makeSuite(TestApi))
    # suite.addTest(TestApi('test_login'))

    # 创建 TextTestRunner 对象并运行测试
    # unittest.TextTestRunner().run(suite)

    # 创建 HTMLTestReport 类实例。 runner
    runner = HTMLTestReport(BASE_DIR + "/report/test_result.html") # 绝对路径

    # runner = HTMLTestReport("./report/ihrm.html", description="描述", title="标题") # 相对路径

    runner.run(suite)
    

    # ===========遍历所有文件==============
    # dir_path = os.path.dirname(__file__)+'/scripts'
    # # print(dir_path)

    # test_suite = unittest.defaultTestLoader.discover(start_dir=dir_path)

    # unittest.TextTestRunner().run(test_suite)
