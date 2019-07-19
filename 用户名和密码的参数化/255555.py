# -*- coding: utf-8 -*-
# File  : 255555.py
# Date  : 2018/9/12
import unittest,time
from selenium import webdriver
# 构建登陆类，用unittest框架，所以是unittest.testCase
class test(unittest.TestCase):
    # 构建登陆异常的方法
    def test_login(self):
        dr = webdriver.Firefox()  # 调用谷歌浏览器，其他浏览器更改drvier
        # 需要测试的网页
        dr.get('https://passport.cnblogs.com/user/signin')
        # 构建参数化，格式为[[,,,],[,,,],[,,,]...[,,,]，
        # 最外面[]里的每个[]为一条用例，每条用例的项用,隔开
        user_pass = [['1', '1', '错误的用户名登陆', 'login_username_error', 'lblUserNameError', u'用户名错误！'],
                     ['', '123456', '不输入用户名登陆', 'login_username_null', 'lblUserNameError', u'请输入用户名！'],
                     ['testuser', '1', '错误的密码登陆', 'login_password_error', 'lblUserPwdError', u'密码错误'],
                     ['1', '', '不输入密码登陆', 'login_username_null', 'lblUserPwdError', u'请输入密码！']]
        # 参数化定义变量，变量名自定义，数量为需要变量的数量
        # 最多不超过参数化的数量，顺序与定义参数化的值顺序一致
        for (a, b, c, d, e, f) in user_pass:
            # 输入用户名，定义a在最前面，所以对应用例的一个值
            # find_element_by_id里的值为网页抓取到的元素
            dr.find_element_by_id('input1').send_keys(a)
            # 输入密码，b为参数化的密码
            dr.find_element_by_id('input2').send_keys(b)
            # 点击登陆，click()为点击事件
            dr.find_element_by_id('signin').click()
            time.sleep(2)
            print(c)  # c为参数化的测试目的
            # get_screenshot_as_file为截图方法，path为路径
            # d为参数化的图片名
            dr.get_screenshot_as_file(path + d + ".jpg")
            # 先验证提示类型是否正确，e为会显示错误信息的id元素
            assert dr.find_element_by_id(e).text, '提示信息类型错误！'
            # 如果提示类型正确，就会有错误信息，将错误信息赋值给定义的变量
            error_message = dr.find_element_by_id(e).text
            # asserEqual()是unittest框架中的一种断言，比较两个值是否相等
            # f为参数化预期值
            self.assertEqual(error_message, f)
            # refresh()为浏览器刷新
            dr.refresh()
if __name__ == "__main__":
    unittest.main()
