import calendar

def getDatesDay(day, month, year):
    day -= 1
    date_days = []
    c = calendar.monthcalendar(year, month)
    for week in c:
        if week[day]:
            date_days.append('{}-{:0>2}-{:0>2}'.format(year, month, week[day]))
    return date_days
    
print(getDatesDay(2, 8, 2020))