import datetime
from datetime import datetime, time, timedelta, date
currentDate=datetime.now()
print(currentDate)
print(currentDate.year)
print(currentDate.month)
print(currentDate.day)

myTime=time(14, 20, 30)
print(myTime)
print(myTime.hour)
print(myTime.minute)
print(myTime.second)

print(datetime(2024, 1, 1, 14, 20, 30))

print(timedelta(hours=5))
print(currentDate+timedelta(hours=5))