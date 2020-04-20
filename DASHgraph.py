import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go

app = dash.Dash()

df = pd.read_csv("/Users/dines/OneDrive/Documents/coursAnneLaure/data/timesData.csv")
df = df.loc[:20, ["num_students", "female_male_ratio", "university_name"]]
df['num_students'] = [float(each.replace(',','.')) for each in df.num_students]
df = df.dropna().head(20)
df["female_male_ratio"] = [(each.replace(':','/')) for each in df["female_male_ratio"]]

colors = {
    'background': 'white',
    'text': 'black'
}

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Graphique Dash',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),
    html.Div(children="le nombre d’étudiants total en fonction du Ratio étudiant féminin / étudiant masculin", style={
        'textAlign': 'center',
        'color': colors['text']
    }),
    dcc.Graph(
        id='Graph1',
        figure={
            'data': [
                go.Bar(
                x = df["female_male_ratio"],
                y = df["num_students"],
                name = "university_name",
                marker = dict(color = 'rgba(241, 136, 187, 5)', line = dict(color ='rgb(0,0,0)',width =1.5)),
                text = df.university_name)
            ],
            'layout': {
                    'plot_bgcolor': colors['background'],
                    'paper_bgcolor': colors['background'],
                    'font': {
                        'color': colors['text']}
                }    
                
            
            
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)

