import pandas as pd
file_path = r"C:\Users\yifru\OneDrive\Desktop\machine learning\worksheet three\encoding data.csv"
df = pd.read_csv(file_path)
df_encoded = pd.get_dummies(df, columns=['city'])
print(df_encoded)