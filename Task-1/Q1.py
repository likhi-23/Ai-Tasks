Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> f = open(r'C:\Users\karri\OneDrive\Desktop\file.txt','r')
>>> p = f.read()
>>> print(p)
1Aaa3.5Maths2Bbb4.2Physics3Ccc7.62Chemistry4Ddd9.55Biology5Eee4.0Social6Fff7.6English7Ggg3.111Maths8Hhh9.99Physics9Iii1.23Civics
>>> f.close()
>>> import pandas as pd
>>> df = pd.read_csv(r'C:\Users\karri\OneDrive\Desktop\file.txt')
>>> df.to_csv('Filename2.csv',index = None)
>>> import pandas as pd
>>> df = pd.read_csv(r'C:\Users\karri\OneDrive\Desktop\AI TASKS\Filename2.csv')
>>> print(df)
   1  Aaa    3.5      Maths
0  2  Bbb  4.200    Physics
1  3  Ccc  7.620  Chemistry
2  4  Ddd  9.550    Biology
3  5  Eee  4.000     Social
4  6  Fff  7.600    English
5  7  Ggg  3.111      Maths
6  8  Hhh  9.990    Physics
7  9  Iii  1.230     Civics
>>> 