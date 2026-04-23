import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
data = [np.random.normal(0, std, 100) for std in range(1, 6)]
data
sns.violinplot(data=data)
plt.title ('Violinplot')
plt.xlabel('Category')
plt.ylabel('Values')
plt.show()
