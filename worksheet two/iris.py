import pandas as pd
from matplotlib import pyplot
#pip install scipy
#from scipy.stats import gaussian_kde
file_path = r"C:\Users\yifru\OneDrive\Desktop\machine learning\worksheet two\iris\iris.data"

names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'Class']

data = pd.read_csv(file_path, names=names)

#3 Code to display the number of rows and columns of data:
print("\n", data.shape)

#4 Code to display the first five records of data:
print ("\n", data.head())

#5 Code to display the last five records of data:
print ("\n", data.tail ())

#6 Code to display the first ten records of data:
print ("\n", data[:10])

#7 Code to describe the dataset interms of mean, standard deviation, minimum value
# maximum value, 1st Quadrant, 3rd Quadrant:
print ("\n", data.describe())

#8 Code to display the count of records in each classs label:
print ("\n The number of each class", data['Class'].value_counts())

#9. code to Extract the independent features from the dataset
print (data.iloc[:,:-1].values)

#10. code to  Extract the value of the class label of the dataset
print (data.iloc[:,4].values)

#11 Code to Generate Histogram graph for each feature of the dataset
data.hist()
pyplot.show()

#12.  Code to Generate Density graph plot for each feature of the dataset
data.plot(kind='density', subplots=True, layout=(2,2), sharex=False)
pyplot.show()

#13.  Code to Generate boxplot graph plot for each feature of the dataset
data.plot(kind='box', subplots=True, layout=(2,2), sharex=False,sharey=False)
pyplot.show()
