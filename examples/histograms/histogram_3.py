import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-white')

data = np.random.randn(1000)
plt.hist(data, bins=30, density=True,
         orientation='horizontal',
         log=True,
         color='steelblue', alpha=0.5,
         edgecolor='none');
plt.show()
