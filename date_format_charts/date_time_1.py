from datetime import datetime, timedelta
from matplotlib import pyplot as plt

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

y = [0, 4, 2, 3, 6, 8, 5]
plt.plot_date(dates, y) # plots the chart in the data format

plt.tight_layout() # makes the chart look smaller
plt.show()
