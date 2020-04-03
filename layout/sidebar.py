import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from database import transforms
import pandas as pd

# load data
df_con = transforms.df_con
df_rec = transforms.df_rec
df_fat = transforms.df_fat
df_act = transforms.df_act

# add (All) to show world data
countries = ['(All)'] + df_con['Country/Region'].dropna().unique().tolist()
states = ['(All)'] + df_con['Province/State'].dropna().unique().tolist()

# create country_buttons to sort country buttons
country_cases = {}
for country in countries[1:]:
    country_cases[country] = df_con[df_con['Country/Region']==country].iloc[:, 4:].sum()[-1]

dff = pd.DataFrame(country_cases.items())
dff.columns = ['Country/Region', 'Cases']
dff = dff.sort_values(by=['Cases'], ascending=False)
country_buttons = dff['Country/Region']

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "overflow-y": "scroll", # add scroll bar
    "top": "5rem",
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
    'display':'inline-block',
}

def create_country_button(country):
    return html.Div([
            html.Div(id=country+'-name', children = [
                country,
            ], style={
                'textAlign':'left',
                'display':'table-cell',
                'vertical-align': 'middle',
                'padding': 10,
            }),
            html.Div(
                dff[dff['Country/Region']==country]['Cases']
            , style={
                'textAlign':'right',
                'display':'table-cell',
                'vertical-align': 'middle',
                'padding': 10,
            }),
        ], style={
            'display': 'table',
            'border':'1px solid',
            'border-radius': '3px',
            'height': '30px',
            'width': '100%',
            'margin-bottom': 10,
        })


layout = html.Div([

    html.Div([
        html.Div(id='global-name', children = [
            "Global",
        ], style={
            'textAlign':'left',
            'display':'table-cell',
            'vertical-align': 'middle',
            'padding': 10,
        }),
        html.Div([
            df_con.iloc[:, 4:].sum()[-1]
        ], style={
            'textAlign':'right',
            'display':'table-cell',
            'vertical-align': 'middle',
            'padding': 10,
        }),
    ], style={
        'display': 'table',
        'border':'1px solid',
        'border-radius': '3px',
        'height': '45px',
        'width': '100%',
    }),

    html.Hr(),

    html.Div(
        [create_country_button(country) for country in country_buttons]
    ),

], style=SIDEBAR_STYLE)
