import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
    'display':'inline-block',
}

layout = html.Div(
    [
        # html.H6('CONFIRMED'),
        # html.H3(id='confirmed-number'),
        # html.P('Active'),
        # html.P(id='active-number'),
        # html.P('Recovered'),
        # html.P(id='recovered-number'),
        # html.P('Fatal'),
        # html.P(id='fatal-number'),

        html.P(
            "A simple sidebar layout with navigation links", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Page 1", href="/page-1", id="page-1-link"),
                dbc.NavLink("Page 2", href="/page-2", id="page-2-link"),
                dbc.NavLink("Page 3", href="/page-3", id="page-3-link"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)
