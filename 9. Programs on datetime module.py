import datetime

# d = datetime.date(2019, 12, 25)
# print (d)


tday= datetime.date.today()
print('Today is: ', tday)
# print(tday.weekday()) #to print which day is today in week
# #
# print((tday.isoweekday()))
#
# #date after one week from now
# tdelta = datetime.timedelta(days=7)
# print(tdelta)
# print(tday + tdelta)
#
# bday = datetime.date(1995, 4, 17)
# till_bday = tday - bday
# print(till_bday)
# print(till_bday.total_seconds())

# datetime for all data
# dt = datetime.datetime(2017, 8, 29, 12, 20, 100000)
# print(dt)

t = datetime.time(9, 30, 45, 100000)
print(t)
