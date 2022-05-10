import pandas as pd
import requests
import io
import numpy

url = "https://raw.githubusercontent.com/cognizance-amrita/AI-Tasks/main/Q4-Dataset.csv"
download = requests.get(url).content
df = pd.read_csv(io.StringIO(download.decode('utf-8')))
arr = df.to_numpy()
arr = arr[arr[:, 2].argsort()]
print(arr)
df1 = pd.DataFrame(arr, columns=['ProductID','price','rating'])
print(df1)
