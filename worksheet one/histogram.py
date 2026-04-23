import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data=np.random.randn(1000)
plt.hist(data, bins=20, edgecolor='black')
plt.title ('Histogram of Randomly Generated Data')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()
