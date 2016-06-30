# encoding: utf-8
from PrepareDataForCreatingExamination.parser import Parsependata
from PrepareDataForCreatingExamination.sqlHandler import MySqlHandler
import csv
import time

# 解析线上下载下来的PenData数据，获得每份笔迹的信息：zip包的路径，StuId，License
myParser = Parsependata("E:\PenData")
paperDataInfo = myParser.getPaperDataInfo()

# 通过查询MySQL
# 根据StuId获得ClassId和老师的TeacherLoginName
# 根据License获得PaperId
# Q:一个License获得多个PaperId怎么办，可否通过多个License查询出唯一的PaperId？
# 将得到的[TeacherLoginName，ClassId，PaperId]放入列表中
# 注意去重
mySqlHandler = MySqlHandler(paperDataInfo)
result = mySqlHandler.getResult()

# 将TeacherLoginName,ClassId,PaperId,StartTime,EndTime,ExamName写入csv格式的文件中
csvFile = file("DataForCreatingExamination.csv", "wb")
writer = csv.writer(csvFile)
twoHoursAgo = time.time() - 2 * 60 * 60
examNamePrefix = "LZ_PERFORMANCE_"
i = 0
for e in result:
    writer.writerow([e[0], e[1], e[2],
                    time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(twoHoursAgo + i * 2)),
                    time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(twoHoursAgo + i * 2 + 2)),
                    examNamePrefix+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(twoHoursAgo + i * 2))])
    i += 1

csvFile.close()
