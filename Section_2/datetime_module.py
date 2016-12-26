#
import datetime

d = datetime.date(2012, 12, 14)
print(d.year)
print(d.month)
print(d.day)

print(datetime.date.today())
print(datetime.datetime.today())

#strftime allows us to format dates/datetimes
print(datetime.datetime.today().strftime('%m/%d/%Y'))
print(datetime.datetime.today().strftime('%Y-%m-%d-%H.%M.%S'))

#timedelta represents the difference between two dates or times
now = datetime.datetime.now()
then = datetime.datetime(2012, 12, 14)
delta = now - then
print(type(delta))
print(delta.days)
print(delta.seconds)
