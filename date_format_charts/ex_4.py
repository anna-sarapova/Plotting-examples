import matplotlib
import matplotlib.pyplot as plt
from datetime import datetime

origin = ['2020-02-05 17:17:55',
          '2020-02-05 17:17:51',
          '2020-02-05 17:17:49']

a = [datetime.strptime(d, '%Y-%m-%d %H:%M:%S') for d in origin]
# strptime() - parse 2-digit years when given %y format code.
# When 2-digit years are parsed, they are converted into standard

b = ['35.764299', '20.3008', '36.94704']

x = matplotlib.dates.date2num(a)
# date2num - Convert datetime objects to Matplotlib dates
formatter = matplotlib.dates.DateFormatter('%H:%M:%S')

figure = plt.figure()
axes = figure.add_subplot(1, 1, 1)

axes.xaxis.set_major_formatter(formatter)
plt.setp(axes.get_xticklabels(), rotation=15)

axes.plot(x, b)
plt.show()