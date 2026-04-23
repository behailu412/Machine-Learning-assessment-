import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
file_path = r"C:\Users\yifru\OneDrive\Desktop\machine learning\csv data collection\bar graph data.csv"
data=pd.read_csv(file_path)
plt.xlabel('Department')
plt.ylabel('Number of Students')
plt.bar(data['dept'],data['stu'], color=('red','green','blue','yellow','orange'))
plt.show()