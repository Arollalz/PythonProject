# coding = utf-8
import time
from selenium import webdriver
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import threading
class Witkeyuser(threading.Thread):
    def __init__(self, name, password, task_limit_number=2):
        threading.Thread.__init__(self)
        self.name = name
        self.password = password
        self.task_limit_number = task_limit_number

    def run(self):
        # chrome
        # chromedriver = os.getcwd()+"\chromedriver.exe"
        # os.environ["webdriver.chrome.driver"] = chromedriver
        # browser = webdriver.Chrome(chromedriver)

        # firefox
        # browser = webdriver.Firefox()

        # phantom
        phantomjsdriver = os.getcwd()+"\phantomjs.exe"
        os.environ["webdriver.phantomjs.driver"] = phantomjsdriver
        browser = webdriver.PhantomJS(phantomjsdriver)

        browser.get("http://172.16.8.7:4031/")
        # browser.get("http://witkey.iclassedu.com/#/")
        #go to login page
        browser.find_element_by_xpath("/html/body/div[1]/div/div/nav/ul/li[2]").click()
        #login with name and password
        WebDriverWait(browser, 10).until(lambda the_driver: the_driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[1]/div[1]/input").is_displayed())

        browser.find_element_by_css_selector("body > div.container > div.content.animate-view.ng-scope > div.sec-panel.box-container.ng-scope > div.sec-panel-content.box-content > div.field.first > input").send_keys(self.name)
        browser.find_element_by_css_selector("body > div.container > div.content.animate-view.ng-scope > div.sec-panel.box-container.ng-scope > div.sec-panel-content.box-content > div:nth-child(3) > input").send_keys(self.password)
        browser.find_element_by_css_selector("body > div.container > div.content.animate-view.ng-scope > div.sec-panel.box-container.ng-scope > div.sec-panel-content.box-content > div:nth-child(5) > button").click()

        #begin to check work
        WebDriverWait(browser, 10).until(lambda the_driver: the_driver.find_element_by_xpath("/html/body/div[4]/div[2]/div[1]/div[3]/button/span").is_displayed())
        browser.find_element_by_xpath("/html/body/div[4]/div[2]/div[1]/div[3]/button/span").click()
        #check
        finished_task_num = 0
        while finished_task_num < self.task_limit_number:
            time.sleep(2)# wait for server pushing new order
            try:
                # browser.find_element_by_class_name("popup-mask").is_displayed()
                WebDriverWait(browser, 10).until(lambda the_driver: the_driver.find_element_by_xpath("/html/body/div[4]/div[2]/div[2]/div[3]/div/div[2]/div/div[1]/span[2]/span/ul/li[7]").is_displayed())
                browser.find_element_by_xpath("/html/body/div[4]/div[2]/div[2]/div[3]/div/div[2]/div/div[1]/span[2]/span/ul/li[7]").click()
                browser.find_element_by_id("questionSubmit").click()
                time.sleep(0.5)
                WebDriverWait(browser, 10).until(lambda the_driver: EC.element_to_be_clickable(the_driver.find_element_by_id("questionSubmit")))
                browser.find_element_by_id("questionSubmit").click()
                finished_task_num += 1
            except:
                finished_task_num -= 1
                print "popup is displayed, wait..."
        # quit
        browser.quit()
