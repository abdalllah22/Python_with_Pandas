import pandas as pd
import numpy as np

import mysql.connector as sql

'''
# series in pandas 
a = (11,22,33,44,55,66)
b = {'a':1, 'b':2}
sr = pd.Series(b)
print(sr)
'''
'''
# deal with CSV files
player_data_frame = pd.read_csv("data.csv")
print(player_data_frame.head())
print(player_data_frame.shape)
'''
'''
# deal with Json files
player_data_frame = pd.read_json("data2.json")
print(player_data_frame.head())
print(player_data_frame.shape)
'''
'''
# deal with Json files
url = "https://en.wikipedia.org/wiki/mosalah"
tables = pd.read_html(url)
print(len(tables))
'''
'''
# melt fuction
players_df = pd.read_csv("data.csv")
print(players_df.head())
print("-----------------><-------------------------")
players_df_melted = pd.melt(players_df, id_vars=['name'], value_vars=['age'], var_name ='ChangedVarname', value_name ='ChangedValname' ) # to get specific col 
players_df_melted = pd.melt(players_df, id_vars=['name'], var_name ='ChangedVarname', value_name ='ChangedValname' )    # to get all cols
print(players_df_melted)
'''
'''
student_df = pd.DataFrame({
    'name': ['John', 'Boby', 'Mina'],
    'level': ['Masters', 'Graduate', 'Graduate'],
    'age': [27, 23, 21]
})
print(student_df)
print("-----------------><-------------------------")
student_df_pivot = student_df.pivot(index="level", columns="name", values="age")
print(student_df_pivot)
'''
'''
# bins and covert to categorical values
players_df = pd.read_csv("data.csv")
print(players_df['age'].value_counts())
def age(x):
    if x > 30:
        return 'old'
    else:
        return 'small'
players_df['age'] = players_df['age'].apply(age)
print(players_df['age'].value_counts())
'''
'''
# series in pandas 
a = (11,22,33,44,55,66)
b = {'a':1, 'b':2}
sr = pd.Series(a,index=['a','b','c','d','e','f'])

print(sr.iloc[1:3])
'''
me = ['ahmed','abdallah','mohamed']
ser = pd.Series(me)
print(ser.index)
print(ser.values)
print(ser.dtype)
df = pd.read_csv('./data/pokemon.csv')
print(df.shape)