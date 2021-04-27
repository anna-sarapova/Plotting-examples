import pandas as pd
from datetime import datetime, timedelta
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates

plt.style.use('seaborn')

dates = [
    datetime(2021, 5, 24),
    datetime(2021, 6, 24),
    datetime(2021, 7, 24),
    datetime(2021, 8, 24),
    datetime(2021, 9, 24),
    datetime(2021, 10, 24),
    datetime(2021, 11, 24)
]
""" dates and y must have the same length of array elements"""
y = [0, 4, 2, 3, 6, 8, 5]
plt.plot_date(dates, y, linestyle='solid', color='#003f5c')
""" linestyle - units the points of data with a line"""
"""plot_date - function that plots the chart in the data format"""
plt.title('Date format chart')
plt.xlabel('Date')
plt.ylabel('Random points')


plt.tight_layout()
"""makes the chart look smaller"""

plt.gcf().autofmt_xdate()
"""above function show the full date on X-axis 
(dates are rotated and have different alignment) """

date_format = mpl_dates.DateFormatter('%b, %d %Y')
""" %b - month, %d - day, %Y - year"""

plt.gca().xaxis.set_major_formatter(date_format)
"""format the dates in the form of "Mar, 24 2021" 
as specified in date_format"""

plt.show()
