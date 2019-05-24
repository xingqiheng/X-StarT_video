#!/user/bin/env python
# -*-encoding:utf-8-*-
from selenium.webdriver.common.by import By
import base_page
import time
class LoginPage(base_page.Action):
    #登录页元素
    name_loc = (By.XPATH, "//*[@value='login']")
    password_loc = (By.XPATH, "//*[@value='password']")
    submit_loc = (By.XPATH, "//*[@id='app']/div/div/div/form/button/span/button/span")




#=============== 断言元素 ===============

    #登录成功 - 断言元素     //*[@id="app"]/div[1]/div[1]/div[2]/div[2]/div[2]/div/span
    msg_top = (By.XPATH, "//*[@id='app']/div[1]/div[1]/div[2]/div[2]/div[2]/div/span")
    logout_loc = (By.XPATH, "//*[@id='app']/div[1]/div[1]/div[2]/div[2]/div[2]/ul/li[2]")
    wulian = (By.XPATH, "//p")
    login_msg = (By.CLASS_NAME, "login_tips")





#=============== 操作步骤 ===============

    def login(self,value1,value2):
        self.find_element(*self.name_loc).send_keys(value1)
        self.find_element(*self.password_loc).send_keys(value2)
        self.find_element(*self.submit_loc).click()
        time.sleep(2)





#=============== 断言 ===============

    def get_msg01(self):
        return self.find_element(*self.msg_top).text  #登录成功获取页面信息

    def get_msg02(self):
        return self.find_element(*self.msg_forget_pwd).text  #退出登录成功获取页面信息

    def result_login(self):
        try:
            self.find_element(*self.wulian).is_displayed()
            print(u'已成功登录账号')
        except Exception:
            print(u'未能正常登录账号')

    def login_result_msg(self):
        return self.find_element(*self.login_msg).text    #账号和密码不能为空 or 账号或密码错误



