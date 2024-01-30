

from dash import html, dcc
import dash_admin_components as dac
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc

from function import InfosBox
from data_preparation import *
import plotly.graph_objs as go
import matplotlib.colors as mcolors

features =  ["goal_score","goal_encaisse","shots","shots_on_target","possession",
             "passes","pass_accuracy","fouls","yellow_cards","red_cards","points"]

tab_database = html.Div(
    children=[
        dbc.Row(html.H1("Database")),
        html.Div(
            children=[
                InfosBox(box_title="Number of Rows",box_value=group_stage_data1.shape[0],box_icon="list",box_color="success"),
                InfosBox(box_title="Number of Columns",box_value=len(features),box_icon="list",box_color="primary"),
                InfosBox(box_title="Target variable",box_value="Issue",box_icon="list",box_color="info")
            ],
            className="row"
        ),
        html.Div(
            children=[
                dac.SimpleBox(
                    style={"height" : "500px","width":"100%"},
                    title="Variable description",
                    children=[

                    ]
                ),
                dac.SimpleBox(
                    style={"height" : "500px","width":"100%"},
                    title="Data"
                )

            ],
            className='row'
        ),
        html.Div([
            dac.Box([
                dac.BoxHeader(
                    collapsible=False,
                    collapsed=False,
                    title="Issue distribution",
                    children=[
                        dac.BoxDropdown([
                            html.Label("Graph type",className="text-center mt-3 mb-1"),
                            html.P(),
                            dcc.RadioItems(
                                id="target-graph-value",
                                options=[
                                    {"label": [
                                        html.Img(src="/static/images/PieChart.png", height=30),
                                        html.Span("Pie Chart", style={'font-size': 15, 'padding-left': 10})
                                    ],
                                    "value" : "pie-chart"},
                                    {"label": [
                                        html.Img(src="/static/images/BarChart.png", height=30),
                                        html.Span("Bar Chart", style={'font-size': 15, 'padding-left': 10})
                                    ],
                                    "value" : "bar-chart"}],
                                value="pie-chart"
                            ),
                        ],style={"width":"100%","text-align":"left"})
                ]),
                dac.BoxBody([
                    dcc.Loading(dcc.Graph(id="target-graph-output",config=dict(displayModeBar=False),responsive=True))
                ]
                )
            ],
            solid_header=True,
            width=4),
            dac.Box([
                dac.BoxHeader(
                    collapsible=False,
                    collapsed=False,
                    title="Features distribution",
                    children=[
                        dac.BoxDropdown(
                            [
                                html.Label("Choose a feature"),
                                dcc.Dropdown(
                                    id="feature-graph-value",
                                    options=[
                                        {"label" : x, "value" : x} for x in features
                                    ],
                                    value=features[0],
                                    multi=False,
                                    placeholder='Choose a feature'
                                ),
                                html.P(),
                                dcc.RadioItems(
                                    id="feature-graph-type-value",
                                    options=[
                                        {"label": [
                                            html.Img(src="/static/images/Histogram.jpg", height=30),
                                            html.Span("Histogram", style={'font-size': 15, 'padding-left': 10})
                                        ],
                                        "value" : "histogram"},
                                        {"label": [
                                            html.Img(src="/static/images/BoxPlot.png", height=30),
                                            html.Span("Box plot", style={'font-size': 15, 'padding-left': 10})
                                        ],
                                        "value" : "box-plot"},
                                        ],
                                    value="histogram"
                                ),
                                html.P(),
                                html.Label("fill color"),
                                dcc.Dropdown(
                                    id="feature-graph-fill-value",
                                    options=[
                                        {"label" : x, "value" : x} for x in mcolors.CSS4_COLORS
                                    ],
                                    value="navy",
                                    multi=False,
                                    placeholder="Choose a fill color"
                                )
                            ],
                            style={"width":"600pv"}
                        )
                    ] 
                ),
                dac.BoxBody(dcc.Loading(dcc.Graph(id="feature-graph-output",config=dict(displayModeBar=False),responsive=True)))
            ],
            solid_header=True,
            width=4),
            dac.Box([
                dac.BoxHeader(
                    collapsible=False,
                    collapsed=False,
                    title="Distribution of feature by target",
                    children=[
                        dac.BoxDropdown(
                            [
                                html.Label("Choose a feature"),
                                dcc.Dropdown(
                                    id="feature-boxplot-graph-value",
                                    options=[
                                        {"label" : x, "value" : x} for x in features
                                    ],
                                    value=features[0],
                                    multi=False,
                                    placeholder='Choose a feature'
                                ),
                                dcc.RadioItems(
                                    id="feature-target-graph-type-value",
                                    options=[
                                        {"label": [
                                            html.Img(src="/static/images/Histogram.jpg", height=30),
                                            html.Span("Histogram", style={'font-size': 15, 'padding-left': 10})
                                        ],
                                        "value" : "histogram"},
                                        {"label": [
                                            html.Img(src="/static/images/BoxPlot.png", height=30),
                                            html.Span("Box plot", style={'font-size': 15, 'padding-left': 10})
                                        ],
                                        "value" : "box-plot"},
                                        ],
                                    value="box-plot"
                                ),
                            ]
                        )
                    ] 
                ),
                dac.BoxBody(dcc.Loading(dcc.Graph(id="feature-target-graph-output",config=dict(displayModeBar=False),responsive=True)))
            ],
            solid_header=True,
            width=4),
        ],
        className='row'),
        html.Div([
            
            dac.SimpleBox(
                style={"height" : "500px","width":"100%"},
                title="Correlation Report",
                children=[

                ],
                width=6
            ),
        ],
        className='row')
    ]
)