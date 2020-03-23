import pandas as pd
import numpy as np
import plotly.graph_objs as go
import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

from app import app
from layout import main, sidebar
from database import transforms

# load data
df_con = transforms.df_con
df_rec = transforms.df_rec
df_fat = transforms.df_fat
df_act = transforms.df_act

# variables
scale = 10 # map scale
# countries having states in dictionary
countries_states = {}
countries_having_states = df_con[df_con['Province/State'].notnull()]['Country/Region'].unique()
for country in countries_having_states:
    countries_states[country] = ['(All)'] + df_con[df_con['Country/Region']==country]['Province/State'].tolist()

# layout
app.layout = html.Div([
    main.layout,
    sidebar.layout,
])

# country-dropdown -> state-dropdown
@app.callback(
    dash.dependencies.Output('state-dropdown', 'options'),
    [dash.dependencies.Input('country-dropdown', 'value')])
def set_states_options(country_value):
    if country_value in countries_having_states:
        return [{'label': state, 'value': state} for state in countries_states[country_value]]
    else:
        return [{'label': '(All)', 'value': '(All)'}]

@app.callback(
    dash.dependencies.Output('state-dropdown', 'value'),
    [dash.dependencies.Input('state-dropdown', 'options')])
def set_cities_value(available_options):
    return available_options[0]['value']

# map
@app.callback(
    Output('map-graph', 'figure'),
    [Input('country-dropdown', 'value')]
)
def callback_map_graph(country_value):
    return {
        'data': [ go.Scattergeo(
            lon = df_con['Long'],
            lat = df_con['Lat'],
            text = df_con['Country/Region'] + '<br>' + df_con.iloc[:, -1].astype(str),
            mode = 'markers',
            marker = {
                'size': df_con.iloc[:, -1].dropna()/scale,
                'opacity': 0.5,
                'sizemode': 'area',
                'color': 'rgb(255, 0, 0)',
            }
        )],
        'layout': {
            'title': 'Confirmed Number of COVID-19 Cases',
            'autosize': False,
            'width': '1200',
            'height': '600',
            'geo': {
                'showland': True,
                'landcolor': 'rgb(217, 217, 217)',
            }
        }
    }

# confirmed number
@app.callback(
    Output('confirmed-number', 'children'),
    [Input('country-dropdown', 'value')]
)
def callback_confirmed_number(country_value):
    if country_value == '(All)':
        return df_con.iloc[:, 4:].sum()[-1]
    else:
        return df_con[df_con['Country/Region']==country_value].iloc[:, 4:].sum()[-1]

# recovered number
@app.callback(
    Output('recovered-number', 'children'),
    [Input('country-dropdown', 'value')]
)
def callback_recovered_number(country_value):
    if country_value == '(All)':
        return df_rec.iloc[:, 4:].sum()[-1]
    else:
        return df_rec[df_rec['Country/Region']==country_value].iloc[:, 4:].sum()[-1]

# fatal number
@app.callback(
    Output('fatal-number', 'children'),
    [Input('country-dropdown', 'value')]
)
def callback_fatal_number(country_value):
    if country_value == '(All)':
        return df_fat.iloc[:, 4:].sum()[-1]
    else:
        return df_fat[df_fat['Country/Region']==country_value].iloc[:, 4:].sum()[-1]

# active number
@app.callback(
    Output('active-number', 'children'),
    [Input('country-dropdown', 'value')]
)
def callback_active_number(country_value):
    if country_value == '(All)':
        return df_act.iloc[:, 4:].sum()[-1]
    else:
        return df_act[df_act['Country/Region']==country_value].iloc[:, 4:].sum()[-1]

# subject graph
@app.callback(
    Output('confirmed-graph', 'figure'),
    [Input('country-dropdown', 'value')]
)
def callback_confirmed_graph(country_value):
    if country_value == '(All)':
        return {
            'data': [
                go.Bar(
                    x = df_con.columns[4:],
                    y = df_con.iloc[:, 4:].sum()
                )
            ],
            'layout': go.Layout(
                xaxis = {'title': 'Date'},
                yaxis = {'title': '# of Patients'},
                hovermode = 'closest'
            )
        }
    else:
        return {
            'data': [
                go.Bar(
                    x = df_con.columns[4:],
                    y = df_con[df_con['Country/Region']==country_value].iloc[:, 4:].sum(),
                ),
            ],
            'layout': go.Layout(
                xaxis = {'title': 'Date'},
                yaxis = {'title': '# of Patients'},
                hovermode = 'closest',
            )
        }

# recovered graph
@app.callback(
    Output('recovered-graph', 'figure'),
    [Input('country-dropdown', 'value')]
)
def callback_recovered_graph(country_value):
    if country_value == '(All)':
        return {
            'data': [
                go.Bar(
                    x = df_rec.columns[4:],
                    y = df_rec.iloc[:, 4:].sum()
                )
            ],
            'layout': go.Layout(
                xaxis = {'title': 'Date'},
                yaxis = {'title': '# of Patients'},
                hovermode = 'closest'
            )
        }
    else:
        return {
            'data': [
                go.Bar(
                    x = df_rec.columns[4:],
                    y = df_rec[df_rec['Country/Region']==country_value].iloc[:, 4:].sum(),
                ),
            ],
            'layout': go.Layout(
                xaxis = {'title': 'Date'},
                yaxis = {'title': '# of Patients'},
                hovermode = 'closest',
            )
        }

# fatal graph
@app.callback(
    Output('fatal-graph', 'figure'),
    [Input('country-dropdown', 'value')]
)
def callback_fatal_graph(country_value):
    if country_value == '(All)':
        return {
            'data': [
                go.Bar(
                    x = df_fat.columns[4:],
                    y = df_fat.iloc[:, 4:].sum()
                )
            ],
            'layout': go.Layout(
                xaxis = {'title': 'Date'},
                yaxis = {'title': '# of Patients'},
                hovermode = 'closest'
            )
        }
    else:
        return {
            'data': [
                go.Bar(
                    x = df_fat.columns[4:],
                    y = df_fat[df_fat['Country/Region']==country_value].iloc[:, 4:].sum(),
                ),
            ],
            'layout': go.Layout(
                xaxis = {'title': 'Date'},
                yaxis = {'title': '# of Patients'},
                hovermode = 'closest',
            )
        }

# fatal graph
@app.callback(
    Output('active-graph', 'figure'),
    [Input('country-dropdown', 'value')]
)
def callback_active_graph(country_value):
    if country_value == '(All)':
        return {
            'data': [
                go.Bar(
                    x = df_act.columns[4:],
                    y = df_act.iloc[:, 4:].sum()
                )
            ],
            'layout': go.Layout(
                xaxis = {'title': 'Date'},
                yaxis = {'title': '# of Patients'},
                hovermode = 'closest'
            )
        }
    else:
        return {
            'data': [
                go.Bar(
                    x = df_act.columns[4:],
                    y = df_act[df_act['Country/Region']==country_value].iloc[:, 4:].sum(),
                ),
            ],
            'layout': go.Layout(
                xaxis = {'title': 'Date'},
                yaxis = {'title': '# of Patients'},
                hovermode = 'closest',
            )
        }

if __name__ == '__main__':
    app.run_server(debug=True)