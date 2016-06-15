from witkeyuser import Witkeyuser
import os
import threading


f = open(os.getcwd()+"\selectWitkeyUserLoginNameAndPassword.csv")
print os.getcwd()
threads = []
for line in f.readlines():
    if line == "" or line == "\n":
        break
    name_password = line.split(',')
    print name_password

    t = Witkeyuser(name_password[0], name_password[1], 4)
    threads.append(t)
f.close()

for t in threads:
    t.start()
for t in threads:
    t.join()

# 18828078637
# 13438354577
# 13550384499
# 18602852536
# 18782967218
# 15982329128
# 18780165474
# 13618040690
# 13882162641
# 13666221984
# 13096323190
# 15882067658
# 15608018861
# 1820285009501
# 18190790927
# 18215552511
# user = Witkeyuser("15982329128", "123456", 4)
# user.run()
