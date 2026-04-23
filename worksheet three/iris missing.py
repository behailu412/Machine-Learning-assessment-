#1.	Deliberately change the value of data to missing value in each feature of the dataset
import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer, KNNImputer
# Load the dataset
file_path = r"C:\Users\yifru\OneDrive\Desktop\machine learning\worksheet three\iris\iris.data"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'Class']
data11=pd.read_csv(file_path, names=names)
iris_df = data11
iris_df=iris_df.iloc[:,:-1]
# Introduce some artificial missing values for demonstration
# In a real scenario, your data would already have NaNs
np.random.seed(42) # for reproducibility
for col in iris_df.columns:
    missing_indices = np.random.choice(iris_df.index, size=10, replace=False)
    iris_df.loc[missing_indices, col] = np.nan
print("DataFrame with missing values:")
print(iris_df)


#2.	Impute the missing value data with mean value of the corresponding feature value
print("\nMissing values before imputation:")
print(iris_df.isnull().sum())
for col in iris_df.columns:
    mean_value = iris_df[col].mean()
    iris_df[col].fillna(mean_value, inplace=True)
print("\nDataFrame after mean imputation:")
print(iris_df.head())
print("\nMissing values after imputation:")
print(iris_df.isnull().sum())
print(data11.iloc[:,4])
iris_df['Class']=data11.iloc[:,4]
print(iris_df)

#3.	Adjust the precision to 2 round off. 
# code to round ofto 2 decimal place
iris_df=iris_df.round(3)
print(iris_df)
data=np.concatenate((iris_df,data11),axis=1)
print(data)

#4.	Impute the missing value data with most frequent value of the corresponding feature
data2=iris_df.copy()
print (data2.tail())
print (round(data2.isnull().sum(), 2).sort_values(ascending=False))
imp_mode=imputer = SimpleImputer(strategy='most_frequent')
imp_mode.fit(data2)
data2=imp_mode.transform(data2)
print (data2)


#5.	Impute the missing value data with a constant value 100 to every corresponding feature
#  Imputation with constant vales
data2=iris_df.copy()
print (data2.tail())
print (round(data2.isnull().sum(), 2).sort_values(ascending=False))
imputer = SimpleImputer(strategy='constant', fill_value=100)
imp_cons=imputer
imp_cons.fit(data2)
data2=imp_cons.transform(data2)
print (data2)

#6.	Impute the missing value data with KNN where N=2
#  Imputation with nearest values
data=iris_df.copy()
data2= (data.iloc[:,:-1])
# creating a data frame from the list
Before_imputation = data2
#print dataset before imputation
print("Data Before performing imputation\n",Before_imputation)
# create an object for KNNImputer
imputer = KNNImputer(n_neighbors=2)
After_imputation = imputer.fit_transform(Before_imputation)
# print dataset after performing the operation
print("\n\nAfter performing imputation\n",After_imputation)


#7.	delete records of dataset with missing values 
#  deletion of records with missing values
data=iris_df.copy()
data2= (data.iloc[:,:-1])
print (len(data2))
data2 = data2.dropna() # drop rows with nan values
print (data2.isnull().sum())
print (data2)
print (data2.isnull().sum())
print (data2)

