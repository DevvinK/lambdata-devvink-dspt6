# my_lambdata/my_script.py
# python -m my_lambdata.my_script

import pandas as pd
from my_lambdata.my_mod import enlarge, null_check, date_divider
import numpy as na


print("Hello")

df = pd.DataFrame({"a":[1,2,3], "b":[4,5,6]})
print(df.head())

df2 = pd. DataFrame({"a":[na.nan,2,3], "b":[4,5,6]})
print(null_check(df2))

raw_data = {'name': ['Willard Morris', 'Al Jennings', 'Omar Mullins', 'Spencer McDaniel'],
'age': [20, 19, 22, 21],
'favorite_color': ['blue', 'red', 'yellow', "green"],
'grade': [88, 92, 95, 70],
'birth_date': ['01-02-1996', '08-05-1997', '04-28-1996', '12-16-1995']}
df3 = pd.DataFrame(raw_data, index = ['Willard Morris', 'Al Jennings', 'Omar Mullins', 'Spencer McDaniel'])
print(date_divider(df3,'birth_date'))

x=11
print(enlarge(x))