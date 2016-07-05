# encoding: utf-8
import gl
from PrepareDataForCreatingExamination.sqlHandler import MySqlHandler
import hashlib
import csv
from stringtorawstring import toraw

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

# STEP_05
# ！！！！将stuLoginName, studentId, penSerialnumber, examId, MD5, zip包的个数写入csv格式的文件中, zip包路径
csvFile = file("upload.csv", "wb")
writer = csv.writer(csvFile)

mytoraw = toraw()

i = 0
for e in result:
    path = mytoraw._raw(e[3])
    try:
        f = open(path.decode(
            "utf-8").encode("gbk"), "rb")
    except UnicodeDecodeError:
        continue
    myBytes = f.read()
    m = hashlib.md5()
    m.update(myBytes)
    writer.writerow([e[0], e[4], e[1], e[2], m.hexdigest(), len(e[5]), e[3]])
    i += 1
csvFile.close()
