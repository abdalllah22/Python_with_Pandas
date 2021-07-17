import numpy as np
import pandas as pd


def solution(files):
    # files - any of available files, i.e:
    # write your solution here
    all_lists = []
    for file in files: 
        df = pd.read_csv(file)
        # year = pd.DatetimeIndex(df['date']).year
        df_vol = df.groupby([pd.DatetimeIndex(df['date']).year]).max().head().drop_duplicates(subset = ["vol"])
        print(df_vol[['date','vol']])
        df_close = df.groupby([pd.DatetimeIndex(df['date']).year]).max().head().drop_duplicates(subset = ["close"])
        print(df_close[['date','close']].reset_index(0))
        innerlist = [df_vol,df_close]
        all_lists.append(innerlist)
    # return all_lists

files = ["./data/framp.csv", "./data/gnyned.csv", "./data/gwoomed.csv",
               "./data/hoilled.csv", "./data/plent.csv", "./data/throwsh.csv",
               "./data/twerche.csv", "./data/veeme.csv"]
# files = ["./data/framp.csv"]
solution(files)
