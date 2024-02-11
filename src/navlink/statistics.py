# -*- coding: utf-8 -*-

from dash import dcc, html
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
from function import *
from data_preparation import *

but_marque = data["Goals"].sum(skipna=True)
total_match = Stadium.shape[0]
ratio_but_match = but_marque/total_match

best_scorer = (goals.pivot_table(index=["Name"],values=["But"],aggfunc="sum")
                    .sort_values(by="But",ascending=False).index[0])
best_attack = (goals.pivot_table(index=["Team name"],values=["But"],aggfunc="sum")
                    .sort_values(by="But",ascending=False).index[0])

statistics = html.Div(
    children=[
        html.Div(
            children=[
                dbc.Card(
                    children=[
                        html.H1("Before AFCON")
                    ],
                    className="controls_team",
                    style={"text-align":"center","font-weight":"bold","color":"red"}
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
                                        html.H5("Number of country by Sub confederation",className="text-center mt-3 mb-1"),
                                        html.P(),
                                        html.Div(
                                            className="selection d-flex justify-content-center mb-3",
                                            children=[
                                                dmc.ChipGroup(
                                                    [dmc.Chip(lab, value=val,size="sm", color="red",styles=styles) 
                                                    for lab, val in zip(["Pie chart","Bar chart"],["pie-chart","bar-chart"])],
                                                    value="pie-chart",
                                                    multiple=False,
                                                    id="statistics-before-afcon-country-sub-confederation-graph-value"
                                                )
                                            ]
                                        ),
                                        dcc.Loading(dcc.Graph(id="statistics-before-afcon-country-sub-confederation-graph-output",config=dict(displayModeBar=False)))
                                    ],
                                    className="attributes_card"
                                )
                            ],
                            sm = 4
                        ),
                        dbc.Col(
                            children=[
                                dbc.Card(
                                    children=[
                                        html.H5("Trophies by Sub confederation",className="text-center mt-3 mb-1"),
                                        html.P(),
                                        html.Div(
                                            className="selection d-flex justify-content-center mb-3",
                                            children=[
                                                dmc.ChipGroup(
                                                    [dmc.Chip(lab, value=val,size="sm", color="red",styles=styles) 
                                                    for lab, val in zip(["Pie chart","Bar chart"],["pie-chart","bar-chart"])],
                                                    value="pie-chart",
                                                    multiple=False,
                                                    id="statistics-before-afcon-trophy-sub-confederation-graph-value"
                                                )
                                            ]
                                        ),
                                        dcc.Loading(dcc.Graph(id="statistics-before-afcon-trophy-sub-confederation-graph-output",config=dict(displayModeBar=False)))
                                    ],
                                    className="attributes_card"
                                )
                            ],
                            sm=3
                        ),
                        dbc.Col(
                            children=[
                                dbc.Card(
                                    children=[
                                        html.H5("Country by Sub confederation with number of trophies",className="text-center mt-3 mb-1"),
                                        html.P(),
                                        html.Div(
                                            className="selection d-flex justify-content-center mb-3",
                                            children=[
                                                dmc.ChipGroup(
                                                    [dmc.Chip(x, value=x,size="sm", color="red",styles=styles) for x in ["CECAFA","COSAFA","UNAF","UNIFFAC","WAFU"]],
                                                    value="UNIFFAC",
                                                    multiple=False,
                                                    id="statistics-before-afcon-names-graph-value"
                                                )
                                            ]
                                        ),
                                        dcc.Loading(dcc.Graph(id="statistics-before-afcon-names-graph-output",config=dict(displayModeBar=False)))
                                    ],
                                    className="attributes_card"
                                )
                            ],
                            sm=5
                        )
                    ]
                ),
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
                                        html.H5("Order country by",className="text-center mt-3 mb-1"),
                                        html.P(),
                                        html.Div(
                                            className="selection d-flex justify-content-center mb-3",
                                            children=[
                                                dmc.ChipGroup(
                                                    [dmc.Chip(lab, value=val,size="sm", color="red",styles=styles) 
                                                    for lab, val in zip(["Trophies","Appearances"],["titre","appearances"])],
                                                    value="titre",
                                                    multiple=False,
                                                    id="statistics-before-afcon-country-graph-value"
                                                )
                                            ]
                                        ),
                                        dcc.Loading(dcc.Graph(id="statistics-before-afcon-country-graph-output",config=dict(displayModeBar=False)))
                                    ],
                                    className="attributes_card"
                                )
                            ],
                            sm=6
                        ),
                        dbc.Col(
                            children=[
                                dbc.Card(
                                    children=[
                                        html.H5("Order country by",className="text-center mt-3 mb-1"),
                                        html.P(),
                                    ],
                                    className="attributes_card"
                                )
                            ],
                            sm=6
                        )
                    ]
                ),
            ]
        ),
        html.Div(
            children=[
                dbc.Card(
                    children=[
                        html.H1("During AFCON")
                    ],
                    className="controls_team",
                    style={"text-align":"center","font-weight":"bold","color":"red"}
                )
            ]
        ),
        html.Div(
            children=[
                dbc.Card(
                    children=[
                        html.Div(
                            children=[
                                ValueBox(box_title="Goals score",box_value=int(but_marque),box_icon="database",box_color="primary"),
                                ValueBox(box_title="Total of games",box_value=int(total_match),box_icon="bars",box_color="success"),
                                ValueBox(box_title="Best scorer",box_value=best_scorer,box_icon="thumbs-up",box_color="primary"),
                                ValueBox(box_title="Best attack",box_value=best_attack,box_icon="thumbs-up",box_color="success")
                            ],
                            className='row',
                        ),
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
                                        html.H5("Order goals by",className="text-center mt-3 mb-1"),
                                        html.P(),
                                        html.Div(
                                            className="selection d-flex justify-content-center mb-3",
                                            children=[
                                                dmc.ChipGroup(
                                                    [dmc.Chip(lab, value=val,size="sm", color="red",styles=styles) 
                                                    for lab, val in zip(["Players","Country","Date","Sub confederation","Step"],
                                                                        ["players","country","date","sub-confederation","step"])],
                                                    value="players",
                                                    multiple=False,
                                                    id="statistics-during-afcon-goal-graph-value"
                                                )
                                            ]
                                        ),
                                        dcc.Loading(dcc.Graph(id="statistics-during-afcon-goal-graph-output",config=dict(displayModeBar=False)))
                                    ],
                                    className="attributes_card"
                                )
                            ],
                            sm=6
                        ),
                        dbc.Col(
                            children=[
                                dbc.Card(
                                    children=[
                                        html.H5("Order country by",className="text-center mt-3 mb-1"),
                                        html.P(),
                                        html.Div(
                                            className="selection d-flex justify-content-center mb-3",
                                            children=[
                                                dmc.ChipGroup(
                                                    [dmc.Chip(lab, value=val,size="sm", color="red",styles=styles) 
                                                    for lab, val in zip(["Goals scored","Goals conceced","Goals difference"],
                                                                        ["goal-scored","goal-conceded","goal-difference"])],
                                                    value="goal-scored",
                                                    multiple=False,
                                                    id="statistics-during-afcon-country-goal-graph-value"
                                                )
                                            ]
                                        ),
                                        dcc.Loading(dcc.Graph(id="statistics-during-afcon-country-goal-graph-output",config=dict(displayModeBar=False)))
                                    ],
                                    className="attributes_card"
                                )
                            ],
                            sm=6
                        )
                ]),
            ]
        )
    ]
)