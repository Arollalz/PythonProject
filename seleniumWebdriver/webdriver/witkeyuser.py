# coding = utf-8
import time
from selenium import webdriver
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
class Witkeyuser:
    def __init__(self, name, password, task_limit_number=2):
        self.name = name
        self.password = password
        self.task_limit_number = task_limit_number

    def checkTask(self):
        chromedriver = os.getcwd()+"\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromedriver
        browser = webdriver.Chrome(chromedriver)
        browser.get("http://172.16.8.5:4031/")
        #go to login page
        WebDriverWait(browser, 10).until(lambda the_driver: the_driver.find_element_by_xpath("/html/body/div[1]/div/div/nav/ul/li[2]").is_displayed())
        browser.find_element_by_xpath("/html/body/div[1]/div/div/nav/ul/li[2]").click()

        #login with name and password
        WebDriverWait(browser, 10).until(lambda the_driver: the_driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[2]/div[1]/input").is_displayed())
        browser.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[2]/div[1]/input").send_keys(self.name)
        browser.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[2]/div[2]/input").send_keys(self.password)
        browser.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[2]/div[3]/button").click()

        #begin to check work
        WebDriverWait(browser, 10).until(lambda the_driver: the_driver.find_element_by_xpath("/html/body/div[4]/div[2]/div[1]/div[3]/button/span").is_displayed())
        browser.find_element_by_xpath("/html/body/div[4]/div[2]/div[1]/div[3]/button/span").click()

        #check
        finished_task_num = 0

        while finished_task_num < self.task_limit_number:
            try:
                WebDriverWait(browser, 10).until(lambda the_driver: the_driver.find_element_by_xpath("/html/body/div[4]/div[2]/div[2]/div[3]/div/div[2]/div/div[1]/span[2]/span/ul/li[7]").is_displayed())
                browser.find_element_by_xpath("/html/body/div[4]/div[2]/div[2]/div[3]/div/div[2]/div/div[1]/span[2]/span/ul/li[7]").click()
                browser.find_element_by_id("questionSubmit").click()
                time.sleep(5)
                WebDriverWait(browser, 10).until(lambda the_driver: EC.element_to_be_clickable(the_driver.find_element_by_id("questionSubmit")))
                browser.find_element_by_id("questionSubmit").click()
                finished_task_num += 1
            except TimeoutException:
                finished_task_num -= 1
                print "timeout"
        # ng - scope
        # ng - isolate - scope
        browser.quit()
