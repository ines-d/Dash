import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px


app = dash.Dash()
server = app.server

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash('auth', external_stylesheets=external_stylesheets)

#préparer les données
df = pd.read_csv("/Users/dines/OneDrive/Documents/coursAnneLaure/data/timesData.csv")

df = df[["world_rank","university_name", "teaching", "year","income"]]

df2011 = df[df.year == 2011].iloc[:3]
df2012 = df[df.year == 2012].iloc[:3]
df2013 = df[df.year == 2013].iloc[:3]
df2014 = df[df.year == 2014].iloc[:3]
df2015 = df[df.year == 2015].iloc[:3]
df2016 = df[df.year == 2016].iloc[:3]

data = pd.concat([df2011,df2012,df2013,df2014,df2015,df2016])




markdown_text="""
# Exercice 3 Plotly
"""
texte1="""
Ce graphique va montrer l'évolution du score universitaire pour l'enseignement "teaching" pour les 3 premières University pour chaque annnée, sur une péride de 2011 à 2016.
"""

texte2="""
On remarque que "teaching" le score universitaire pour l'enseignement (l'environnement d'apprentissage) 
baisse d'année en année.
"""


app.layout = html.Div([
    dcc.Markdown(children=markdown_text, style={'textAlign': 'center', 'color':'black'}),
    html.Div([
        dcc.Markdown(children=texte1)
    ]),
    html.Div([
        html.H2(
            children='3D Scatter Plots',
            style={
                'textAlign': 'center',
                'color': 'black'
            }
        )
    ]),
    html.Div([
        dcc.Graph(
            figure=px.scatter_3d(data, x=data.teaching, y=data.university_name, z=data.year, color=data.university_name)
        )
    ]),
    html.Div([
        dcc.Markdown(children=texte2)
    ])

])


if __name__ == '__main__':
    app.run_server(debug=True)



