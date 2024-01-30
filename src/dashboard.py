
from dash import dcc, html, callback
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
import dash_admin_components as dac
from function import *
from data_preparation import *


but_marque = data1["goal_score"].sum(skipna=True)
total_match = data2.dropna().shape[0]
ratio_but_match = but_marque/total_match

best_scorer = (data4.pivot_table(index=["name"],values=["total_but"],aggfunc="sum")
                    .sort_values(by="total_but",ascending=False).index[0])
best_attack = (data1.pivot_table(index=["team_name"],values=["goal_score"],aggfunc="sum")
                    .sort_values(by="goal_score",ascending=False).index[0])
best_defense = (data1.pivot_table(index=["team_name"],values=["goal_encaisse"],aggfunc="sum")
                    .sort_values(by="goal_encaisse",ascending=True).index[0])

styles = {
    "label": {
        "&[data-checked]": {
            "&, &:hover": {
                "backgroundColor": dmc.theme.DEFAULT_COLORS["indigo"][5],
                "color": "white",
            },
        },
    }
}


# Body
body = html.Div(
            children=[
                dbc.Row(html.H1("Dashboard")),
                dbc.Row(
                    children=[
                        html.Div(
                            children=[
                                ValueBox(box_title="Goals score",box_value=int(but_marque),box_icon="database",box_color="primary"),
                                ValueBox(box_title="Total of games",box_value=int(total_match),box_icon="bookmark",box_color="success"),
                                ValueBox(box_title="Best scorer",box_value=best_scorer,box_icon="list",box_color="primary"),
                                ValueBox(box_title="Best attack",box_value=best_attack,box_icon="suitcase",box_color="success")
                            ],
                            className='row'
                        )
                    ],
                    id="id_header"
                ),
                html.P(),
                dbc.Row(
                    children=[
                        html.Div(
                            children=[
                                dcc.Tabs(
                                    id="dashboard-tabs-value",
                                    value="dashboard-groupstage-tab",
                                    children=[
                                        dcc.Tab(label="Group stage", value="dashboard-groupstage-tab"),
                                        dcc.Tab(label="Round of 16", value="dashboard-roundof16-tab"),
                                        dcc.Tab(label="Quarter-finale", value="dashboard-quarterfinale-tab"),
                                        dcc.Tab(label="Semi-finale", value="dashboard-semifinale-tab"),
                                        dcc.Tab(label="Match for 3rd place", value="dashboard-smallfinale-tab"),
                                        dcc.Tab(label="Final", value="dashboard-final-tab"),
                                        dcc.Tab(label="Overall", value="dashboard-overall-tab")
                                    ]
                                ),
                                html.Div(id="dashboard-tabs-content"),
                            ],
                            id="main-panel"
                        )
                    ],
                align='bottom',
                id="body"
                ),
            ]
        )

########################################################## Tab 2 - Round of 16 ##########################################################
#       Round of 16
#########################################################################################################################################

tab_round16 = html.Div(
    children=[
        dbc.Card(
            children=[
                dbc.CardBody(
                    children=[
                        dbc.Row(html.Div(id="dashbaord-roundof16-stadium")),
                        html.Hr(),
                    ]
                )
            ]
        )
    ]
)


tab_overall = html.Div([
    dbc.Card([
        dbc.CardBody(
            children=[
                dbc.Row([html.H1("Overall Statistics")]),
                html.Hr(),
                dbc.Row([html.H2("Before AFCON")]),
                html.Br(),
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
                                                    [dmc.Chip(lab, value=val,styles=styles) 
                                                    for lab, val in zip(["Pie chart","Bar chart"],["pie-chart","bar-chart"])],
                                                    value="pie-chart",
                                                    multiple=False,
                                                    id="country-sub-confederation-graph-value"
                                                )
                                            ]
                                        ),
                                        dcc.Loading(dcc.Graph(id="country-sub-confederation-graph-output",config=dict(displayModeBar=False)))
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
                                                    [dmc.Chip(lab, value=val,styles=styles) 
                                                    for lab, val in zip(["Pie chart","Bar chart"],["pie-chart","bar-chart"])],
                                                    value="pie-chart",
                                                    multiple=False,
                                                    id="trophy-sub-confederation-graph-value"
                                                )
                                            ]
                                        ),
                                        dcc.Loading(dcc.Graph(id="trophy-sub-confederation-graph-output",config=dict(displayModeBar=False)))
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
                                                    [dmc.Chip(x, value=x,styles=styles) for x in ["CECAFA","COSAFA","UNAF","UNIFFAC","WAFU"]],
                                                    value="UNIFFAC",
                                                    multiple=False,
                                                    id="names-graph-value"
                                                )
                                            ]
                                        ),
                                        dcc.Loading(dcc.Graph(id="names-graph-output",config=dict(displayModeBar=False)))
                                    ],
                                    className="attributes_card"
                                )
                            ],
                            sm=5
                        )
                    ]
                ),
                html.P(),
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
                                                    [dmc.Chip(lab, value=val,styles=styles) 
                                                    for lab, val in zip(["Trophies","Appearances"],["titre","appearances"])],
                                                    value="titre",
                                                    multiple=False,
                                                    id="country-graph-value"
                                                )
                                            ]
                                        ),
                                        dcc.Loading(dcc.Graph(id="country-graph-output",config=dict(displayModeBar=False)))
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
                html.P(),
                dbc.Row(html.H2("During AFCON")),
                html.Hr(),
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
                                                    [dmc.Chip(lab, value=val,styles=styles) 
                                                    for lab, val in zip(["Players","Country","Date","Sub confederation","Step"],
                                                                        ["name","team_name","date","sub_confederation","step"])],
                                                    value="name",
                                                    multiple=False,
                                                    id="goal_value"
                                                )
                                            ]
                                        ),
                                        dcc.Loading(dcc.Graph(id="goal_graph",config=dict(displayModeBar=False)))
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
                                                    [dmc.Chip(lab, value=val,styles=styles) 
                                                    for lab, val in zip(["Goals scored","Goals conceced","Goals difference"],
                                                                        ["goal-scored","goal-conceded","goal-difference"])],
                                                    value="goal-scored",
                                                    multiple=False,
                                                    id="country-goal-value"
                                                )
                                            ]
                                        ),
                                        dcc.Loading(dcc.Graph(id="country-goal-graph",config=dict(displayModeBar=False)))
                                    ],
                                    className="attributes_card"
                                )
                            ],
                            sm=6
                        )
            ]),
            html.P(),
            dbc.Row(
                children=[
                    dbc.Col(
                        children=[
                            dbc.Card(
                                children=[

                                ]
                            )
                        ],
                        sm=4
                    )
                ]
            )
        ])
    ])
])

dashboard = html.Div(
    id="main-app", className="main-app",
    children=[
        body
    ]
)