""" ihrm 断言的工具文件 """

# 定义 断言 函数
# def common_assert():
#     self.assertEqual(200, resp.status_code)   # self / resp 报错
#     self.assertEqual(True, resp.json().get("success"))
#     self.assertEqual(10000, resp.json().get("code"))
#     self.assertIn("操作成功", resp.json().get("message"))


# 定义 断言 函数
def common_assert(self, resp, status_code, success, code, message):
    self.assertEqual(status_code, resp.status_code)
    self.assertEqual(success, resp.json().get("success"))
    self.assertEqual(code, resp.json().get("code"))
    self.assertIn(message, resp.json().get("message"))