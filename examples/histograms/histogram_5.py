import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-white')

data = np.random.randn(1000)
plt.hist(data, bins=100, alpha=0.7,
         histtype='stepfilled', color='steelblue',
         edgecolor='none');
plt.show()