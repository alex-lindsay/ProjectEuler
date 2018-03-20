import datetime

startDate  = datetime.date(1901, 1, 1)
endDate = datetime.date(2000, 12, 31)
oneWeek = datetime.timedelta(days=7)

curDate = startDate
print(curDate, curDate.weekday())
#move to first Sunday
daysToSunday = datetime.timedelta(days=6-curDate.weekday())
curDate += daysToSunday
print(curDate, curDate.weekday())
countOfSundays = 0

while curDate < endDate:
    if curDate.day == 1:
        countOfSundays += 1
    curDate += oneWeek

print(curDate, curDate.weekday(), countOfSundays)
