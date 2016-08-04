# encoding: gbk
import MySQLdb
import gl
import config
import os



class MySqlHandler:
    def __init__(self, data1=None, data2=None):
        self.paperDataInfo = data1
        self.exerciseDataInfo = data2

    def _readFileAndPutIntoGlVar(self,URL, Var):
        f = open(os.getcwd() + URL, "r")
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

    # loginname, studentid, serialnumber, examid1111, MD5, zipcount, datapath, licenses

    def getResult0(self):
        conn = MySQLdb.connect(
            host = '172.16.6.20',
            port = 3306,
            user = 'admin',
            passwd = '123456',
            db = 'smartmatch'
        )
        cur = conn.cursor()
        query = """SELECT DISTINCT edu_auth.account.loginName,pen.serialNum
                FROM pen JOIN student ON pen.studentId = student.studentId
                JOIN edu_auth.account ON student.accountId = edu_auth.account.accountId
                WHERE student.studentId = (%s)"""
        resultInfo = []
        for e in self.exerciseDataInfo:
            # print e
            # print e[0]
            # print e[1]
            tempArray = []
            tempStr = e[2:]
            # print "====", tempStr[0]
            tempArray = tempStr[0]
            # for e0 in tempStr:
            #     tempArray.append(e0[e0.find("\'") + 1:e0.rfind("\'")])
            # print "tempArray", tempArray #TEST
            # print e[3][1:]
            # print e[4][1:-3]
            # print gl.createtime[0]
            queryResult = cur.execute(query, (e[1],))
            result = cur.fetchmany(queryResult)
            # print result
            # 0.edu_auth.account.loginName,1. pen.serialNum, 2.penuse.examId,zip包的路径，3.StuId, Lincense
            try:
                resultInfo.append((result[0][0], result[0][1], "", e[0], e[1], tempArray))
            except IndexError:
                continue
        # i = 0
        # for e2 in resultInfo:
        #     i += 1
        #     print e2
        #
        # print i
        # print resultInfo
        cur.close()
        conn.close()
        return resultInfo


    def getResult1(self):
        conn = MySQLdb.connect(
            host = '172.16.6.20',
            port = 3306,
            user = 'admin',
            passwd = '123456',
            db = 'smartmatch'
        )

        cur = conn.cursor()
        i = 0

        stringWHERE = "FALSE"
        studentIds = []
        numOfStu = len(self.paperDataInfo)
        while numOfStu > 0:
            stringWHERE += " OR (penlicense_use.paperType = 'exampaper' AND student.studentId = (%s) AND penlicense_use.license = (%s))"
            numOfStu -= 1

        for e1 in self.paperDataInfo:
            print "students..."
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
        self._readFileAndPutIntoGlVar("\CreateTime.csv", gl.createtime)
        conn = MySQLdb.connect(
            host = '172.16.6.20',
            port = 3306,
            user = 'admin',
            passwd = '123456',
            db = 'smartmatch'
        )

        cur = conn.cursor()

        # query = """SELECT DISTINCT edu_auth.account.loginName, pen.serialNum, penuse.examId
        #     FROM  penuse JOIN pen ON penuse.studentId=pen.studentId
        #     JOIN student ON student.studentId = penuse.studentId
        #     JOIN edu_auth.account ON student.accountId = edu_auth.account.accountId
        #     JOIN penlicense_use ON penlicense_use.paperId = penuse.paperId
		 #     JOIN examination ON penuse.paperId = examination.paperId
        #     WHERE examination.examName LIKE (%s)  AND penlicense_use.license = (%s) AND penuse.createTime > (%s) AND student.studentId = (%s)"""
        # query0 = """SELECT * FROM school
        #         JOIN student ON school.schoolId = student.currSchoolId
        #         WHERE school.`name` IN ("演示学校","2C测试学校","a1新建学校","魔法学校","部署测试","测试学校","111","11","聚云浩海","启航新课堂八年级下","天府前沿八年级下","天府前沿7年级下")
        #         AND student.studentId = (%s);"""

        query = """SELECT DISTINCT edu_auth.account.loginName, pen.serialNum, penuse.examId
                    FROM  penuse JOIN pen ON penuse.studentId=pen.studentId
                    JOIN student ON student.studentId = penuse.studentId
                    JOIN edu_auth.account ON student.accountId = edu_auth.account.accountId
                    JOIN penlicense_use ON penlicense_use.paperId = penuse.paperId
        		      JOIN examination ON penuse.examId = examination.examId
                    WHERE penuse.service = 'exam' AND penuse.classId = student.currClassId AND examination.examName LIKE (%s)  AND penlicense_use.license = (%s) AND penuse.createTime > (%s) AND student.studentId = (%s)"""

        #  self.paperDataInfo -> zip包的路径，StuId，License
        #  self.data2 -> TeacherLoginName，ClassId，PaperId
        resultInfo = []
        for e in self.paperDataInfo:
            # print e
            # print e[0]
            # print e[1]
            tempArray = []
            tempStr = e[2:]
            for e0 in tempStr:
                tempArray.append(e0[e0.find("\'")+1:e0.rfind("\'")])
            # print "tempArray", tempArray #TEST
            # print e[3][1:]
            # print e[4][1:-3]
            # print gl.createtime[0]
            myVars = []
            likePartern = "PERFORMANCE"+"%"
            myVars.append(likePartern)
            if len(e) == 3:
                myVars.append((e[2][2:-3]))
            else:
                myVars.append((e[2][3:-1]))
            myVars.append((gl.createtime[0][0:-1]))
            myVars.append((e[1]))
            print myVars

            # query0Result = cur.execute(query0, ((e[1]),))
            # result0 = cur.fetchmany(query0Result)
            #
            # if result0 != ():
            #     print "=============", result0
            #     break

            queryResult = cur.execute(query, myVars)
            result = cur.fetchmany(queryResult)
            if result == ():
                continue
            else:
                try:
                    resultInfo.append((result[0][0], result[0][1], result[0][2], e[0], e[1], tempArray))
                except IndexError:
                    continue
             # print result
            #0.edu_auth.account.loginName,1. pen.serialNum, 2.penuse.examId,zip包的路径，3.StuId, Lincense

        # for e2 in resultInfo:
        #     i += 1
        #     print e2

        # print i
        # print "============", len(resultInfo)
        cur.close()
        conn.close()
        return resultInfo



