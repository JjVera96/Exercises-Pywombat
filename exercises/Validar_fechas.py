import re

def date_is_valid(str_date):
    if re.match('[0-9]{4}-[0-9]{2}-[0-9]{2}', str_date): return True
    return False 


print(date_is_valid("2020-01-31"))
print(date_is_valid("220-01-31"))