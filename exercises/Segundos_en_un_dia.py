import datetime

now = datetime.datetime.now()
tomorrow = now + datetime.timedelta(days=1)
diff = tomorrow - now
print('Existen {} segundos en un día.'.format(int(diff.total_seconds())))
