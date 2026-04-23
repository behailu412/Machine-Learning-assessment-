import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
file_path = r"C:\Users\yifru\OneDrive\Desktop\machine learning\csv data collection\area chart data.csv"
Data=pd.read_csv(file_path)
plt.fill_between(Data['x'], Data['y1'], Data['y2'], color='skyblue', alpha=0.4)
plt.title('Area Chart')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.show()
