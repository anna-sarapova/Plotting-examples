import numpy
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas

total_bars = 25
numpy.random.seed(total_bars)

dates = pandas.date_range('3/4/2020',
                          periods=total_bars,
                          freq='m')
# periods - Number of periods to generate
# freq - default ‘D’ -  strings frequency

diff = pandas.DataFrame(
    data=numpy.random.randn(total_bars),
    index=dates,
    columns=['A']
)

figure, axes = plt.subplots(figsize=(10, 6))

axes.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))

axes.bar(diff.index,
         diff['A'],
         width=25,
         align='center')

plt.show()