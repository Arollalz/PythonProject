# encoding: gbk
from PrepareDataForCreatingExamination.parser import Parsependata
from PrepareDataForCreatingExamination.sqlHandler import MySqlHandler
import csv
import time
from PrepareDataForCreatingExamination import gl
import config
from stringtorawstring import toraw
import hashlib

# STEP_01
# 解析线上下载下来的PenData数据，获得每份笔迹的信息：zip包的路径，StuId，License
myParser = Parsependata(config.PENFILE)
exerciseDataInfo = myParser.getExerciseDataInfo()

csvPaperDataInfo = file("exerciseDataInfo.csv", "wb")

exerciseDataInfoWriter = csv.writer(csvPaperDataInfo)
for e in exerciseDataInfo:
    exerciseDataInfoWriter.writerow([e[0], e[1], e[2]])
csvPaperDataInfo.close()

# STEP_02
# loginname,studentid,serialnumber,examid1111,MD5,zipcount,datapath,licenses
mySqlHandler = MySqlHandler(data2=exerciseDataInfo)
result = mySqlHandler.getResult0()


#STEP_03
csvUploadExercise = file("uploadExercise.csv", "wb")
writer = csv.writer(csvUploadExercise, delimiter="|")

mytoraw = toraw()

i = 0
for e in result:
    md5s = []
    pathes = []
    for e0 in e[5]:
        oldPath = e[3]+"\\" + e0 + ".zip"
        # print "oldpath",oldPath
        path = mytoraw._raw(oldPath)
        print "path", path
        try:
            f = open(path, "rb")
        except UnicodeDecodeError:
            print "continue"
            continue
        myBytes = f.read()
        m = hashlib.md5()
        m.update(myBytes)
        md5s.append(m.hexdigest())
        pathes.append(path)

    writer.writerow([e[0], e[4], e[1], e[2], ",".join(md5s), len(e[5]), ",".join(pathes), ",".join(e[5])])
    i += 1
print i
csvUploadExercise.close()

