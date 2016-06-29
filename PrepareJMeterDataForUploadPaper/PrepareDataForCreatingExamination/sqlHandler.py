import MySQLdb
from PrepareDataForCreatingExamination.parser import Parsependata


class MySqlHandler:
    def __init__(self, data):
        self.paperDataInfo = data

    def getResult(self):
        conn = MySQLdb.connect(
            host='172.16.8.11',
            port=3306,
            user='admin',
            passwd='123456',
            db='smartmatch'
        )

        cur = conn.cursor()
        i = 0

        stringWHERE = "FALSE"
        studentIds = []
        numOfStu = len(self.paperDataInfo)
        while numOfStu > 0:
            stringWHERE += " OR (student.studentId = (%s) AND penlicense_use.license = (%s))"
            numOfStu -= 1

        for e1 in self.paperDataInfo:
            studentIds.append((e1[1]))
            studentIds.append((e1[2][0]))

        query = """SELECT DISTINCT edu_auth.account.loginName, student.currClassId, penlicense_use.paperId
                                FROM (((student JOIN class
                                ON student.currClassId = class.classId ) JOIN teacher
                                ON teacher.teacherId = class.masterTeacherId) JOIN edu_auth.account
                                ON edu_auth.account.accountId = teacher.accountId JOIN penlicense_use
                                ON TRUE
                                ) WHERE """ + stringWHERE

        # print query #TEST
        queryResult = cur.execute(query, studentIds)

        resultInfo = cur.fetchmany(queryResult)
        # for e2 in resultInfo:
        #     i += 1
        #     print e2

        # print i
        # print resultInfo
        return resultInfo
