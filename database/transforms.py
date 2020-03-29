import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import dash
from dash.dependencies import Input, Output
import pandas as pd

# read data
# url_con = 'csse_covid_19_time_series/time_series_19-covid-Confirmed.csv'
# url_rec = 'csse_covid_19_time_series/time_series_19-covid-Recovered.csv'
# url_fat = 'csse_covid_19_time_series/time_series_19-covid-Deaths.csv'

url_con = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
url_rec = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv'
url_fat = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv'

df_con = pd.read_csv(url_con)
df_rec = pd.read_csv(url_rec)
df_fat = pd.read_csv(url_fat)

df_act = df_con.copy() # active = confirmed - recovered - fatal
df_act.iloc[:, 4:] = df_act.iloc[:, 4:] - df_rec.iloc[:, 4:] - df_fat.iloc[:, 4:]
