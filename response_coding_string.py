# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 13:55:08 2020

@author: HP
"""


import pandas as pd
import numpy as np



def response_coding(target,df):
    
    no_class=df[target].unique()
    l=[]
    d={}
    
    for column in df.columns:
        if df[column].dtypes == np.object:
            no_categories=df[column].unique()
            for j in range(len(no_categories)):
                for i in range(len(no_class)):
                    prob=(df[(df[column]==no_categories[j])&(df.classes==no_class[i])].count()/df[(df[column]==no_categories[j])].count()).values
                    prob=list(prob)
                    key=no_categories[j]+"."+column+"."+column+str(no_class[i])
                    value=prob[0]
                    d.setdefault(key,value)
                    df[column+str(no_class[i])]= pd.Series(prob[0])
                    
                           
    for k,v in d.items():
        column_name=k[k.find('.')+1:][:k[k.find('.')+1:].find('.')] # name of column for which response coding is performed
        category=k[:k.find('.')] # category of column
        cat_class=k[k[::-1].find('.')+2:] #Class category based on dependent label
        df[cat_class]=np.where(df[column_name]==category,v,df[cat_class])
            
    print(no_class)
    print(df.head())


response_coding("Target",df)