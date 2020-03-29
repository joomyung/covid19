import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": "5rem",
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
    'display':'inline-block',
}

layout = html.Div([

    html.Div([
        "Global",
    ], style={'width':'50%','display':'inline-block'}),
    html.Div([
        "523232",
    ], style={'textAlign':'right','width':'50%','display':'inline-block'}),

    html.Hr(),

], style=SIDEBAR_STYLE)
