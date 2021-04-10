import matplotlib.pyplot as plt

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
sizes = [15, 30, 45, 10]
explode = (0, 0.1, 0, 0)
# only "explode" the 2nd slice (i.e. 'Hogs')
# explode - means that a part will be emphasised

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels,
        autopct='%1.1f%%', # - shows in percent data
        shadow=True, startangle=90)
ax1.axis('equal')
# Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()
