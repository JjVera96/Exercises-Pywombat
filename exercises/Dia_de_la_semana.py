# https://pywombat.com/my/exercises/32cfae25

import calendar 

def day_of_week(day, month, year):
    days_spanish = {
        'Monday': 'Lunes',
        'Tuesday': 'Martes',
        'Wednesday': 'Miercoles',
        'Thursday': 'Jueves',
        'Friday': 'Viernes',
        'Saturday': 'Sabado',
        'Sunday': 'Domingo',
    }
    return days_spanish[calendar.day_name[calendar.weekday(year, month, day)]]

print(day_of_week(17, 8, 1993))
print(day_of_week(1, 1, 2000))
print(day_of_week(18, 11, 1995))
print(day_of_week(31, 12, 2019))