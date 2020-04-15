import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import dash
from dash.dependencies import Input, Output
import pandas as pd

# read data
url_con = 'database/time_series_covid19_confirmed_global.csv'
url_rec = 'database/time_series_covid19_recovered_global.csv'
url_fat = 'database/time_series_covid19_deaths_global.csv'

df_con = pd.read_csv(url_con)
df_rec = pd.read_csv(url_rec)
df_fat = pd.read_csv(url_fat)

# drop an error data
df_con = df_con.drop(index=231)
df_rec = df_rec.drop(index=231)
df_fat = df_fat.drop(index=231)

df_act = df_con.copy() # active = confirmed - recovered - fatal
df_act.iloc[:, 4:] = df_act.iloc[:, 4:] - df_rec.iloc[:, 4:] - df_fat.iloc[:, 4:]
