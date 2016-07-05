# coding=utf-8
import MySQLdb
import gl


class MySqlHandler:
    def __init__(self, data1):
        self.paperDataInfo = data1

    def getResult1(self):
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
        for e2 in resultInfo:
            i += 1
            print e2

        print i
        # print resultInfo
        cur.close()
        conn.close()
        return resultInfo

    def getResult2(self):
        conn = MySQLdb.connect(
            host='172.16.8.11',
            port=3306,
            user='admin',
            passwd='123456',
            db='smartmatch'
        )

        cur = conn.cursor()

        query = """SELECT DISTINCT edu_auth.account.loginName, pen.serialNum, penuse.examId
            FROM  penuse JOIN pen ON penuse.studentId=pen.studentId
            JOIN student ON student.studentId = penuse.studentId
            JOIN edu_auth.account ON student.accountId = edu_auth.account.accountId
            JOIN penlicense_use ON penlicense_use.paperId = penuse.paperId
		     JOIN examination ON penuse.paperId = examination.paperId
            WHERE examination.examName LIKE "%LZ_PERFORMANCE_%" AND penlicense_use.license = (s%) AND penuse.createTime > (s%) AND student.studentId = (s%)"""

        #  self.paperDataInfo -> zip包的路径，StuId，License
        #  self.data2 -> TeacherLoginName，ClassId，PaperId
        resultInfo = []
        for e in self.paperDataInfo:
            queryResult = cur.execute(query, [(e[2]),(gl.createtime),(e[1])])
            result = cur.fetchmany(queryResult)
            #edu_auth.account.loginName, pen.serialNum, penuse.examId,zip包的路径，StuId, Lincense
            resultInfo.append((result[0], result[1], result[2], e[0], e[1], e[2]))
        # for e2 in resultInfo:
        #     i += 1
        #     print e2

        # print i
        # print resultInfo
        cur.close()
        conn.close()
        return resultInfo



