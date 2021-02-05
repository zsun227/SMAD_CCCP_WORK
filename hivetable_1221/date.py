import sys
from datetime import datetime

timestamp = int(sys.argv[1].split('-')[1])
dates = datetime.fromtimestamp(timestamp / 1e3)

year, month, day, hour = dates.year, dates.month, dates.day, dates.hour
index = int(sys.argv[1].split('-')[2])
f1 = open('tmp_year.txt', 'w')
f2 = open('tmp_month.txt', 'w')
f3 = open('tmp_day.txt', 'w')
f4 = open('tmp_hour.txt', 'w')
f5 = open('tmp_index.txt', 'w')

f1.write('%d' % year)
f1.close()

f2.write('%d' % month)
f2.close()

f3.write('%d' % day)
f3.close()

f4.write('%d' % hour)
f4.close()

f5.write('%d' % index)
f5.close()
