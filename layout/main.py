import dash
import plotly
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import pandas
from dash.dependencies import Input, Output
from datetime import date

from app import app

from database import transforms

# load data
df_con = transforms.df_con
df_rec = transforms.df_rec
df_fat = transforms.df_fat
df_act = transforms.df_act

MAIN_STYLE = {
    "margin-left": "16rem",
    "margin-right": "2rem",
    # "padding": "0rem 0rem",
}

# variables
today = date.today()
# add (All) to show world data
countries = ['(All)'] + df_con['Country/Region'].dropna().unique().tolist()
states = ['(All)'] + df_con['Province/State'].dropna().unique().tolist()
colors = {
    'background': 'rgb(40, 51, 74)',
    'text': 'rgb(255,255,255)'
}

layout = html.Div([

    html.Div([
        html.H2([
            'COVID-19 CASES - DASHBOARD',
        ]),
        html.P([
            today.strftime("%A, %B %d, %Y")
        ]),
    ], style={'backgroundColor':colors['background'],'color':colors['text']}),

    # choose options
    html.Div([

        # choose total or new cases
        html.Div([
            'Select Metric'
        ], style={'width':'6rem','display':'inline-block','verticalAlign':'top'}),
        html.Div([
            dcc.Dropdown(
                id='total-new-dropdown',
                options=[
                    {'label':'Total Cases', 'value':'total'},
                    {'label':'New Cases', 'value':'new'}
                ],
                value='total'
            )
        ], style={'width':'20%','display':'inline-block','verticalAlign':'top'}),

        # choose country
        html.Div([
            'Select Country'
        ], style={'display':'inline-block','verticalAlign':'top'}),
        html.Div([
            dcc.Dropdown(
                id='country-dropdown',
                options=[
                    {'label': country, 'value': country}
                    for country in countries
                ],
                value='(All)'
            )
        ], style={'width':'20%','display':'inline-block','verticalAlign':'top'}),

        # choose state
        html.Div([
            'Select State'
        ], style={'display':'inline-block','verticalAlign':'top'}),
        html.Div([
            dcc.Dropdown(
                id='state-dropdown',
            )
        ], style={'width':'20%','display':'inline-block','verticalAlign':'top'}),

    ]),
    html.Hr(),

    # bar graphs
    html.Div([

        # confirmed bar
        html.Div([
            html.H4([
                'Confirmed'
            ]),
            html.H5(
                id='confirmed-number',
            ),
            dcc.Graph(id='confirmed-graph'),
        ], style={'width':'25%','display':'inline-block','textAlign':'center'}),
        # recovered bar
        html.Div([
            html.H4([
                'Recovered'
            ]),
            html.H5(
                id='recovered-number',
            ),
            dcc.Graph(id='recovered-graph'),
        ], style={'width':'25%','display':'inline-block','textAlign':'center'}),
        # fatal bar
        html.Div([
            html.H4([
                'Fatal'
            ]),
            html.H5(
                id='fatal-number',
            ),
            dcc.Graph(id='fatal-graph'),
        ], style={'width':'25%','display':'inline-block','textAlign':'center'}),
        # active bar
        html.Div([
            html.H4([
                'Active'
            ]),
            html.H5(
                id='active-number',
            ),
            dcc.Graph(id='active-graph'),
        ], style={'width':'25%','display':'inline-block','textAlign':'center'}),

    ]),
    html.Hr(),

    # maps
    html.Div([
        dcc.Graph(id='map-graph')
    ], style={'width':'100%','display':'flex','align-items':'center','justify-content':'center'})

], style=MAIN_STYLE)
