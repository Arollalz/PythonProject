from witkeyuser import Witkeyuser
import os
# f = open(os.getcwd()+"\selectWitkeyUserLoginNameAndPassword.csv")
# print os.getcwd()
# for line in f.readlines():
#     print line
#     name_password = line.split(',')
#     print name_password
#     user = Witkeyuser(name_password[0], name_password[1], 10000)
#     user.checkTask()
# f.close()


user = Witkeyuser("18780165474", "123456", 4)
user.checkTask()
