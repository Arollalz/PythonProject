# encoding: utf-8
import os
import time
import hashlib
import gl
from stringtorawstring import toraw
#
# oldPath = "D:\PenData\PenData1\敖翔\2015-2016学年下学期第5周周练_STUB2C99FD98C27458E82A8332AD2D87884\3.36.zip"
# mytoraw = toraw()
# print mytoraw._raw(oldPath)
# f = open(mytoraw._raw(oldPath).decode("utf-8").encode("gbk"), "rb")
# myBytes = f.read()
# # print myBytes
# m = hashlib.md5()
# m.update(myBytes)
# print m.hexdigest()
# print gl.result
def _readFileAndPutIntoGlVar(URL, Var):
    f = open(os.getcwd()+URL, "r")
    while True:
        line = f.readline()
        if line:
            Var.append(line.split(","))
        else:
            break
    f.close()
_readFileAndPutIntoGlVar("\DataForCreatingExamination.csv", gl.result)
print gl.result