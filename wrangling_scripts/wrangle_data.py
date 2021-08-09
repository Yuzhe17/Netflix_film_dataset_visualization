import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sb
from collections import Counter
from plotly.express import bar

def datawrangling(path):
    '''Wrangling the dataset for plotting

    Args(str): path to the dataset

    Returns(Object): pandas dataframe
    '''

    df=pd.read_csv(path,parse_dates=['Premiere'],encoding='ISO-8859-1')
    df['Premiere_month']=df['Premiere'].dt.month
    df['Premiere_year']=df['Premiere'].dt.year.astype('str')

    return df

def contain_english(language_list):
    num=0
    for language in language_list:
        if 'English' in language:
            num+=1
    return round(num/len(language_list),2)

def return_figures():
    '''return figures
    '''
    df=datawrangling('data/NetflixOriginals.csv')
    IMDB_df_5=df.sort_values(by=['IMDB Score'],ascending=False).iloc[:5,:]
    genre_df_5=df.groupby(by=['Genre']).count()[['Title']].reset_index()\
               .sort_values(by=['Title'],ascending=False).iloc[:5,:]
    year_df=df.groupby(by=['Premiere_year']).count()[['Title']].reset_index()
    englishnumber_df=df[['Premiere_year','Language']].groupby(by=['Premiere_year']).aggregate(contain_english).reset_index()



    graph_one=bar(IMDB_df_5,y='Title',x='IMDB Score',category_orders={'Title':IMDB_df_5['Title'].to_list()[::]}\
        ,labels={"Title":"film title"},title="Top 5 films with highest IMDB scores",text='IMDB Score')
    graph_two=bar(genre_df_5,x='Genre',y='Title',labels={"Title":"Number of films"},title="Number of released films by genre",text='Title')
    graph_three=bar(year_df,x='Premiere_year',y='Title',text='Title',labels={"Title":"Number of films","Premiere_year":"Year"},title="Number of released films by year")
    graph_four=bar(englishnumber_df,x='Premiere_year',y='Language',text='Language',labels={"Language":"proportion of Enlish film","Premiere_year":"Year"},title="Proportion of Enlish film by year")


    figures=[]
    figures.append(dict(data=graph_one))
    figures.append(dict(data=graph_two))
    figures.append(dict(data=graph_three))
    figures.append(dict(data=graph_four))

    return figures
