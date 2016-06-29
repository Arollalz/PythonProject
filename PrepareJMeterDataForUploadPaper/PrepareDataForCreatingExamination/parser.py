# encoding: utf-8
import os

class Parsependata:
    def __init__(self, path):
        self.path = path

    # zip包的路径，stuId，license
    def getPaperDataInfo(self):
        pendataInfo = []
        for root, sub_dirs, files in os.walk(self.path):
            if len(files) and (root.find("null") == -1) and (root.find("练习") == -1):
                zipPath = root
                stuId = root[root.find("STU"):]
                licenses =[]
                for e in files:
                    licenses.append(e[0:e.find(".zip")])

                pendataInfo.append([zipPath, stuId, licenses])

        #TEST-start
        num = 1
        for e in pendataInfo:
            print num
            print e[0]
            print e[1]
            print e[2]
            num += 1
        #TEST-end

        return pendataInfo









