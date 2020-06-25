def seconds_format(seconds):
    hours = int(seconds/3600)
    minutes = int(seconds/60)%60
    seconds = seconds%60
    return "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)
    
print(seconds_format(31530))
print(seconds_format(18945))
print(seconds_format(3905))
print(seconds_format(213455))