'''
Created on 2018年6月19日

@author: Administrator
'''
from selenium import webdriver
import unittest, time,os
# import HTMLTestReport
from BeautifulReport import BeautifulReport
from myemail import Email
# import yagmail


class YoudaoTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)  # 隐性等待时间为30秒
        self.base_url = "http://www.youdao.com"

    def test_youdao(self):
        u'有道测试'
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("translateContent").clear()

        try:
            driver.find_element_by_id("translateContent").send_keys("瓷器")
        except:
            driver.get_screenshot_as_file("H:\\fc\\screenshot\\kw.png")

        driver.find_element_by_id("translateContent").submit()
        time.sleep(3)
        driver.find_element_by_xpath("/html/body/div[7]/i/a[1]").click()
        driver.close()

        '''
        page_source=driver.page_source
        self.assertIn( "hello",page_source) 
        '''

    def close_alert_and_get_its_test(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text()
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
                return alert_text
        finally:
            self.accept_next_alert = True


if __name__ == "__main__":
    #unittest.main()

    # suite_tests = unittest.defaultTestLoader.discover(".",pattern="test_youdao.py",top_level_dir=None)
    # BeautifulReport(suite_tests).report(filename = '百度测试报告', description = '搜索测试', log_path = '.')
    
    testunit = unittest.TestSuite()
    testunit.addTest(YoudaoTest("test_youdao"))

    path = "H:\\fc\\TestReport"
    os.chdir(path)
    now = time.strftime("%Y-%m-%M-%H_%M_%S", time.localtime(time.time()))
    fp = open("result" + now + ".html", 'wb')
    runner = HTMLTestReport.HTMLTestRunner(stream=fp,
                                           title='test result',
                                           description=u'result:')
    runner.run(testunit)
    
    # yag = yagmail.SMTP(user="691618966@qq.com", password="ytrrkmtghhckbegf", host="smtp.qq.com")
    # contents = ["测试报告"]
    # yag.send("691618966@qq.com", "subject", contents)
    # yag.send(["15088558058@qq.com"], "subject", contents)
    # yag.send("15088558058@qq.com", "发送附件", contents, ["H:\\fc\\TestReport"])
    #
    # result_dir = r'H:\\fc\\TestReport'
    # lists = os.listdir(result_dir)
    # lists.sort()
    # file_new = os.path.join(lists[-1])
    # source_path = result_dir + '\\' + file_new

    
    email_host ="smtp.qq.com"
    host_port = 465
    from_addr ="691618966@qq.com"
    pwd ="ytrrkmtghhckbegf"
    # 获取最新生成的测试报告附件
    result_dir=r'H:\\fc\\TestReport'
    # result_dir = r'H:\\fc\\test_case'
    lists = os.listdir(result_dir)
    lists.sort()
    file_new = os.path.join(lists[-1])
    source_path= result_dir + '\\' + file_new
    to_addr_list=["15088558058@qq.com,691618966@qq.com"]
    email_content  = "t_report"
    email_content_html ="tttt"
    email_subject ="t_report"
    email_from ="12332"
    part_name = "test.html"
    email_obj = Email.get_email_obj(email_subject,email_from,to_addr_list)
    Email.attach_content(email_obj,email_content)
    Email.attach_part(email_obj,source_path,part_name)
    Email.send_email(email_obj,email_host,host_port,from_addr,pwd,to_addr_list)

    fp.close()
    




