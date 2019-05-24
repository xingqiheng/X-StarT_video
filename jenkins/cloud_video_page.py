#!/user/bin/env python
# -*-encoding:utf-8-*-
from selenium.webdriver.common.by import By
import base_page
import time
from selenium.webdriver.support.wait import WebDriverWait
class Cloud_Video_Page(base_page.Action):
    # 进入【物联监控】
    close_window_loc = (By.XPATH, "//div[@id='app']/div[3]/div[2]/div/div/div/div/span")  # 收起告警事件悬浮窗
    enter_wulian_loc = (By.XPATH, "//p")

    #进入【云对讲呼叫台】
    cloud_call_desk_loc = (By.XPATH, "//*[@id='app']/div[1]/div[1]/div[2]/ul/li[4]/div/span")
    call_center_loc = (By.XPATH, "//*[@id='app']/div[1]/div[1]/div[2]/ul/li[4]/ul/li[1]/div/span")

    #进入【呼叫业主】
    click_call_owner_loc = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[3]/div/div/div/div[2]/div[2]/div[1]/div[3]/i[1]")

    #选择项目
    select_item_loc = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[3]/div/div/div/div[2]/div[2]/div[2]/div[1]/div[1]/span[2]")
    xinghai_item_loc = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[3]/div/div/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[1]/div[2]/div[2]/div[2]/div/div[2]/div[4]/div[1]/span[2]")

    #进入【电话搜索】
    telephone_search_loc = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[3]/div/div/div/div[2]/div[2]/div[2]/div[1]/div[2]/span[2]")
    enter_telephone_number_loc = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[3]/div/div/div/div[2]/div[2]/div[2]/div[1]/div[3]/form/div/div/div/input")
    click_search_button_loc = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[3]/div/div/div/div[2]/div[2]/div[2]/div[1]/div[3]/form/div/div/div/div/button")

    #点击呼叫按钮
    call_up_telephone_loc = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[3]/div/div/div/div[2]/div[2]/div[2]/div[1]/div[3]/div/div/div/div[3]")

    #结束通话
    hang_up_button01_loc = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[3]/div/div/div/div[2]/div[1]/div[1]/div/div[2]/div[3]/div[1]/div/div[2]/div/img")
    hang_up_button02_loc = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[3]/div/div/div/div[2]/div[1]/div[1]/div/div[2]/div[3]/div[3]/div/div/div[1]/img")
    hang_up_button03_loc = (By.XPATH, "/html/body/div[2]/p")



#=============== 断言元素 ===============
    msg_cloud_video_tip_loc = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[3]/div/div/div/div[2]/div[1]/div[1]/div/div[2]/div[2]/div/p")
    msg_call_up_tip_loc = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[3]/div/div/div/div[2]/div[1]/div[1]/div/div[2]/div[3]/div[1]/div/div[1]/div/p[2]")




    def enter_wulian(self,driver):
        self.find_element(*self.close_window_loc).click()
        # time.sleep(1)
        element = WebDriverWait(driver, 5, 1).until(lambda driver: self.find_element(*self.enter_wulian_loc))   #显式等待
        element.click()
        # self.find_element(*self.enter_wulian_loc).click()
        # time.sleep(2)

    def enter_cloud_video(self):
        self.find_element(*self.cloud_call_desk_loc).click()
        time.sleep(1)   #强制等待
        self.find_element(*self.call_center_loc).click()
        time.sleep(2)

    def click_call_owner(self):
        self.find_element(*self.click_call_owner_loc).click()
        time.sleep(1)

    def choose_item(self):
        self.find_element(*self.select_item_loc).click()
        time.sleep(1)
        self.find_element(*self.xinghai_item_loc).click()
        time.sleep(2)

    def telephone_search(self,values3):
        self.find_element(*self.telephone_search_loc).click()
        time.sleep(1)
        self.find_element(*self.enter_telephone_number_loc).send_keys(values3)
        time.sleep(1)
        self.find_element(*self.click_search_button_loc).click()
        time.sleep(1)

    def call_up(self):
        self.find_element(*self.call_up_telephone_loc).click()
        time.sleep(8)

    def hang_up(self):
        try:
            self.find_element(*self.hang_up_button01_loc).click()
            print(u'未接听，主动挂断')
        except Exception:
            try:
                self.find_element(*self.hang_up_button02_loc).click()
                print(u'通话中，主动挂断')
            except Exception:
                print(u'通话已结束')
        time.sleep(2)




#=============== 断言 ===============
    def result_enter_cloud_video(self):
        return self.find_element(*self.msg_cloud_video_tip_loc).text

    def result_call_up(self):
        return self.find_element(*self.msg_call_up_tip_loc).text