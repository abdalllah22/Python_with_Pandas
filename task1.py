import pandas as pd
import numpy as np


def process_data():
    # Do not alter this line.
    biopics = pd.read_csv("biopics.csv",encoding='latin-1')
    # Write your code here.
    # Remember to return the right object.
    # print(biopics)
    # print(biopics.sort_values("title"))
    if not biopics["title"].is_unique:
        biopics.drop_duplicates(subset =['title'], keep = False, inplace = True) 
    biopics.rename(index=str,columns={'box_office':'earnings'},inplace=True)
    biopics.dropna(subset = ["earnings"], inplace=True)
    biopics.drop(biopics[biopics.year_release <= 1990].index, inplace=True)
    biopics['type_of_subject'] = pd.Categorical(biopics.type_of_subject)
    biopics['country'] = biopics.country.astype('category') # anthor way 
    biopics['lead_actor_actress_known'] = np.where(biopics['lead_actor_actress'].isnull(), False, True )
    biopics['earnings'] = (biopics['earnings'].astype(float)/1000000).astype(float)
    biopics = biopics[["title", "year_release", "earnings","country","type_of_subject","lead_actor_actress","lead_actor_actress_known"]]
    biopics.sort_values(by='earnings', ascending=False, inplace=True)
    print(biopics) 


    print(biopics.columns)


process_data()