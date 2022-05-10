import pandas as pd
import numpy as np
missing_values = ["NAN","NA", "-", "Nil"]
df = pd.read_csv("https://raw.githubusercontent.com/cognizance-amrita/AI-Tasks/main/Q2-Dataset.csv", na_values = missing_values)
#missing values in each column
print(df.isnull().sum())
# total no:of missing values
print("Total number of missing values: ",df.isnull().sum().sum())

#Replace all the missing values according to each column
import pandas as pd
import numpy as np
missing_values = ["NAN","NA","-","Nil"]
df = pd.read_csv("https://raw.githubusercontent.com/cognizance-amrita/AI-Tasks/main/Q2-Dataset.csv",na_values = missing_values)
df['LotFrontage'].fillna(50, inplace=True)
df['Alley'].fillna('Pave', inplace=True)
df['BsmtQual'].fillna('Gd', inplace=True)
df['BsmtCond'].fillna('Gd', inplace=True)
df['BsmtExposure'].fillna('Mn', inplace=True)
df['BsmtFinType1'].fillna('ALQ',inplace=True)
df['BsmtFinType2'].fillna('Unf',inplace=True)
print(df.isnull().sum())

                          

