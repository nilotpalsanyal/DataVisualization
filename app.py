import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)

df = px.data.iris()

app.layout = html.Div([
    html.H1("Dash Components Example", style={'text-align': 'center'}),

    # Dropdown component
    html.Div([
        html.Label("Select a species:"),
        dcc.Dropdown(
            id='species-dropdown',
            options=[{'label': species, 'value': species} for species in df['species'].unique()],
            value='setosa'
        )
    ], style={'width': '50%', 'padding': '10px', 'margin': '10px'}),

    # Text component 
    html.Div([
        html.Label("Enter your name:"),
        dcc.Input(id='name-input', type='text', placeholder='Enter your name')
    ], style={'padding': '10px', 'margin': '10px'}),

    # Slider component
    html.Div([
        html.Label("Select a number:"),
        dcc.Slider(
            id='slider-input',
            min=0,
            max=100,
            step=1,
            value=50,
            marks={i: str(i) for i in range(0, 101, 10)}
        )
    ], style={'padding': '10px', 'margin': '10px'}),

    # RangeSlider component
    html.Div([
        html.Label("Select a range:"),
        dcc.RangeSlider(
            id='range-slider-input',
            min=0,
            max=100,
            step=1,
            value=[20, 80],
            marks={i: str(i) for i in range(0, 101, 10)}
        )
    ], style={'padding': '10px', 'margin': '10px'}),

    # DatePickerSingle component
    html.Div([
        html.Label("Pick a date:"),
        dcc.DatePickerSingle(
            id='date-picker-single',
            date='2024-11-06'
        )
    ], style={'padding': '10px', 'margin': '10px'}),

    # DatePickerRange component
    html.Div([
        html.Label("Pick a date range:"),
        dcc.DatePickerRange(
            id='date-picker-range',
            start_date='2024-01-01',
            end_date='2024-12-31',
            display_format='YYYY-MM-DD'
        )
    ], style={'padding': '10px', 'margin': '10px'}),

    # Checklist component
    html.Div([
        html.Label("Select options:"),
        dcc.Checklist(
            id='checklist-input',
            options=[{'label': f'Option {i}', 'value': f'opt{i}'} for i in range(1, 4)],
            value=['opt1']
        )
    ], style={'padding': '10px', 'margin': '10px'}),

    # RadioItems component
    html.Div([
        html.Label("Select a choice:"),
        dcc.RadioItems(
            id='radio-items-input',
            options=[{'label': f'Choice {i}', 'value': f'choice{i}'} for i in range(1, 4)],
            value='choice1'
        )
    ], style={'padding': '10px', 'margin': '10px'}),

    # Markdown component
    html.Div([
        html.Label("Formatted text using Markdown:"),
        dcc.Markdown("""
            **This is a markdown text**
            - Bullet point 1
            - Bullet point 2
        """)
    ], style={'padding': '10px', 'margin': '10px'}),

    # Textarea component
    html.Div([
        html.Label("Enter multiline text:"),
        dcc.Textarea(
            id='textarea-input',
            value='This is some initial text.',
            style={'width': '100%', 'height': 100}
        )
    ], style={'padding': '10px', 'margin': '10px'}),

    # Tabs component
    dcc.Tabs([
        dcc.Tab(label='Tab 1', children=[
            html.Div([
                html.Label("Tab 1 Content")
            ])
        ]),
        dcc.Tab(label='Tab 2', children=[
            html.Div([
                html.Label("Tab 2 Content")
            ])
        ]),
    ], style={'padding': '10px', 'margin': '10px'}),

    # Graph component
    html.Div([
        html.Label("Scatter plot of Iris dataset:"),
        dcc.Graph(
            id='iris-graph',
            figure=px.scatter(df, x='sepal_width', y='sepal_length', color='species')
        )
    ], style={'padding': '10px', 'margin': '10px'}),

    # File Upload component
    html.Div([
        html.Label("Upload a file:"),
        dcc.Upload(
            id='upload-data',
            children=html.Button('Upload File'),
            multiple=False
        )
    ], style={'padding': '10px', 'margin': '10px'}),

    # Store component
    dcc.Store(id='store-data'),

    # Location component
    dcc.Location(id='url', refresh=False),

    # Interval component
    dcc.Interval(
        id='interval-component',
        interval=1000,  # in milliseconds
        n_intervals=0
    ),

    # Loading component
    html.Div([
        dcc.Loading(
            id="loading-1",
            children=[html.Div(id="loading-output-1")],
            type="circle"
        )
    ], style={'padding': '10px', 'margin': '10px'})
], style={'width':'40%', 'padding-left':'30%'})


@app.callback(
    Output('loading-output-1', 'children'),
    Input('interval-component', 'n_intervals')
)
def update_loading_output(n):
    return f"Interval count: {n}"


if __name__ == '__main__':
    app.run_server(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
