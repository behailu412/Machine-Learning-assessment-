import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
file_path = r"C:\Users\yifru\OneDrive\Desktop\machine learning\csv data collection\radar chart data.csv"
data1=pd.read_csv(file_path)
labels=data1['dept']
data=data1['instractor']

# Create a polar plot
plt.polar(labels, data, color='blue', linewidth=2)

# Add a title
plt.title("Polar Plot Example")

# Display the plot
plt.show()
