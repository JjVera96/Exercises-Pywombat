from datetime import datetime

now = datetime.now()
name = "{}_pywombat.txt".format(now.strftime("%Y_%m_%d"))
f = open(name, "w")
f.close()