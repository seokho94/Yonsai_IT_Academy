from datetime import datetime

now = datetime.now()
hour = now.hour
min = now.minute
sec = now.second

print("{} : {} : {}".format(hour, min, sec))

print(type(hour))
print(type(min))