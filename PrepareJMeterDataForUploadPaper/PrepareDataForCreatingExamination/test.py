# encoding: utf-8
import os
for root, sub_dirs, files in os.walk("E:\PenData"):
    print root
    print sub_dirs
    print files