import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from database import transforms

# load data
df_con = transforms.df_con
df_rec = transforms.df_rec
df_fat = transforms.df_fat
df_act = transforms.df_act

# add (All) to show world data
countries = ['(All)'] + df_con['Country/Region'].dropna().unique().tolist()
states = ['(All)'] + df_con['Province/State'].dropna().unique().tolist()

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

layout = html.Div([

    dbc.Button(id='global-button', children = [
        html.Div([
            "Global",
        ], style={'textAlign':'left', 'width':'50%','display':'inline-block'}),
        html.Div([
            df_con.iloc[:, 4:].sum()[-1]
        ], style={'textAlign':'right','width':'50%','display':'inline-block'}),
    ], outline=True, color='dark', size='lg', block=True),

    html.Hr(),

    html.Div(id='country-button'),

], style=SIDEBAR_STYLE)
