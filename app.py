from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd

# init
app = Dash(__name__)

# load data
df = pd.read_csv('formatted_data.csv')

# sort data by date
df['date'] = pd.to_datetime(df['date'])
df = df.sort_values(by='date')

# make line chart
fig = px.line(
    df, 
    x='date', 
    y='sales', 
    title='Pink Morsel Sales Before and After Price Increase',
    labels={'date': 'Date', 'sales': 'Total Sales ($)'} # Adding clear axis labels
)

# layout
app.layout = html.Div(children=[
    html.H1(
        children='Soul Foods: Pink Morsel Sales Visualizer',
        style={'textAlign': 'center'}
    ),
    dcc.Graph(
        id='sales-line-chart',
        figure=fig
    )
])

# run server
if __name__ == '__main__':
    app.run(debug=True)