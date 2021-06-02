from datetime import datetime
from datetime import timedelta

if __name__ == '__main__':
    date = datetime(year=2021, month=6, day=3, hour=10)
    utc = int(input('UTC: '))
    result = date + timedelta(hours=utc)
    print(result.strftime("%A %H:%M"))