import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output

# Creating the data
data_set = {'Companies': ['Tesla', 'Amazon', 'Apple', 'Alphabet', 'Microsoft', 'Meta', 'Nvidia'],
            'Earnings_Growth': [7.30, 9.29, 24.30, 28.60, 35.43, 37.91, 55.69]}

df = pd.DataFrame(data_set)
print(df)

# App Layout **************************************************************************
# this goes to styles.css and tells it what to do!
stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
app = Dash(__name__, external_stylesheets=stylesheets)

# dcc provides a wide range of components like dropdowns,
# sliders, input boxes, graphs, date pickers, and more, allowing users to interact with your app
app.layout = html.Div([
    dcc.Dropdown(id='site-dropdown',
                 options=[{'label': company, 'value': company} for company in df['Companies'].unique()],
                 value=df['Companies'].unique()[0]  # default to one site
                 ), dcc.Graph(id='Magnificent Graph about Valuation, Growth and Margins')
])

# Callbacks ***************************************************************************
@app.callback(
    Output('Magnificent Graph about Valuation, Growth and Margins', 'figure'),
              Input('site-dropdown', 'value')
              )
def update_graph(selected_company):
    filtered_df = df[df['Earnings Growth in Percentage'] == selected_company]
    fig = px.bar(filtered_df, x='Companies',
                 y='Earnings_Growth', color='Companies', title=f'Magnificent Graph about Valuation, Growth and Margins',
                 labels={'Companies': "Companies", 'Earnings_Growth': 'Earnings Growth(%)'})
    fig.update_layout(
        title={
            'text': f'Magnificent Graph about Valuation, Growth and Margins',
            'y': 0.9,  # vertical position
            'x': 0.5,  # Center the Title
            'xanchor': 'center',
            'yanchor': 'top',
            'font': {
                'size': 25,
                'family': 'Arial, sans-serif',
                'color': 'black',
                'weight': 'bold'

            }
        }
    )
    return fig

if __name__ == 'main':
    app.run_server(debug=True)