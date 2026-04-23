import pandas as pd
import numpy as np
#Age={42, 15, 67, 55, 1, 29, 75, 89, 4, 10, 15, 38, 22, 77}
#Convert the given age value to the category of (‘Baby’, ‘Child’, ‘Teenage’, ‘Adult’, ‘Elderly’) suing binning method as cut value of [0, 3, 7, 17, 63, 99]
file_path = r"C:\Users\yifru\OneDrive\Desktop\machine learning\worksheet three\binning data.csv"
data=pd.read_csv(file_path)
print("Before: ")
print(data)
Label = pd.cut(x=data['Age'], bins=[0, 3, 7, 17, 63, 99],
                     labels=['Baby', 'Child', 'Teenage', 'Adult', 'Elderly'])
print("After: \n ", Label)
print("Categories: ")
print(Label.value_counts())
data = pd.concat([data, Label], axis=1)
print ("\n \n \n Merged Data \n \n", data)
