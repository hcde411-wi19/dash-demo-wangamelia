# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np
import pandas as pd

weekday_in_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
counts_in_order = [160613, 154225, 155175, 150819, 146014, 215725, 203483]
ped_s = [28686, 27520, 27224, 25846, 24900, 37808, 34792]
ped_n = [26884, 26444, 25876, 24368, 23403, 36894, 32792]
bike_s = [52642, 50812, 51866, 50913, 49740, 71586, 68147]
bike_n = [52401, 49449, 50209, 49692, 47971, 69437, 67752]
# initialize Dash app and initialize the static folder
app = dash.Dash(__name__, static_folder='static')

trace1 = go.Scatter(x=weekday_in_order, y=counts_in_order, name='counts')
trace2 = go.Scatter(x=weekday_in_order, y=ped_s, name='ped s')
trace3 = go.Scatter(x=weekday_in_order, y=ped_n, name='ped n')
trace4 =go.Scatter(x=weekday_in_order, y=bike_s, name='bike s')
trace5 = go.Scatter(x=weekday_in_order, y=bike_n, name='bike n')


# define lines - for each usage data, we create a line series through go.Scatter with mode 'lines+markers'
series = [trace1, trace2, trace3, trace4, trace5]


# set layout of the page
app.layout = html.Div(children=[

    # set the page heading
    html.H1(children='L2 Line Chart'),

    # set the description underneath the heading
    html.Div(children='''
        Exercise2 as a line chart.
    '''),

    # append the visualization to the page
    dcc.Graph(
        id='example-graph',
        figure={
            # configure the data
            'data': series,
            'layout': 
            	go.Layout(title='Usage of BGT North of NE 70th per week day', barmode='stack')
        }
    )

])


if __name__ == '__main__':
    app.run_server(debug=True)