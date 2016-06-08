from witkeyuser import Witkeyuser
import os
import threading


f = open(os.getcwd()+"\selectWitkeyUserLoginNameAndPassword.csv")
print os.getcwd()
threads = []
for line in f.readlines():
    if line == "" or line == "\n":
        break
    print line
    name_password = line.split(',')
    print name_password

    t = Witkeyuser(name_password[0], name_password[1], 4)
    threads.append(t)
f.close()

for t in threads:
    t.start()
for t in threads:
    t.join()

# 13438354577,123456
# 18782967218,123456
# 18583750817,123456
# 15196775582,123456
# 18780165474,123456
# 13618040690,123456
# 13882162641,123456
# 13666221984,123456
# 15882067658,123456
# 18215679921,123456
# 18202824902,123456
# 18602878213,123456
# 18190790927,123456
# 18202850095,123456
# 18675503875,123456
user = Witkeyuser("13438354577", "123456", 4)
user.checkTask()
