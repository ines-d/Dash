#!/usr/bin/env python
# coding: utf-8

# In[34]:


import numpy as np # algèbre linéaire
import pandas as pd # procès de données, CSV file I/O (e.g. pd.read_csv)

# plotly
# import plotly.plotly as py
from plotly.offline import init_notebook_mode, iplot, plot
import plotly as py
init_notebook_mode(connected=True)
import plotly.graph_objs as go

# librairie word cloud
from wordcloud import WordCloud

# librairie matplotlib
import matplotlib.pyplot as plt

# Permet d'afficher les données disponibles dans le répertoire data
import os
print(os.listdir("/Users/dines/OneDrive/Documents/coursAnneLaure/data")) 

# Chargement des données qui seront utilisées.
timesData = pd.read_csv("/Users/dines/OneDrive/Documents/coursAnneLaure/data/timesData.csv")
timesData.info()


# In[56]:


"""
Créer un dashboard Dash afﬁchant un scatter plots avec le nombre d’étudiants total 
en fonction du Ratio étudiant féminin / étudiant masculin, pour les 20 premières université du classement.
"""

df = timesData.loc[:20, ["num_students", "female_male_ratio", "university_name"]]
df['num_students'] = [float(each.replace(',','.')) for each in df.num_students]
df = df.dropna().head(20)
df["female_male_ratio"] = [(each.replace(':','/')) for each in df["female_male_ratio"]]
df['university_name'] = df.university_name.astype(str)#= [str(each) for each in df.university_name]


print(df.info())
df.num_students
df.female_male_ratio
df


# In[62]:


trace1 = go.Bar(
                x = df["female_male_ratio"],
                y = df["num_students"],
                name = "univarsity_name",
                marker = dict(color = 'rgba(255, 51, 150, 5)', line = dict(color ='rgb(0,0,0)',width =1)),
                text = df.university_name)

data = [trace1]
layout = go.Layout(barmode = "group", title = "le nombre d’étudiants total en fonction du Ratio étudiant féminin / étudiant masculin",
                  xaxis={'title': 'Ratio étudiants féminin / étudiants masculin'},
                yaxis={'title': 'Nombre étudiants Total'})
fig = go.Figure(data = data, layout = layout)
iplot(fig)


# In[58]:


figure={
            'data': [
                go.Scatter(
                    x=df["female_male_ratio"],
                    y=df["num_students"],
                    text=df["university_name"],
                    mode='markers',
                    opacity=0.8,
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'black'}
                    },
                    #name= i
                ) #for i in df.university_name.unique()
            ],
            'layout': go.Layout(
                xaxis={'title': 'Ratio étudiants féminin / étudiants masculin'},
                yaxis={'title': 'Nombre étudiants Total'},
                margin={'l': 150, 'b': 130, 't': 40, 'r': 40},
                legend={'x': 0, 'y': 1},
                hovermode='closest'
            )
        }
iplot(figure)


# In[59]:


figure={
            'data': [
                go.Scatter(
                    x=df[df["university_name"]==i]["female_male_ratio"],#pour avoir la légende
                    y=df[df["university_name"]==i]["num_students"],
                    text=df["university_name"],
                    mode='markers',
                    opacity=0.8,
                    marker={
                        'size': 10,
                        'line': {'width': 0.1, 'color': 'black'}
                    },
                    name= i#pour la légende
                ) for i in df.university_name.unique() #pour la légende
            ],
            'layout': go.Layout(
                xaxis={'title': 'Ratio étudiants féminin / étudiants masculin'},
                yaxis={'title': 'Nombre étudiants Total'},
                margin={'l': 30, 'b': 130, 't': 50, 'r': 50},
                legend={'x': 0.2, 'y': -2},
                hovermode='closest'
            )
        }
iplot(figure)


# In[64]:


data = [
    {
        'y': df.num_students,
        'x': df.female_male_ratio,
        'mode': 'markers',
        'marker': {
            'color': df.num_students,
            'size': df.num_students,
            'showscale': True # c'est la barre de couleur à droite
        },
        "text" :  df.university_name
    }
]
layout= go.Layout(title = "Le nombre d’étudiants total en fonction du Ratio étudiant féminin / étudiant masculin",
                xaxis={'title': 'Ratio étudiants féminin / étudiants masculin'},
                yaxis={'title': 'Nombre étudiants Total'})
                #margin={'l': 150, 'b': 130, 't': 40, 'r': 40},
                #legend={'x': 0, 'y': 1},
                #hovermode='closes')
    
fig = go.Figure(data = data, layout = layout)

    
    
iplot(fig)


# In[ ]:




