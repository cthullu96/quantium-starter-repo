from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd

#init
app = Dash(__name__)

# Load and sort the data
df = pd.read_csv('formatted_data.csv')
df['date'] = pd.to_datetime(df['date'])
df = df.sort_values(by='date')

# css
# colours
COLORS = {
    'primary': '#E35B89', # A nice Pink for Pink Morsels
    'background': '#F5F5F5', # Light grey background
    'text': '#333333' # Dark grey text for readability
}

#layout
app.layout = html.Div(style={'backgroundColor': COLORS['background'], 'padding': '20px', 'fontFamily': 'Arial'}, children=[
    
    # header
    html.H1(
        children='Soul Foods: Pink Morsel Sales Visualizer',
        style={'textAlign': 'center', 'color': COLORS['primary']}
    ),
    
    # radio buttons
    html.Div(children=[
        html.Label("Select Region:", style={'fontWeight': 'bold', 'color': COLORS['text'], 'marginRight': '15px'}),
        dcc.RadioItems(
            id='region-radio',
            options=[
                {'label': 'North', 'value': 'north'},
                {'label': 'East', 'value': 'east'},
                {'label': 'South', 'value': 'south'},
                {'label': 'West', 'value': 'west'},
                {'label': 'All Regions', 'value': 'all'}
            ],
            value='all', # default value
            inline=True, # buttons side-by-side
            style={'display': 'inline-block', 'color': COLORS['text']}
        )
    ], style={'textAlign': 'center', 'margin': '20px', 'fontSize': '18px'}),

    # graph
    dcc.Graph(
        id='sales-line-chart'
    )
])

#links button to graph
@app.callback(
    Output('sales-line-chart', 'figure'),
    Input('region-radio', 'value')
)
def update_graph(selected_region):
    # filter
    if selected_region == 'all':
        filtered_df = df
    else:
        filtered_df = df[df['region'] == selected_region]

    # line chart
    fig = px.line(
        filtered_df, 
        x='date', 
        y='sales', 
        title=f'Pink Morsel Sales: {selected_region.capitalize()} Region',
        labels={'date': 'Date', 'sales': 'Total Sales ($)'}
    )
    
    # add css
    fig.update_layout(
        plot_bgcolor=COLORS['background'],
        paper_bgcolor=COLORS['background'],
        font_color=COLORS['text']
    )
    fig.update_traces(line_color=COLORS['primary']) 

    return fig

# run server
if __name__ == '__main__':
    app.run(debug=True)