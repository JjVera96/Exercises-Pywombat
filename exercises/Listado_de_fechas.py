import datetime
import time 


f = open('dates.txt','a')
while True:
    now = datetime.datetime.now()
    f.write('{}\n'.format(now.strftime('%Y-%M-%d %H:%M:%S')))
    time.sleep(1)
f.close()
