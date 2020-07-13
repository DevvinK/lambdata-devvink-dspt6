# my_lambdata/my_mod.py
# my_lambdata.my_mod

import pandas as pd

def enlarge(num):
   return num * 100

def null_check(df):
   null_lines = df[df.isnull().any(axis=1)]
   return null_lines

def date_divider(df,date_col):
   '''
    df: the whole dataframe adding new day, month, year to
    date_col: the name of the column the date is stored in
   '''
   converted_df = df.copy()
   converted_df["Year"] = pd.DatetimeIndex(converted_df[date_col]).year
   converted_df["Month"] = pd.DatetimeIndex(converted_df[date_col]).month
   converted_df["Day"] = pd.DatetimeIndex(converted_df[date_col]).day
   return converted_df

if __name__ == "__main__":
   x = 11
   print(enlarge(x))

   y = int(input("Please choose a number (e.g. 5)"))
   print(enlarge(y))