#8.	Transform the dataset to Min-Max Normalization
import math as m
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
file_path = r"C:\Users\yifru\OneDrive\Desktop\machine learning\worksheet three\iris\iris.data"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'Class']
data=pd.read_csv(file_path, names=names)
data2= (data.iloc[:,:-1])
print (data2.head())
print (data2.shape)
Scaler=MinMaxScaler()
ScaledData=Scaler.fit_transform (data2)
ScaledData=ScaledData.round(2)
print (ScaledData)
print (ScaledData.shape)
