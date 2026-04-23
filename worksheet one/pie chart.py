import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
file_path = r"C:\Users\yifru\OneDrive\Desktop\machine learning\csv data collection\bar graph data.csv"
data=pd.read_csv(file_path)
plt.title('pie chart analaysis')
plt.pie(data['stu'],labels=data['dept'], autopct='%.2f')
plt.show()