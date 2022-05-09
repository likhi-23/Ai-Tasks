Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import matplotlib.pyplot as plt
>>> import pandas as pd
>>> data = pd.read_csv(r'C:\Users\karri\Downloads\Q5.csv')
>>> df = pd.DataFrame(data)
>>> X = list(df.iloc[:,0])
>>> Y = list(df.iloc[:,1])
>>> plt.bar(X, Y, color='g')
<BarContainer object of 171 artists>
>>> plt.xlabel("Size")
Text(0.5, 0, 'Size')
>>> plt.ylabel("Price")
Text(0, 0.5, 'Price')
>>> plt.show()
>>> 