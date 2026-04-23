import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
data = [np.random.normal(0, std, 100) for std in range(1, 4)]
data
sns.boxplot(data=data)
plt.title ('Boxplot')
plt.xlabel('Category')
plt.ylabel('Values')
plt.show()
