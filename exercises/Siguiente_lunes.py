# https://pywombat.com/my/exercises/5a0fc6ba

from datetime import datetime
from datetime import timedelta

if __name__ == '__main__':
    day = datetime.today().weekday()
    date = datetime.now() + timedelta(days=8-day)
    print(date.date())