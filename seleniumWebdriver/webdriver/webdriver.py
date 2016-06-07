# coding = utf-8
import time
from selenium import webdriver
import os


chromedriver = os.getcwd()+"\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
browser = webdriver.Chrome(chromedriver)
browser.get("http://172.16.8.5:4031/")
#go to login page
browser.find_element_by_xpath("/html/body/div[1]/div/div/nav/ul/li[2]").click()
time.sleep(3)
#login with name and password (15196775582 13096323190 18780165474)
browser.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[2]/div[1]/input").send_keys("18780165474")
browser.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[2]/div[2]/input").send_keys("123456")
browser.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[2]/div[3]/button").click()
time.sleep(3)
#begin to check work
browser.find_element_by_xpath("/html/body/div[4]/div[2]/div[1]/div[3]/button/span").click()
time.sleep(5)
#check
browser.find_element_by_xpath("/html/body/div[4]/div[2]/div[2]/div[3]/div/div[2]/div/div[1]/span[2]/span/ul/li[7]").click()
browser.find_element_by_id("questionSubmit").click()
time.sleep(0.5)
browser.find_element_by_id("questionSubmit").click()
