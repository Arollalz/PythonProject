# encoding: utf-8
import os
import time
# 2016-06-20 16:00:00
print time.time()
print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
time.sleep(1)
print time.time()
print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
