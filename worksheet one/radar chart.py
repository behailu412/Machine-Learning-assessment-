import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
file_path = r"C:\Users\yifru\OneDrive\Desktop\machine learning\csv data collection\radar chart data.csv"
data1=pd.read_csv(file_path)
labels=data1['dept']
data=data1['instractor']
angles=np.linspace(0, 1.5* np.pi, len(labels), endpoint=False)
data=np.concatenate((data,[data[0]]))
angles=np.concatenate((angles, [angles[0]]))
"""plt.polar (angles,data, marker='o')"""
plt.polar (angles,data)
plt.fill(angles, data, alpha=0.5)
plt.title('Radar Chart')
plt.legend()
plt.show()
