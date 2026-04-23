import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
file_path = r"C:\Users\yifru\OneDrive\Desktop\machine learning\csv data collection\line chart data.csv"
df=pd.read_csv(file_path)
plt.plot(df['x'],df['y'])
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('line chart graph')
plt.show()