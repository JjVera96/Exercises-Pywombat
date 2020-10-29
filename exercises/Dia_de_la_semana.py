import calendar 

def day_of_week(day, month, year):
    return calendar.day_name[calendar.weekday(year, month, day)]

print(day_of_week(17, 8, 1993))
print(day_of_week(1, 1, 2000))
print(day_of_week(18, 11, 1995))
print(day_of_week(31, 12, 2019))