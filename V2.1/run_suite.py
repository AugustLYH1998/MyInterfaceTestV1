import os
import unittest

if __name__=='__main__':
    # unittest.main()

    # # 创建 TestSuite 对象
    # suite = unittest.TestSuite()

    # # 将要运行的测试方法添加到 TestSuite 中
    # suite.addTest(TestLogin('test01_login_ok'))

    # # 创建 TextTestRunner 对象并运行测试
    # unittest.TextTestRunner().run(suite)
    
    dir_path = os.path.dirname(__file__)+'/scripts'
    # print(dir_path)

    test_suite = unittest.defaultTestLoader.discover(start_dir=dir_path)

    unittest.TextTestRunner().run(test_suite)
