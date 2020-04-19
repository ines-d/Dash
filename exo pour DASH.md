```python
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
```


<script type="text/javascript">
window.PlotlyConfig = {MathJaxConfig: 'local'};
if (window.MathJax) {MathJax.Hub.Config({SVG: {font: "STIX-Web"}});}
if (typeof require !== 'undefined') {
require.undef("plotly");
requirejs.config({
    paths: {
        'plotly': ['https://cdn.plot.ly/plotly-latest.min']
    }
});
require(['plotly'], function(Plotly) {
    window._Plotly = Plotly;
});
}
</script>



    ['timesData.csv']
    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 2603 entries, 0 to 2602
    Data columns (total 14 columns):
     #   Column                  Non-Null Count  Dtype  
    ---  ------                  --------------  -----  
     0   world_rank              2603 non-null   object 
     1   university_name         2603 non-null   object 
     2   country                 2603 non-null   object 
     3   teaching                2603 non-null   float64
     4   international           2603 non-null   object 
     5   research                2603 non-null   float64
     6   citations               2603 non-null   float64
     7   income                  2603 non-null   object 
     8   total_score             2603 non-null   object 
     9   num_students            2544 non-null   object 
     10  student_staff_ratio     2544 non-null   float64
     11  international_students  2536 non-null   object 
     12  female_male_ratio       2370 non-null   object 
     13  year                    2603 non-null   int64  
    dtypes: float64(4), int64(1), object(9)
    memory usage: 284.8+ KB
    


```python
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

```

    <class 'pandas.core.frame.DataFrame'>
    Int64Index: 18 entries, 1 to 20
    Data columns (total 3 columns):
     #   Column             Non-Null Count  Dtype  
    ---  ------             --------------  -----  
     0   num_students       18 non-null     float64
     1   female_male_ratio  18 non-null     object 
     2   university_name    18 non-null     object 
    dtypes: float64(1), object(2)
    memory usage: 576.0+ bytes
    None
    




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>num_students</th>
      <th>female_male_ratio</th>
      <th>university_name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>2.243</td>
      <td>33 / 67</td>
      <td>California Institute of Technology</td>
    </tr>
    <tr>
      <th>2</th>
      <td>11.074</td>
      <td>37 / 63</td>
      <td>Massachusetts Institute of Technology</td>
    </tr>
    <tr>
      <th>3</th>
      <td>15.596</td>
      <td>42 / 58</td>
      <td>Stanford University</td>
    </tr>
    <tr>
      <th>4</th>
      <td>7.929</td>
      <td>45 / 55</td>
      <td>Princeton University</td>
    </tr>
    <tr>
      <th>5</th>
      <td>18.812</td>
      <td>46 / 54</td>
      <td>University of Cambridge</td>
    </tr>
    <tr>
      <th>6</th>
      <td>19.919</td>
      <td>46 / 54</td>
      <td>University of Oxford</td>
    </tr>
    <tr>
      <th>7</th>
      <td>36.186</td>
      <td>50 / 50</td>
      <td>University of California, Berkeley</td>
    </tr>
    <tr>
      <th>8</th>
      <td>15.060</td>
      <td>37 / 63</td>
      <td>Imperial College London</td>
    </tr>
    <tr>
      <th>9</th>
      <td>11.751</td>
      <td>50 / 50</td>
      <td>Yale University</td>
    </tr>
    <tr>
      <th>10</th>
      <td>38.206</td>
      <td>52 / 48</td>
      <td>University of California, Los Angeles</td>
    </tr>
    <tr>
      <th>11</th>
      <td>14.221</td>
      <td>42 / 58</td>
      <td>University of Chicago</td>
    </tr>
    <tr>
      <th>12</th>
      <td>15.128</td>
      <td>50 / 50</td>
      <td>Johns Hopkins University</td>
    </tr>
    <tr>
      <th>13</th>
      <td>21.424</td>
      <td>48 / 52</td>
      <td>Cornell University</td>
    </tr>
    <tr>
      <th>14</th>
      <td>18.178</td>
      <td>31 / 69</td>
      <td>ETH Zurich – Swiss Federal Institute of Techno...</td>
    </tr>
    <tr>
      <th>15</th>
      <td>41.786</td>
      <td>48 / 52</td>
      <td>University of Michigan</td>
    </tr>
    <tr>
      <th>18</th>
      <td>20.376</td>
      <td>51 / 49</td>
      <td>University of Pennsylvania</td>
    </tr>
    <tr>
      <th>19</th>
      <td>11.885</td>
      <td>39 / 61</td>
      <td>Carnegie Mellon University</td>
    </tr>
    <tr>
      <th>20</th>
      <td>19.835</td>
      <td>53 / 47</td>
      <td>University of Hong Kong</td>
    </tr>
  </tbody>
</table>
</div>




```python
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
```


<div>


            <div id="353a7b9e-7a8a-4703-a771-1995045ea75c" class="plotly-graph-div" style="height:525px; width:100%;"></div>
            <script type="text/javascript">
                require(["plotly"], function(Plotly) {
                    window.PLOTLYENV=window.PLOTLYENV || {};

                if (document.getElementById("353a7b9e-7a8a-4703-a771-1995045ea75c")) {
                    Plotly.newPlot(
                        '353a7b9e-7a8a-4703-a771-1995045ea75c',
                        [{"marker": {"color": "rgba(255, 51, 150, 5)", "line": {"color": "rgb(0,0,0)", "width": 1}}, "name": "univarsity_name", "text": ["California Institute of Technology", "Massachusetts Institute of Technology", "Stanford University", "Princeton University", "University of Cambridge", "University of Oxford", "University of California, Berkeley", "Imperial College London", "Yale University", "University of California, Los Angeles", "University of Chicago", "Johns Hopkins University", "Cornell University", "ETH Zurich \u2013 Swiss Federal Institute of Technology Zurich", "University of Michigan", "University of Pennsylvania", "Carnegie Mellon University", "University of Hong Kong"], "type": "bar", "x": ["33 / 67", "37 / 63", "42 / 58", "45 / 55", "46 / 54", "46 / 54", "50 / 50", "37 / 63", "50 / 50", "52 / 48", "42 / 58", "50 / 50", "48 / 52", "31 / 69", "48 / 52", "51 / 49", "39 / 61", "53 / 47"], "y": [2.243, 11.074, 15.596, 7.929, 18.812, 19.919, 36.186, 15.06, 11.751, 38.206, 14.221, 15.128, 21.424, 18.178, 41.786, 20.376, 11.885, 19.835]}],
                        {"barmode": "group", "template": {"data": {"bar": [{"error_x": {"color": "#2a3f5f"}, "error_y": {"color": "#2a3f5f"}, "marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "bar"}], "barpolar": [{"marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "barpolar"}], "carpet": [{"aaxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "baxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "type": "carpet"}], "choropleth": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "choropleth"}], "contour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "contour"}], "contourcarpet": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "contourcarpet"}], "heatmap": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmap"}], "heatmapgl": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmapgl"}], "histogram": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "histogram"}], "histogram2d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2d"}], "histogram2dcontour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2dcontour"}], "mesh3d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "mesh3d"}], "parcoords": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "parcoords"}], "pie": [{"automargin": true, "type": "pie"}], "scatter": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter"}], "scatter3d": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter3d"}], "scattercarpet": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattercarpet"}], "scattergeo": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergeo"}], "scattergl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergl"}], "scattermapbox": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattermapbox"}], "scatterpolar": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolar"}], "scatterpolargl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolargl"}], "scatterternary": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterternary"}], "surface": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "surface"}], "table": [{"cells": {"fill": {"color": "#EBF0F8"}, "line": {"color": "white"}}, "header": {"fill": {"color": "#C8D4E3"}, "line": {"color": "white"}}, "type": "table"}]}, "layout": {"annotationdefaults": {"arrowcolor": "#2a3f5f", "arrowhead": 0, "arrowwidth": 1}, "coloraxis": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "colorscale": {"diverging": [[0, "#8e0152"], [0.1, "#c51b7d"], [0.2, "#de77ae"], [0.3, "#f1b6da"], [0.4, "#fde0ef"], [0.5, "#f7f7f7"], [0.6, "#e6f5d0"], [0.7, "#b8e186"], [0.8, "#7fbc41"], [0.9, "#4d9221"], [1, "#276419"]], "sequential": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "sequentialminus": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]]}, "colorway": ["#636efa", "#EF553B", "#00cc96", "#ab63fa", "#FFA15A", "#19d3f3", "#FF6692", "#B6E880", "#FF97FF", "#FECB52"], "font": {"color": "#2a3f5f"}, "geo": {"bgcolor": "white", "lakecolor": "white", "landcolor": "#E5ECF6", "showlakes": true, "showland": true, "subunitcolor": "white"}, "hoverlabel": {"align": "left"}, "hovermode": "closest", "mapbox": {"style": "light"}, "paper_bgcolor": "white", "plot_bgcolor": "#E5ECF6", "polar": {"angularaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "radialaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "scene": {"xaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "yaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "zaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}}, "shapedefaults": {"line": {"color": "#2a3f5f"}}, "ternary": {"aaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "baxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "caxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "title": {"x": 0.05}, "xaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "title": {"standoff": 15}, "zerolinecolor": "white", "zerolinewidth": 2}, "yaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "title": {"standoff": 15}, "zerolinecolor": "white", "zerolinewidth": 2}}}, "title": {"text": "le nombre d\u2019\u00e9tudiants total en fonction du Ratio \u00e9tudiant f\u00e9minin / \u00e9tudiant masculin"}, "xaxis": {"title": {"text": "Ratio \u00e9tudiants f\u00e9minin / \u00e9tudiants masculin"}}, "yaxis": {"title": {"text": "Nombre \u00e9tudiants Total"}}},
                        {"responsive": true}
                    ).then(function(){

var gd = document.getElementById('353a7b9e-7a8a-4703-a771-1995045ea75c');
var x = new MutationObserver(function (mutations, observer) {{
        var display = window.getComputedStyle(gd).display;
        if (!display || display === 'none') {{
            console.log([gd, 'removed!']);
            Plotly.purge(gd);
            observer.disconnect();
        }}
}});

// Listen for the removal of the full notebook cells
var notebookContainer = gd.closest('#notebook-container');
if (notebookContainer) {{
    x.observe(notebookContainer, {childList: true});
}}

// Listen for the clearing of the current output cell
var outputEl = gd.closest('.output');
if (outputEl) {{
    x.observe(outputEl, {childList: true});
}}

                        })
                };
                });
            </script>
        </div>



```python
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
```


<div>


            <div id="7a8bd396-72c2-4892-8adc-38726ea923e6" class="plotly-graph-div" style="height:525px; width:100%;"></div>
            <script type="text/javascript">
                require(["plotly"], function(Plotly) {
                    window.PLOTLYENV=window.PLOTLYENV || {};

                if (document.getElementById("7a8bd396-72c2-4892-8adc-38726ea923e6")) {
                    Plotly.newPlot(
                        '7a8bd396-72c2-4892-8adc-38726ea923e6',
                        [{"marker": {"line": {"color": "black", "width": 0.5}, "size": 15}, "mode": "markers", "opacity": 0.8, "text": ["California Institute of Technology", "Massachusetts Institute of Technology", "Stanford University", "Princeton University", "University of Cambridge", "University of Oxford", "University of California, Berkeley", "Imperial College London", "Yale University", "University of California, Los Angeles", "University of Chicago", "Johns Hopkins University", "Cornell University", "ETH Zurich \u2013 Swiss Federal Institute of Technology Zurich", "University of Michigan", "University of Pennsylvania", "Carnegie Mellon University", "University of Hong Kong"], "type": "scatter", "x": ["33 / 67", "37 / 63", "42 / 58", "45 / 55", "46 / 54", "46 / 54", "50 / 50", "37 / 63", "50 / 50", "52 / 48", "42 / 58", "50 / 50", "48 / 52", "31 / 69", "48 / 52", "51 / 49", "39 / 61", "53 / 47"], "y": [2.243, 11.074, 15.596, 7.929, 18.812, 19.919, 36.186, 15.06, 11.751, 38.206, 14.221, 15.128, 21.424, 18.178, 41.786, 20.376, 11.885, 19.835]}],
                        {"hovermode": "closest", "legend": {"x": 0, "y": 1}, "margin": {"b": 130, "l": 150, "r": 40, "t": 40}, "template": {"data": {"bar": [{"error_x": {"color": "#2a3f5f"}, "error_y": {"color": "#2a3f5f"}, "marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "bar"}], "barpolar": [{"marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "barpolar"}], "carpet": [{"aaxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "baxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "type": "carpet"}], "choropleth": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "choropleth"}], "contour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "contour"}], "contourcarpet": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "contourcarpet"}], "heatmap": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmap"}], "heatmapgl": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmapgl"}], "histogram": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "histogram"}], "histogram2d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2d"}], "histogram2dcontour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2dcontour"}], "mesh3d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "mesh3d"}], "parcoords": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "parcoords"}], "pie": [{"automargin": true, "type": "pie"}], "scatter": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter"}], "scatter3d": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter3d"}], "scattercarpet": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattercarpet"}], "scattergeo": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergeo"}], "scattergl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergl"}], "scattermapbox": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattermapbox"}], "scatterpolar": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolar"}], "scatterpolargl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolargl"}], "scatterternary": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterternary"}], "surface": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "surface"}], "table": [{"cells": {"fill": {"color": "#EBF0F8"}, "line": {"color": "white"}}, "header": {"fill": {"color": "#C8D4E3"}, "line": {"color": "white"}}, "type": "table"}]}, "layout": {"annotationdefaults": {"arrowcolor": "#2a3f5f", "arrowhead": 0, "arrowwidth": 1}, "coloraxis": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "colorscale": {"diverging": [[0, "#8e0152"], [0.1, "#c51b7d"], [0.2, "#de77ae"], [0.3, "#f1b6da"], [0.4, "#fde0ef"], [0.5, "#f7f7f7"], [0.6, "#e6f5d0"], [0.7, "#b8e186"], [0.8, "#7fbc41"], [0.9, "#4d9221"], [1, "#276419"]], "sequential": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "sequentialminus": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]]}, "colorway": ["#636efa", "#EF553B", "#00cc96", "#ab63fa", "#FFA15A", "#19d3f3", "#FF6692", "#B6E880", "#FF97FF", "#FECB52"], "font": {"color": "#2a3f5f"}, "geo": {"bgcolor": "white", "lakecolor": "white", "landcolor": "#E5ECF6", "showlakes": true, "showland": true, "subunitcolor": "white"}, "hoverlabel": {"align": "left"}, "hovermode": "closest", "mapbox": {"style": "light"}, "paper_bgcolor": "white", "plot_bgcolor": "#E5ECF6", "polar": {"angularaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "radialaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "scene": {"xaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "yaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "zaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}}, "shapedefaults": {"line": {"color": "#2a3f5f"}}, "ternary": {"aaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "baxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "caxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "title": {"x": 0.05}, "xaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "title": {"standoff": 15}, "zerolinecolor": "white", "zerolinewidth": 2}, "yaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "title": {"standoff": 15}, "zerolinecolor": "white", "zerolinewidth": 2}}}, "xaxis": {"title": {"text": "Ratio \u00e9tudiants f\u00e9minin / \u00e9tudiants masculin"}}, "yaxis": {"title": {"text": "Nombre \u00e9tudiants Total"}}},
                        {"responsive": true}
                    ).then(function(){

var gd = document.getElementById('7a8bd396-72c2-4892-8adc-38726ea923e6');
var x = new MutationObserver(function (mutations, observer) {{
        var display = window.getComputedStyle(gd).display;
        if (!display || display === 'none') {{
            console.log([gd, 'removed!']);
            Plotly.purge(gd);
            observer.disconnect();
        }}
}});

// Listen for the removal of the full notebook cells
var notebookContainer = gd.closest('#notebook-container');
if (notebookContainer) {{
    x.observe(notebookContainer, {childList: true});
}}

// Listen for the clearing of the current output cell
var outputEl = gd.closest('.output');
if (outputEl) {{
    x.observe(outputEl, {childList: true});
}}

                        })
                };
                });
            </script>
        </div>



```python
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
```


<div>


            <div id="44994af2-7420-4db0-81b0-d4f618df1b29" class="plotly-graph-div" style="height:525px; width:100%;"></div>
            <script type="text/javascript">
                require(["plotly"], function(Plotly) {
                    window.PLOTLYENV=window.PLOTLYENV || {};

                if (document.getElementById("44994af2-7420-4db0-81b0-d4f618df1b29")) {
                    Plotly.newPlot(
                        '44994af2-7420-4db0-81b0-d4f618df1b29',
                        [{"marker": {"line": {"color": "black", "width": 0.1}, "size": 10}, "mode": "markers", "name": "California Institute of Technology", "opacity": 0.8, "text": ["California Institute of Technology", "Massachusetts Institute of Technology", "Stanford University", "Princeton University", "University of Cambridge", "University of Oxford", "University of California, Berkeley", "Imperial College London", "Yale University", "University of California, Los Angeles", "University of Chicago", "Johns Hopkins University", "Cornell University", "ETH Zurich \u2013 Swiss Federal Institute of Technology Zurich", "University of Michigan", "University of Pennsylvania", "Carnegie Mellon University", "University of Hong Kong"], "type": "scatter", "x": ["33 / 67"], "y": [2.243]}, {"marker": {"line": {"color": "black", "width": 0.1}, "size": 10}, "mode": "markers", "name": "Massachusetts Institute of Technology", "opacity": 0.8, "text": ["California Institute of Technology", "Massachusetts Institute of Technology", "Stanford University", "Princeton University", "University of Cambridge", "University of Oxford", "University of California, Berkeley", "Imperial College London", "Yale University", "University of California, Los Angeles", "University of Chicago", "Johns Hopkins University", "Cornell University", "ETH Zurich \u2013 Swiss Federal Institute of Technology Zurich", "University of Michigan", "University of Pennsylvania", "Carnegie Mellon University", "University of Hong Kong"], "type": "scatter", "x": ["37 / 63"], "y": [11.074]}, {"marker": {"line": {"color": "black", "width": 0.1}, "size": 10}, "mode": "markers", "name": "Stanford University", "opacity": 0.8, "text": ["California Institute of Technology", "Massachusetts Institute of Technology", "Stanford University", "Princeton University", "University of Cambridge", "University of Oxford", "University of California, Berkeley", "Imperial College London", "Yale University", "University of California, Los Angeles", "University of Chicago", "Johns Hopkins University", "Cornell University", "ETH Zurich \u2013 Swiss Federal Institute of Technology Zurich", "University of Michigan", "University of Pennsylvania", "Carnegie Mellon University", "University of Hong Kong"], "type": "scatter", "x": ["42 / 58"], "y": [15.596]}, {"marker": {"line": {"color": "black", "width": 0.1}, "size": 10}, "mode": "markers", "name": "Princeton University", "opacity": 0.8, "text": ["California Institute of Technology", "Massachusetts Institute of Technology", "Stanford University", "Princeton University", "University of Cambridge", "University of Oxford", "University of California, Berkeley", "Imperial College London", "Yale University", "University of California, Los Angeles", "University of Chicago", "Johns Hopkins University", "Cornell University", "ETH Zurich \u2013 Swiss Federal Institute of Technology Zurich", "University of Michigan", "University of Pennsylvania", "Carnegie Mellon University", "University of Hong Kong"], "type": "scatter", "x": ["45 / 55"], "y": [7.929]}, {"marker": {"line": {"color": "black", "width": 0.1}, "size": 10}, "mode": "markers", "name": "University of Cambridge", "opacity": 0.8, "text": ["California Institute of Technology", "Massachusetts Institute of Technology", "Stanford University", "Princeton University", "University of Cambridge", "University of Oxford", "University of California, Berkeley", "Imperial College London", "Yale University", "University of California, Los Angeles", "University of Chicago", "Johns Hopkins University", "Cornell University", "ETH Zurich \u2013 Swiss Federal Institute of Technology Zurich", "University of Michigan", "University of Pennsylvania", "Carnegie Mellon University", "University of Hong Kong"], "type": "scatter", "x": ["46 / 54"], "y": [18.812]}, {"marker": {"line": {"color": "black", "width": 0.1}, "size": 10}, "mode": "markers", "name": "University of Oxford", "opacity": 0.8, "text": ["California Institute of Technology", "Massachusetts Institute of Technology", "Stanford University", "Princeton University", "University of Cambridge", "University of Oxford", "University of California, Berkeley", "Imperial College London", "Yale University", "University of California, Los Angeles", "University of Chicago", "Johns Hopkins University", "Cornell University", "ETH Zurich \u2013 Swiss Federal Institute of Technology Zurich", "University of Michigan", "University of Pennsylvania", "Carnegie Mellon University", "University of Hong Kong"], "type": "scatter", "x": ["46 / 54"], "y": [19.919]}, {"marker": {"line": {"color": "black", "width": 0.1}, "size": 10}, "mode": "markers", "name": "University of California, Berkeley", "opacity": 0.8, "text": ["California Institute of Technology", "Massachusetts Institute of Technology", "Stanford University", "Princeton University", "University of Cambridge", "University of Oxford", "University of California, Berkeley", "Imperial College London", "Yale University", "University of California, Los Angeles", "University of Chicago", "Johns Hopkins University", "Cornell University", "ETH Zurich \u2013 Swiss Federal Institute of Technology Zurich", "University of Michigan", "University of Pennsylvania", "Carnegie Mellon University", "University of Hong Kong"], "type": "scatter", "x": ["50 / 50"], "y": [36.186]}, {"marker": {"line": {"color": "black", "width": 0.1}, "size": 10}, "mode": "markers", "name": "Imperial College London", "opacity": 0.8, "text": ["California Institute of Technology", "Massachusetts Institute of Technology", "Stanford University", "Princeton University", "University of Cambridge", "University of Oxford", "University of California, Berkeley", "Imperial College London", "Yale University", "University of California, Los Angeles", "University of Chicago", "Johns Hopkins University", "Cornell University", "ETH Zurich \u2013 Swiss Federal Institute of Technology Zurich", "University of Michigan", "University of Pennsylvania", "Carnegie Mellon University", "University of Hong Kong"], "type": "scatter", "x": ["37 / 63"], "y": [15.06]}, {"marker": {"line": {"color": "black", "width": 0.1}, "size": 10}, "mode": "markers", "name": "Yale University", "opacity": 0.8, "text": ["California Institute of Technology", "Massachusetts Institute of Technology", "Stanford University", "Princeton University", "University of Cambridge", "University of Oxford", "University of California, Berkeley", "Imperial College London", "Yale University", "University of California, Los Angeles", "University of Chicago", "Johns Hopkins University", "Cornell University", "ETH Zurich \u2013 Swiss Federal Institute of Technology Zurich", "University of Michigan", "University of Pennsylvania", "Carnegie Mellon University", "University of Hong Kong"], "type": "scatter", "x": ["50 / 50"], "y": [11.751]}, {"marker": {"line": {"color": "black", "width": 0.1}, "size": 10}, "mode": "markers", "name": "University of California, Los Angeles", "opacity": 0.8, "text": ["California Institute of Technology", "Massachusetts Institute of Technology", "Stanford University", "Princeton University", "University of Cambridge", "University of Oxford", "University of California, Berkeley", "Imperial College London", "Yale University", "University of California, Los Angeles", "University of Chicago", "Johns Hopkins University", "Cornell University", "ETH Zurich \u2013 Swiss Federal Institute of Technology Zurich", "University of Michigan", "University of Pennsylvania", "Carnegie Mellon University", "University of Hong Kong"], "type": "scatter", "x": ["52 / 48"], "y": [38.206]}, {"marker": {"line": {"color": "black", "width": 0.1}, "size": 10}, "mode": "markers", "name": "University of Chicago", "opacity": 0.8, "text": ["California Institute of Technology", "Massachusetts Institute of Technology", "Stanford University", "Princeton University", "University of Cambridge", "University of Oxford", "University of California, Berkeley", "Imperial College London", "Yale University", "University of California, Los Angeles", "University of Chicago", "Johns Hopkins University", "Cornell University", "ETH Zurich \u2013 Swiss Federal Institute of Technology Zurich", "University of Michigan", "University of Pennsylvania", "Carnegie Mellon University", "University of Hong Kong"], "type": "scatter", "x": ["42 / 58"], "y": [14.221]}, {"marker": {"line": {"color": "black", "width": 0.1}, "size": 10}, "mode": "markers", "name": "Johns Hopkins University", "opacity": 0.8, "text": ["California Institute of Technology", "Massachusetts Institute of Technology", "Stanford University", "Princeton University", "University of Cambridge", "University of Oxford", "University of California, Berkeley", "Imperial College London", "Yale University", "University of California, Los Angeles", "University of Chicago", "Johns Hopkins University", "Cornell University", "ETH Zurich \u2013 Swiss Federal Institute of Technology Zurich", "University of Michigan", "University of Pennsylvania", "Carnegie Mellon University", "University of Hong Kong"], "type": "scatter", "x": ["50 / 50"], "y": [15.128]}, {"marker": {"line": {"color": "black", "width": 0.1}, "size": 10}, "mode": "markers", "name": "Cornell University", "opacity": 0.8, "text": ["California Institute of Technology", "Massachusetts Institute of Technology", "Stanford University", "Princeton University", "University of Cambridge", "University of Oxford", "University of California, Berkeley", "Imperial College London", "Yale University", "University of California, Los Angeles", "University of Chicago", "Johns Hopkins University", "Cornell University", "ETH Zurich \u2013 Swiss Federal Institute of Technology Zurich", "University of Michigan", "University of Pennsylvania", "Carnegie Mellon University", "University of Hong Kong"], "type": "scatter", "x": ["48 / 52"], "y": [21.424]}, {"marker": {"line": {"color": "black", "width": 0.1}, "size": 10}, "mode": "markers", "name": "ETH Zurich \u2013 Swiss Federal Institute of Technology Zurich", "opacity": 0.8, "text": ["California Institute of Technology", "Massachusetts Institute of Technology", "Stanford University", "Princeton University", "University of Cambridge", "University of Oxford", "University of California, Berkeley", "Imperial College London", "Yale University", "University of California, Los Angeles", "University of Chicago", "Johns Hopkins University", "Cornell University", "ETH Zurich \u2013 Swiss Federal Institute of Technology Zurich", "University of Michigan", "University of Pennsylvania", "Carnegie Mellon University", "University of Hong Kong"], "type": "scatter", "x": ["31 / 69"], "y": [18.178]}, {"marker": {"line": {"color": "black", "width": 0.1}, "size": 10}, "mode": "markers", "name": "University of Michigan", "opacity": 0.8, "text": ["California Institute of Technology", "Massachusetts Institute of Technology", "Stanford University", "Princeton University", "University of Cambridge", "University of Oxford", "University of California, Berkeley", "Imperial College London", "Yale University", "University of California, Los Angeles", "University of Chicago", "Johns Hopkins University", "Cornell University", "ETH Zurich \u2013 Swiss Federal Institute of Technology Zurich", "University of Michigan", "University of Pennsylvania", "Carnegie Mellon University", "University of Hong Kong"], "type": "scatter", "x": ["48 / 52"], "y": [41.786]}, {"marker": {"line": {"color": "black", "width": 0.1}, "size": 10}, "mode": "markers", "name": "University of Pennsylvania", "opacity": 0.8, "text": ["California Institute of Technology", "Massachusetts Institute of Technology", "Stanford University", "Princeton University", "University of Cambridge", "University of Oxford", "University of California, Berkeley", "Imperial College London", "Yale University", "University of California, Los Angeles", "University of Chicago", "Johns Hopkins University", "Cornell University", "ETH Zurich \u2013 Swiss Federal Institute of Technology Zurich", "University of Michigan", "University of Pennsylvania", "Carnegie Mellon University", "University of Hong Kong"], "type": "scatter", "x": ["51 / 49"], "y": [20.376]}, {"marker": {"line": {"color": "black", "width": 0.1}, "size": 10}, "mode": "markers", "name": "Carnegie Mellon University", "opacity": 0.8, "text": ["California Institute of Technology", "Massachusetts Institute of Technology", "Stanford University", "Princeton University", "University of Cambridge", "University of Oxford", "University of California, Berkeley", "Imperial College London", "Yale University", "University of California, Los Angeles", "University of Chicago", "Johns Hopkins University", "Cornell University", "ETH Zurich \u2013 Swiss Federal Institute of Technology Zurich", "University of Michigan", "University of Pennsylvania", "Carnegie Mellon University", "University of Hong Kong"], "type": "scatter", "x": ["39 / 61"], "y": [11.885]}, {"marker": {"line": {"color": "black", "width": 0.1}, "size": 10}, "mode": "markers", "name": "University of Hong Kong", "opacity": 0.8, "text": ["California Institute of Technology", "Massachusetts Institute of Technology", "Stanford University", "Princeton University", "University of Cambridge", "University of Oxford", "University of California, Berkeley", "Imperial College London", "Yale University", "University of California, Los Angeles", "University of Chicago", "Johns Hopkins University", "Cornell University", "ETH Zurich \u2013 Swiss Federal Institute of Technology Zurich", "University of Michigan", "University of Pennsylvania", "Carnegie Mellon University", "University of Hong Kong"], "type": "scatter", "x": ["53 / 47"], "y": [19.835]}],
                        {"hovermode": "closest", "legend": {"x": 0.2, "y": -2}, "margin": {"b": 130, "l": 30, "r": 50, "t": 50}, "template": {"data": {"bar": [{"error_x": {"color": "#2a3f5f"}, "error_y": {"color": "#2a3f5f"}, "marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "bar"}], "barpolar": [{"marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "barpolar"}], "carpet": [{"aaxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "baxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "type": "carpet"}], "choropleth": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "choropleth"}], "contour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "contour"}], "contourcarpet": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "contourcarpet"}], "heatmap": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmap"}], "heatmapgl": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmapgl"}], "histogram": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "histogram"}], "histogram2d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2d"}], "histogram2dcontour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2dcontour"}], "mesh3d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "mesh3d"}], "parcoords": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "parcoords"}], "pie": [{"automargin": true, "type": "pie"}], "scatter": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter"}], "scatter3d": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter3d"}], "scattercarpet": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattercarpet"}], "scattergeo": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergeo"}], "scattergl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergl"}], "scattermapbox": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattermapbox"}], "scatterpolar": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolar"}], "scatterpolargl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolargl"}], "scatterternary": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterternary"}], "surface": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "surface"}], "table": [{"cells": {"fill": {"color": "#EBF0F8"}, "line": {"color": "white"}}, "header": {"fill": {"color": "#C8D4E3"}, "line": {"color": "white"}}, "type": "table"}]}, "layout": {"annotationdefaults": {"arrowcolor": "#2a3f5f", "arrowhead": 0, "arrowwidth": 1}, "coloraxis": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "colorscale": {"diverging": [[0, "#8e0152"], [0.1, "#c51b7d"], [0.2, "#de77ae"], [0.3, "#f1b6da"], [0.4, "#fde0ef"], [0.5, "#f7f7f7"], [0.6, "#e6f5d0"], [0.7, "#b8e186"], [0.8, "#7fbc41"], [0.9, "#4d9221"], [1, "#276419"]], "sequential": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "sequentialminus": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]]}, "colorway": ["#636efa", "#EF553B", "#00cc96", "#ab63fa", "#FFA15A", "#19d3f3", "#FF6692", "#B6E880", "#FF97FF", "#FECB52"], "font": {"color": "#2a3f5f"}, "geo": {"bgcolor": "white", "lakecolor": "white", "landcolor": "#E5ECF6", "showlakes": true, "showland": true, "subunitcolor": "white"}, "hoverlabel": {"align": "left"}, "hovermode": "closest", "mapbox": {"style": "light"}, "paper_bgcolor": "white", "plot_bgcolor": "#E5ECF6", "polar": {"angularaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "radialaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "scene": {"xaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "yaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "zaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}}, "shapedefaults": {"line": {"color": "#2a3f5f"}}, "ternary": {"aaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "baxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "caxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "title": {"x": 0.05}, "xaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "title": {"standoff": 15}, "zerolinecolor": "white", "zerolinewidth": 2}, "yaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "title": {"standoff": 15}, "zerolinecolor": "white", "zerolinewidth": 2}}}, "xaxis": {"title": {"text": "Ratio \u00e9tudiants f\u00e9minin / \u00e9tudiants masculin"}}, "yaxis": {"title": {"text": "Nombre \u00e9tudiants Total"}}},
                        {"responsive": true}
                    ).then(function(){

var gd = document.getElementById('44994af2-7420-4db0-81b0-d4f618df1b29');
var x = new MutationObserver(function (mutations, observer) {{
        var display = window.getComputedStyle(gd).display;
        if (!display || display === 'none') {{
            console.log([gd, 'removed!']);
            Plotly.purge(gd);
            observer.disconnect();
        }}
}});

// Listen for the removal of the full notebook cells
var notebookContainer = gd.closest('#notebook-container');
if (notebookContainer) {{
    x.observe(notebookContainer, {childList: true});
}}

// Listen for the clearing of the current output cell
var outputEl = gd.closest('.output');
if (outputEl) {{
    x.observe(outputEl, {childList: true});
}}

                        })
                };
                });
            </script>
        </div>



```python
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
```


<div>


            <div id="24491632-f94a-40ab-b810-65085b300a5a" class="plotly-graph-div" style="height:525px; width:100%;"></div>
            <script type="text/javascript">
                require(["plotly"], function(Plotly) {
                    window.PLOTLYENV=window.PLOTLYENV || {};

                if (document.getElementById("24491632-f94a-40ab-b810-65085b300a5a")) {
                    Plotly.newPlot(
                        '24491632-f94a-40ab-b810-65085b300a5a',
                        [{"marker": {"color": [2.243, 11.074, 15.596, 7.929, 18.812, 19.919, 36.186, 15.06, 11.751, 38.206, 14.221, 15.128, 21.424, 18.178, 41.786, 20.376, 11.885, 19.835], "showscale": true, "size": [2.243, 11.074, 15.596, 7.929, 18.812, 19.919, 36.186, 15.06, 11.751, 38.206, 14.221, 15.128, 21.424, 18.178, 41.786, 20.376, 11.885, 19.835]}, "mode": "markers", "text": ["California Institute of Technology", "Massachusetts Institute of Technology", "Stanford University", "Princeton University", "University of Cambridge", "University of Oxford", "University of California, Berkeley", "Imperial College London", "Yale University", "University of California, Los Angeles", "University of Chicago", "Johns Hopkins University", "Cornell University", "ETH Zurich \u2013 Swiss Federal Institute of Technology Zurich", "University of Michigan", "University of Pennsylvania", "Carnegie Mellon University", "University of Hong Kong"], "type": "scatter", "x": ["33 / 67", "37 / 63", "42 / 58", "45 / 55", "46 / 54", "46 / 54", "50 / 50", "37 / 63", "50 / 50", "52 / 48", "42 / 58", "50 / 50", "48 / 52", "31 / 69", "48 / 52", "51 / 49", "39 / 61", "53 / 47"], "y": [2.243, 11.074, 15.596, 7.929, 18.812, 19.919, 36.186, 15.06, 11.751, 38.206, 14.221, 15.128, 21.424, 18.178, 41.786, 20.376, 11.885, 19.835]}],
                        {"template": {"data": {"bar": [{"error_x": {"color": "#2a3f5f"}, "error_y": {"color": "#2a3f5f"}, "marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "bar"}], "barpolar": [{"marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "barpolar"}], "carpet": [{"aaxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "baxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "type": "carpet"}], "choropleth": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "choropleth"}], "contour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "contour"}], "contourcarpet": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "contourcarpet"}], "heatmap": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmap"}], "heatmapgl": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmapgl"}], "histogram": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "histogram"}], "histogram2d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2d"}], "histogram2dcontour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2dcontour"}], "mesh3d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "mesh3d"}], "parcoords": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "parcoords"}], "pie": [{"automargin": true, "type": "pie"}], "scatter": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter"}], "scatter3d": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter3d"}], "scattercarpet": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattercarpet"}], "scattergeo": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergeo"}], "scattergl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergl"}], "scattermapbox": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattermapbox"}], "scatterpolar": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolar"}], "scatterpolargl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolargl"}], "scatterternary": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterternary"}], "surface": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "surface"}], "table": [{"cells": {"fill": {"color": "#EBF0F8"}, "line": {"color": "white"}}, "header": {"fill": {"color": "#C8D4E3"}, "line": {"color": "white"}}, "type": "table"}]}, "layout": {"annotationdefaults": {"arrowcolor": "#2a3f5f", "arrowhead": 0, "arrowwidth": 1}, "coloraxis": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "colorscale": {"diverging": [[0, "#8e0152"], [0.1, "#c51b7d"], [0.2, "#de77ae"], [0.3, "#f1b6da"], [0.4, "#fde0ef"], [0.5, "#f7f7f7"], [0.6, "#e6f5d0"], [0.7, "#b8e186"], [0.8, "#7fbc41"], [0.9, "#4d9221"], [1, "#276419"]], "sequential": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "sequentialminus": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]]}, "colorway": ["#636efa", "#EF553B", "#00cc96", "#ab63fa", "#FFA15A", "#19d3f3", "#FF6692", "#B6E880", "#FF97FF", "#FECB52"], "font": {"color": "#2a3f5f"}, "geo": {"bgcolor": "white", "lakecolor": "white", "landcolor": "#E5ECF6", "showlakes": true, "showland": true, "subunitcolor": "white"}, "hoverlabel": {"align": "left"}, "hovermode": "closest", "mapbox": {"style": "light"}, "paper_bgcolor": "white", "plot_bgcolor": "#E5ECF6", "polar": {"angularaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "radialaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "scene": {"xaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "yaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "zaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}}, "shapedefaults": {"line": {"color": "#2a3f5f"}}, "ternary": {"aaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "baxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "caxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "title": {"x": 0.05}, "xaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "title": {"standoff": 15}, "zerolinecolor": "white", "zerolinewidth": 2}, "yaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "title": {"standoff": 15}, "zerolinecolor": "white", "zerolinewidth": 2}}}, "title": {"text": "Le nombre d\u2019\u00e9tudiants total en fonction du Ratio \u00e9tudiant f\u00e9minin / \u00e9tudiant masculin"}, "xaxis": {"title": {"text": "Ratio \u00e9tudiants f\u00e9minin / \u00e9tudiants masculin"}}, "yaxis": {"title": {"text": "Nombre \u00e9tudiants Total"}}},
                        {"responsive": true}
                    ).then(function(){

var gd = document.getElementById('24491632-f94a-40ab-b810-65085b300a5a');
var x = new MutationObserver(function (mutations, observer) {{
        var display = window.getComputedStyle(gd).display;
        if (!display || display === 'none') {{
            console.log([gd, 'removed!']);
            Plotly.purge(gd);
            observer.disconnect();
        }}
}});

// Listen for the removal of the full notebook cells
var notebookContainer = gd.closest('#notebook-container');
if (notebookContainer) {{
    x.observe(notebookContainer, {childList: true});
}}

// Listen for the clearing of the current output cell
var outputEl = gd.closest('.output');
if (outputEl) {{
    x.observe(outputEl, {childList: true});
}}

                        })
                };
                });
            </script>
        </div>



```python

```
