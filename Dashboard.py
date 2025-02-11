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

# Callbacks ***************************************************************************
fig = px.bar(df, x='Companies',
             y='Earnings_Growth', title=f'Magnificent Graph about Valuation, Growth and Margins',
             labels={'Companies': "Companies", 'Earnings_Growth': 'Earnings Growth(%)'})
fig.update_traces(marker_color='green')
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

app.layout = html.Div([
    dcc.Graph(
        id='Magnificent Graph about Valuation, Growth and Margins',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
