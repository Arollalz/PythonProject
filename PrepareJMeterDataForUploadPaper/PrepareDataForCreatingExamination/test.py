# encoding: utf-8
import os
import time
import hashlib
from stringtorawstring import toraw


# 2016-06-20 16:00:00

# # inpath = "D:\PenData\PenData1\敖翔\2015-2016学年下学期第5周周练_STUB2C99FD98C27458E82A8332AD2D87884\3.36.zip"
# # uipath = unicode(inpath, "utf-8")
# f = open("D:\PenData\PenData1\敖翔\\2015-2016学年下学期第5周周练_STUB2C99FD98C27458E82A8332AD2D87884\\3.36.zip", "rb")
# # coding=utf-8  os.path.normpath(path)

# path = os.path.normpath(r"D:\PenData\PenData1\敖翔\2015-2016学年下学期第5周周练_STUB2C99FD98C27458E82A8332AD2D87884\3.36.zip".decode("utf-8").encode("gbk"))
# print path.decode("gbk")
# print zipfile.is_zipfile(u"D:/PenData/PenData1/敖翔/2015-2016学年下学期第5周周练_STUB2C99FD98C27458E82A8332AD2D87884/3.37.zip")
# f = zipfile.ZipFile("E:/liuzhenWorkFile/Jean/performance/fromTK/liuzhen_script/creatExamination/Data/Data1/Data_50331859_42_505_0.zip".decode("utf-8").encode("gbk"), "r")
# string0 = f.read("Data_50331859_42_505_0.pen")
# m = hashlib.md5()
# m.update(string0)
# print m.hexdigest()

# 932c998fa67625c8ac46cabec375ee6a
# oldPath = os.path.normpath("D:\PenData\PenData1\敖翔\2015-2016学年下学期第5周周练_STUB2C99FD98C27458E82A8332AD2D87884\3.36.zip")
oldPath = "D:\PenData\PenData1\敖翔\2015-2016学年下学期第5周周练_STUB2C99FD98C27458E82A8332AD2D87884\3.36.zip"
# path = oldPath.replace("\\", "/")
# print path

mytoraw = toraw()
print mytoraw._raw(oldPath)
f = open(mytoraw._raw(oldPath).decode("utf-8").encode("gbk"), "rb")
# f = open("D:/PenData/PenData1/敖翔/2015-2016学年下学期第5周周练_STUB2C99FD98C27458E82A8332AD2D87884/3.37.zip".decode("utf-8").encode("gbk"), "rb")
myBytes = f.read()
# print myBytes
m = hashlib.md5()
m.update(myBytes)
print m.hexdigest()
