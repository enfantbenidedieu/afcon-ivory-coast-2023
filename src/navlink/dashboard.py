# -*- coding: utf-8 -*-

from dash import dcc, html
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
from function import *
from data_preparation import *

dashboard = html.Div(
            children=[
                html.Div(
                    children=[
                        dbc.Card(
                            children=[
                                html.Div(id="dashboard-stadium-output",className="div_center_className"),
                            ],
                            className="controls_team"
                        )
                    ]
                ),
                html.Div(
                    children=[
                        dbc.Row(
                            children=[
                                dbc.Col(
                                    children=[
                                        dbc.Card(
                                            children=[
                                                html.Label("Select a step"),
                                                dcc.Dropdown(
                                                    id="dashboard-step-value",
                                                    options=[
                                                        {"label":lab,"value":val} for lab,val in zip(["Group stage","Round of 16","Quarter-final","Semi-final","Match for 3rd place","Final"],
                                                                                                     ["group-stage","round-of-16","quarter-final","semi-final","match-for-3rd-place","final"])
                                                    ],
                                                    value="group-stage",
                                                    multi=False,
                                                    placeholder="Select a step"
                                                )
                                            ],
                                            body=True,
                                            className="controls_team"
                                        )

                                    ],
                                    sm=2,
                                    align="center"
                                ),
                                dbc.Col(children=[html.Div(id="dashboard-step-output")],sm=2),
                                dbc.Col(children=[html.Div(id="dashboard-date-output")],sm=2),
                                dbc.Col(
                                    children = [
                                        dbc.Row(
                                            children=[
                                                dbc.Col(children=[html.Div(id="dashboard-team-one-score-output")],sm=5,align="center"),
                                                dbc.Col(children=[html.H3("VS",style={"text-align":"center"})],sm=2,align="center"),
                                                dbc.Col(children=[html.Div(id="dashboard-team-two-score-output")],sm=5,align="center")
                                            ],
                                            justify="between",
                                            align="center"
                                        )
                                    ],
                                    sm=6
                                ),
                            ]
                        )
                    ]
                ),
                html.Div(
                    children=[
                        dbc.Card(
                            children=[
                                dbc.Row(
                                    children=[
                                        dbc.Col(
                                            children=[
                                                dbc.Card(
                                                    children=[
                                                        html.Div(id="dashboard-team-one-name-output",className="div_center_className"),
                                                        html.P(),
                                                        html.Div(id="dashboard-team-one-flag-output",className="div_center_className"),
                                                        html.P(),
                                                        html.Div(
                                                            children=[
                                                            dmc.ChipGroup(
                                                                [dmc.Chip(lab,value=val,size="sm", color="red",styles=styles)
                                                                for lab,val in zip(["Nickname","Head coach","Appearances","Best result","Trophies","Sub confederation"],
                                                                                ["nickname","manager", "appearance", "best-result","trophies","sub-confederation"])],
                                                                id="dashboard-team-one-others-value",
                                                                value="nickname",
                                                                multiple=False,
                                                                className="div_center_className"
                                                            )
                                                        ],style={"text-align":"center"}),
                                                        html.P(),
                                                        html.Div(id="dashboard-team-one-others-output",className="div_center_className")   
                                                    ],
                                                    body=True,
                                                    className="controls_team",
                                                    style={"height": "480px"}
                                                )
                                            ],
                                            sm=4,
                                            align="center"
                                        ),
                                        dbc.Col(
                                            children=[
                                                dbc.Card(
                                                    children=[
                                                        dcc.Loading(dcc.Graph(id="dashboard-graph-output",config=dict(displayModeBar=False),responsive=False))
                                                    ],
                                                    body=True,
                                                    className="controls_team"
                                                )
                                            ],
                                            sm=4,
                                            align="center"
                                        ),
                                        dbc.Col(
                                            children=[
                                                dbc.Card(
                                                    children=[
                                                        html.Div(id="dashboard-team-two-name-output",className="div_center_className"),
                                                        html.P(),
                                                        html.Div(id="dashboard-team-two-flag-output",className="div_center_className"),
                                                        html.P(),
                                                        html.Div(
                                                            children=[
                                                                dmc.ChipGroup(
                                                                    [dmc.Chip(lab,value=val,size="sm", color="red",styles=styles)
                                                                    for lab,val in zip(["Nickname","Head coach","Appearances","Best result","Trophies","Sub confederation"],
                                                                                    ["nickname","manager","appearance","best-result","trophies","sub-confederation"])],
                                                                    id="dashboard-team-two-others-value",
                                                                    value="nickname",
                                                                    multiple=False,
                                                                    className="div_center_className"
                                                                )
                                                            ]
                                                        )  ,
                                                        html.P(),
                                                        html.Div(id="dashboard-team-two-others-output",className="div_center_className")        
                                                    ],
                                                    body=True,
                                                    className="controls_team",
                                                    style={"height": "480px"}
                                                )
                                            ],
                                            sm=4,
                                            align="center"
                                        )
                                    ]
                                ),
                            ],
                            body=True,
                            className="controls_team"
                        )
                    ]
                ),
                html.P(),
                html.Div(
                    children=[
                        dbc.Card(
                            children=[
                                dbc.Row(
                                    children=[
                                        dbc.Col(
                                            children=[
                                                dbc.Row(
                                                    children=[
                                                        dbc.Col(
                                                            children=[
                                                                dbc.Card(
                                                                    dbc.CardBody(
                                                                        [
                                                                            html.Label("Shots", className="card-title1"),
                                                                            html.Div(id="dashboard-team-one-shots-output",className="card_info1"),
                                                                        ]
                                                                    )
                                                                ,className='attributes_card')
                                                            ],
                                                            sm=3
                                                        ),
                                                        dbc.Col(
                                                            children=[
                                                                dbc.Card(
                                                                dbc.CardBody(
                                                                    [
                                                                        html.Label("Yellow cards", className="card-title1"),
                                                                        html.Div(id="dashboard-team-one-yellow-cards-output",className="card_info1"),
                                                                    ]
                                                                )
                                                                ,className='attributes_card')
                                                            ],
                                                            sm=3
                                                        ),
                                                        dbc.Col(
                                                            children=[
                                                                dbc.Card(
                                                                dbc.CardBody(
                                                                    [
                                                                        html.Label("Red cards", className="card-title1"),
                                                                        html.Div(id="dashboard-team-one-red-cards-output",className="card_info1"),
                                                                    ]
                                                                )
                                                                ,className='attributes_card')
                                                            ],
                                                            sm=3
                                                        ),
                                                        dbc.Col(
                                                            children=[
                                                                dbc.Card(
                                                                dbc.CardBody(
                                                                    [
                                                                        html.Label("Results", className="card-title1"),
                                                                        html.Div(id="dashboard-team-one-results-output",className="card_info1"),
                                                                    ]
                                                                )
                                                                ,className='attributes_card')
                                                            ],
                                                            sm=3
                                                        )
                                                    ]
                                                )
                                            ],
                                            sm=6
                                        ),
                                        dbc.Col(
                                            children=[
                                                dbc.Row(
                                                    children=[
                                                        dbc.Col(
                                                            children=[
                                                                dbc.Card(
                                                                dbc.CardBody(
                                                                    [
                                                                        html.Label("Results", className="card-title2"),
                                                                        html.Div(id="dashboard-team-two-results-output",className="card_info2"),
                                                                    ]
                                                                )
                                                                ,className='attributes_card')
                                                            ],
                                                            sm=3
                                                        ),
                                                        dbc.Col(
                                                            children=[
                                                                dbc.Card(
                                                                dbc.CardBody(
                                                                    [
                                                                        html.Label("Red cards", className="card-title2"),
                                                                        html.Div(id="dashboard-team-two-red-cards-output",className="card_info2"),
                                                                    ]
                                                                )
                                                                ,className='attributes_card')
                                                            ],
                                                            sm=3
                                                        ),
                                                        dbc.Col(
                                                            children=[
                                                                dbc.Card(
                                                                dbc.CardBody(
                                                                    [
                                                                        html.Label("Yellow cards", className="card-title2"),
                                                                        html.Div(id="dashboard-team-two-yellow-cards-output",className="card_info2"),
                                                                    ]
                                                                )
                                                                ,className='attributes_card')
                                                            ],
                                                            sm=3
                                                        ),
                                                        dbc.Col(
                                                            children=[
                                                                dbc.Card(
                                                                    dbc.CardBody(
                                                                        [
                                                                            html.Label("Shots", className="card-title2"),
                                                                            html.Div(id="dashboard-team-two-shots-output",className="card_info2"),
                                                                        ]
                                                                    )
                                                                ,className='attributes_card')
                                                            ],
                                                            sm=3
                                                        )
                                                    ]
                                                )

                                            ],
                                            sm=6
                                        )
                                    ]
                                ),
                                dbc.Row(
                                    children=[
                                        dbc.Col(
                                            children=[
                                                dbc.Card(
                                                    dbc.CardBody(
                                                        [
                                                            html.Label("Possession (%)", className="card-title1"),
                                                            dcc.Loading(dcc.Graph(id="dashboard-team-one-possession-output",config=dict(displayModeBar=False)))
                                                        ]
                                                    )
                                                ,className='attributes_card')
                                            ],
                                            sm=3
                                        ),
                                        dbc.Col(
                                            children=[
                                                dbc.Card(
                                                    dbc.CardBody(
                                                        [
                                                            html.Label("Duel success rate (%)", className="card-title1"),
                                                            dcc.Loading(dcc.Graph(id="dashboard-team-one-duel-success-rate-output",config=dict(displayModeBar=False)))
                                                        ]
                                                    )
                                                ,className='attributes_card')
                                            ],
                                            sm=3
                                        ),
                                        dbc.Col(
                                            children=[
                                                dbc.Card(
                                                    dbc.CardBody(
                                                        [
                                                            html.Label("Duel success rate (%)", className="card-title1"),
                                                            dcc.Loading(dcc.Graph(id="dashboard-team-two-duel-success-rate-output",config=dict(displayModeBar=False)))
                                                        ]
                                                    )
                                                ,className='attributes_card')
                                            ],
                                            sm=3
                                        ),
                                        dbc.Col(
                                            children=[
                                                dbc.Card(
                                                    dbc.CardBody(
                                                        [
                                                            html.Label("Possession (%)", className="card-title1"),
                                                            dcc.Loading(dcc.Graph(id="dashboard-team-two-possession-output",config=dict(displayModeBar=False)))
                                                        ]
                                                    )
                                                ,className='attributes_card')
                                            ],
                                            sm=3
                                        )
                                    ]
                                )
                            ],
                            body=True,
                            className="controls_team"
                        )
                    ]
                ),
                html.Div(
                    children=[
                        dbc.Row(
                            children=[
                                dbc.Col(
                                    children=[
                                        dbc.Card(
                                            children=[
                                                html.Label("Select a TeamStats"),
                                                dcc.Dropdown(
                                                    id="dashboard-team-stats-value",
                                                    options=[
                                                        {"label":lab,"value":val} for lab,val in zip(["General","Distribution","Attack","Defence","Discipline"],
                                                                                                     ["general","distribution","attack","defence","discipline"])
                                                    ],
                                                    value="general",
                                                    multi=False,
                                                    placeholder="Select a TeamStats"
                                                )
                                            ],
                                            body=True,
                                            className="controls_team"
                                        )

                                    ],
                                    sm=2,
                                    align="center"
                                ),  
                            ]
                        )
                    ]
                ),
                html.Div(
                    children=[
                        dbc.Card(
                            children=[
                                dbc.Row(
                                    children=[
                                        dbc.Col(
                                            children=[
                                                dbc.Card(
                                                    children=[
                                                        html.Label("Cumulative Bar plot",style={'font-size': 25, "text-align":"center","font-weight":"bold","color":"red"}),
                                                        dcc.Loading(dcc.Graph(id="dashboard-team-stats-bar-output",config=dict(displayModeBar=False),responsive=False))
                                                    ],
                                                    body=True,
                                                    className="controls_team"
                                                )
                                            ],
                                            sm=6,
                                            align="center"
                                        ),
                                        dbc.Col(
                                            children=[
                                                dbc.Card(
                                                    children=[
                                                        html.Label("Sankey plot",style={'font-size': 25, "text-align":"center","font-weight":"bold","color":"red"}),
                                                        dcc.Loading(dcc.Graph(id="dashboard-team-stats-sankey-output",config=dict(displayModeBar=False),responsive=False))
                                                    ],
                                                    body=True,
                                                    className="controls_team"
                                                )
                                            ],
                                            sm=6
                                        )
                                    ]
                                )
                            ],
                            body=True,
                            className="controls_team"
                        )
                    ]
                )
            ],
            style={"background-color":"black"}
        )


