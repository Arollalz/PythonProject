# encoding: gbk
import gl
from PrepareDataForCreatingExamination.sqlHandler import MySqlHandler
import hashlib
import csv
from stringtorawstring import toraw
import os

# write data to gl
# result = []
# paperDataInfo = []
# createtime = []

def _readFileAndPutIntoGlVar(URL, Var):
    f = open(os.getcwd()+URL, "r")
    while True:
        line = f.readline()
        if line:
            if line.find(",") != -1:
                Var.append(line.split(","))
            else:
                print "-----"
                Var.append(line)
        else:
            break
    f.close()


_readFileAndPutIntoGlVar("\DataForCreatingExamination.csv", gl.result)
_readFileAndPutIntoGlVar("\paperDataInfo.csv", gl.paperDataInfo)
_readFileAndPutIntoGlVar("\CreateTime.csv", gl.createtime)

print gl.createtime
# STEP_04
# 得到学生上传时需要的数据，stuLoginName, studentId, penSerialnumber, examId, MD5, zip包的个数
# stuLoginName <-- edu_auth.account 查表
# studentId <-- gl.paperDataInfo
# penSerialnumber <-- 查表
# examId <-- 查表 用examName，PaperId 查询 gl.result
# MD5 <-- 用hashlib生成 需要zip包路径 转换为String 然后
# zip包个数 <-- gl.paperDataInfo中License的长度
# 联合查询涉及的表  edu_auth.account, penuse，pen, student
mySqlHandler = MySqlHandler(gl.paperDataInfo)
# RESULT: 0.edu_auth.account.loginName, 1.pen.serialNum, 2.penuse.examId, 3.zip包的路径，4.StuId，5.License
result = mySqlHandler.getResult2()

# print "result:", result
# STEP_05
# ！！！！将stuLoginName, studentId, penSerialnumber, examId, MD5, zip包的个数写入csv格式的文件中, zip包路径, License
csvFile = file("upload.csv", "wb")
writer = csv.writer(csvFile, delimiter="|")

mytoraw = toraw()

i = 0
for e in result:
    md5s = []
    pathes = []
    for e0 in e[5]:
        oldPath = e[3]+"\\" + e0 + ".zip"
        # print "oldpath",oldPath
        path = mytoraw._raw(oldPath)
        #print "path", path
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
csvFile.close()

