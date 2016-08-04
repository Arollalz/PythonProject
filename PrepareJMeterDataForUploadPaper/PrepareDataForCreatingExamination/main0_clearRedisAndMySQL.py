# encoding: utf-8
import MySQLdb
# 改MySQL状态
createTime = '2014-06-23 10:00:00'

conn = MySQLdb.connect(
    host='172.16.6.20',
    port=3306,
    user='admin',
    passwd='123456',
    db='smartmatch'
)
cur = conn.cursor()
query = """update exam_summary set examState = 6 where createTime > (%s);
        update examination set examState = 6 where createTime > (%s);
        update examdetail set examState = 6 where createTime > (%s);
        update penuse set status = 6 where createTime >(%s);"""

queryResult = cur.execute(query, (createTime, createTime, createTime, createTime))

result = cur.fetchmany(queryResult)
print result

#清Redis




