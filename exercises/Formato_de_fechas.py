# https://pywombat.com/my/exercises/0bf62e7a

from datetime import datetime

if __name__ == '__main__':
    now = datetime.now()
    print(now.strftime('%Y-%m-%d %H:%M:%S'))
