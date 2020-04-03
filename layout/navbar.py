import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from datetime import date

# variables
today = date.today()
colors = {
    'background': 'rgb(40, 51, 74)',
    'text': 'rgb(255,255,255)'
}

# style
NAVBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "width": "100%",
    "background-color": colors['background'],
    "color": colors['text'],
}

# layout
layout = html.Div([

    html.Div([
        html.H2([
            'COVID-19 CASES - DASHBOARD',
        ]),
        html.P([
            today.strftime("%A, %B %d, %Y")
        ]),
        # html.P(id='test-output'),
    ], style={'margin-left':'10px'})

], style=NAVBAR_STYLE)
