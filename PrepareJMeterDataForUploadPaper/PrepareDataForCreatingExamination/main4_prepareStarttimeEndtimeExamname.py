import csv
import time

count = 205
csvFile = file("upload2.csv", "wb")
writer = csv.writer(csvFile, delimiter="|")
start = time.time()
end = time.time() + 2

for i in range(0, count):
    starttime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(start + i*2))
    endtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(end + i*2))
    writer.writerow([starttime, endtime, "PERFORMANCE"+starttime])

csvFile.close()
