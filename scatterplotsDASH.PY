import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go

app = dash.Dash()

df = pd.read_csv("/Users/dines/OneDrive/Documents/coursAnneLaure/data/timesData.csv")
df = df.loc[:20, ["num_students", "female_male_ratio","university_name"]]
df['num_students'] = [float(each.replace(',','.')) for each in df.num_students]
df = df.dropna().head(20)
df["female_male_ratio"] = [(each.replace(':','/')) for each in df["female_male_ratio"]]


app.layout = html.Div([
    dcc.Graph(
        id='num',
        figure={
            'data': [
                go.Scatter(
                    x=df[df["university_name"]==i]["female_male_ratio"],
                    y=df[df["university_name"]==i]["num_students"],
                    text=df["num_students"],
                    mode='markers',
                    opacity=0.8,
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name=i
                    )for i in df.university_name.unique()

            ],
            'layout': go.Layout(title="le nombre d’étudiants total en fonction du Ratio (étudiant féminin / étudiant masculin)",
                xaxis={'title': 'Ratio étudiants féminin / étudiants masculin'},
                yaxis={'title': 'Nombre étudiants Total'},
                margin={'l': 40, 'b': 40, 't': 100, 'r': 10},
                legend={'x': 1.2, 'y': 1},
                hovermode='closest'
            )
        }
    )
])



if __name__ == '__main__':
    app.run_server(debug=True)