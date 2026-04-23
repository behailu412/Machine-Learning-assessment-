#9.	Transform the dataset to Z-Score Normalization
import pandas as pd
from sklearn.preprocessing import StandardScaler
# Load the dataset
file_path = r"C:\Users\yifru\OneDrive\Desktop\machine learning\worksheet three\iris\iris.data"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'Class']
scaler = StandardScaler()
data=pd.read_csv(file_path, names=names)
data2= (data.iloc[:,:-1])
normalized_data = scaler.fit_transform(data2)
print("Original data:\n \n \n", data2) # Flatten to print as 1D
print("Z-score normalized data (sklearn): \n \n \n", normalized_data)
