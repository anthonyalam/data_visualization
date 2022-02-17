# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.read_csv("/Users/anthonyalam/Desktop/data_visulisation/PS4_GamesSales.csv",encoding= 'unicode_escape')

fig = px.bar(df, x = "North America", y = "Genre")
fig3 = px.bar(df, x = "Japan", y = "Genre")
fig1 = px.bar(df, x = "Publisher", y = "Genre")
fig2 = px.pie(df, names = 'Genre', values= 'Global')
fig4 = px.scatter(df, x = 'Year' , y = 'Genre',size = 'Global')
fig5 = px.bar_polar(df, r = 'Europe' , theta = 'Genre')

app.layout = html.Div(children=[
    html.H1(children='Data Visulisation'),

    html.Div(children='''
        Enjoy your data
    '''),

    dcc.Graph(
        id='fig',
        figure=fig

    ),
    dcc.Graph(
        id='fig3',
        figure=fig3
    ),
    dcc.Graph(
        id='fig1',
        figure=fig1
    ),
    dcc.Graph(
        id='fig2',
        figure=fig2
    ),
    dcc.Graph(
        id='fig4',
        figure=fig4
    ),
    dcc.Graph(
        id='fig5',
        figure=fig5
    ),

])

if __name__ == '__main__':
    app.run_server(debug=True)