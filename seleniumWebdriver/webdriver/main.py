from witkeyuser import Witkeyuser
import os
import threading


# f = open(os.getcwd()+"\selectWitkeyUserLoginNameAndPassword.csv")
# print os.getcwd()
# threads = []
# for line in f.readlines():
#     print line
#     name_password = line.split(',')
#     print name_password
#     #create a lock
#     mutex = threading.Lock()
#     t = threading.Thread(target=Witkeyuser(name_password[0], name_password[1], 10).checkTask())
#     threads.append(t)
# f.close()
#
# for t in threads:
#     t.setDeamon(True)
#     t.start()

# 13438354577
# 15196775582
# 18202824902
# 18602852536
# 18782967218
# 13618040690
# 13096323190
user = Witkeyuser("18602852536", "123456", 4)
user.checkTask()
