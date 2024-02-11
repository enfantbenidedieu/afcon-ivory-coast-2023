# -*- coding: utf-8 -*-

from dash import html, dcc
import dash_bootstrap_components as dbc
import dash_ag_grid as dag
from function import InfosBox 
from data_preparation import *


data["Date"] = data["Date"].astype("str")
Stadium["Date"] = Stadium["Date"].astype("str")
goals["Date"] = goals["Date"].astype("str")
team_infos["Team ID"] = ["+"+str(x) for x in team_infos["Team ID"]]


defaultColDef = {
    "resizable": True,
    "wrapHeaderText": True,
    "autoHeaderHeight": True,
    "filter": True,
    "sortable": True,
}

columnDefs = [
    {
        "headerName"  : "Date",
        "stickyLabel" : True,
        "children": [
            {"field" : "Day"},
            {"field" : "Date"}
        ]
    },
    {
        "headerName" : "Group step",
        "children" : [
            {"field" : "Step"},
            {"field" : "Group"}
        ]
    },
    {
        "headerName" : "Country",
        "children" : [
             {"field" : "Team name",
              "cellRenderer": "TeamLogoRenderer"}
        ]
    },
    {
        "headerName" : "General",
        "children"   : [
            {"field" : "Possession"},
            {"field" : "Duels success rate"},
            {"field" : "Aerial duels rate"},
            {"field" : "Interceptions"},
            {"field" : "Offsides"},
            {"field" : "Corners won"}
        ]
    },
    {
        "headerName" : "Distribution",
        "children" : [
            {"field" : "Passes"},
            {"field" : "Long passes"},
            {"field" : "Passing accuracy"},
            {"field" : "PA in opponents half(%)"},
            {"field" : "Crosses"},
            {"field" : "Crossing accuracy"}
        ]
    },
    {
        "headerName" : "Attack",
        "children" : [
            {"field" : "Goals"},
            {"field" : "Shots"},
            {"field" : "Shots on target"},
            {"field" : "Blocked shots"},
            {"field" : "Shots outside the box"},
            {"field" : "Shots inside the box"},
            {"field" : "Shooting accuracy"}
        ]
    },
    {
        "headerName" : "Defence",
        "children"   : [
            {"field" : "Tackles"},
            {"field" : "Tackles success rate"},
            {"field" : "Clearances"}
        ]
    },
    {
        "headerName" : "Descipline",
        "children"   : [
            {"field" : "Fouls conceded"},
            {"field" : "Yellow cards"},
            {"field" : "Red cards"}
        ]
    },
    {
        "headerName" : "Issue",
        "children"   : [
            {"field" : "Result"}
        ]
    }
]

def DataGrid(data,id_name):
    grid = dag.AgGrid(
        id="database-"+id_name+"-output",
        rowData=data.to_dict("records"),
        columnDefs=[{"field": i} for i in data.columns],
        className="ag-theme-alpine-dark",
        style={'height': '500px'},
        defaultColDef=defaultColDef,
        dashGridOptions={
            "pagination": True,
            "paginationPageSize": 20,
            "enableFilter": True,
        }
    )
    return grid

grid_data = dag.AgGrid(
    id="get-started-example-basic",
    rowData=data.to_dict("records"),
    columnDefs=columnDefs,
    className="ag-theme-alpine-dark",
    style={'height': '500px'},
    defaultColDef=defaultColDef,
    dashGridOptions={
        "pagination": True,
        "paginationPageSize": 20,
        "enableFilter": True,
    }
)

#### Team infos
grid_infos = DataGrid(data=team_infos,id_name="team-infos")

#### Stadium
grid_stadium = DataGrid(data=Stadium,id_name="stadium")

#### Goals Overall
grid_goals = DataGrid(data=goals,id_name="goals-overall")

database = html.Div(
    children=[
        html.Div(
            children=[
                dbc.Card(
                    children=[
                        html.Div(
                            children=[
                                InfosBox(box_title="Number of Rows",box_value=data.shape[0],box_icon="database",box_color="success"),
                                InfosBox(box_title="Number of Columns",box_value=data.shape[1],box_icon="bars",box_color="primary"),
                                InfosBox(box_title="Target variable",box_value="Result",box_icon="thumbs-up",box_color="info")
                            ],
                            className="row"
                        ),
                    ],
                    className="controls_team"
                )
            ]
        ),
        html.Div(
            children=[
                dbc.Card(
                    children=[
                        html.H1("Country informations")
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
                        grid_infos,
                        html.P(),
                        html.Div([
                            dbc.Button("Download Excel", outline=True, color="dark", className="me-1",id="team-infos-btn-xlsx"),
                            dcc.Download(id="download-team-infos-xlsx"),
                        ])
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
                                html.Div(
                                    children=[
                                        dbc.Card(
                                            children=[
                                                html.H1("Stadium")
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
                                                grid_stadium,
                                                html.P(),
                                                html.Div([
                                                    dbc.Button("Download Excel", outline=True, color="dark", className="me-1",id="stadium-btn-xlsx"),
                                                    dcc.Download(id="download-stadium-xlsx"),
                                                ])
                                            ],
                                            className="controls_team"
                                        )
                                    ]
                                ),
                            ],
                            sm=6
                        ),
                        dbc.Col(
                            children=[
                                html.Div(
                                    children=[
                                        dbc.Card(
                                            children=[
                                                html.H1("Goals")
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
                                                grid_goals,
                                                html.P(),
                                                html.Div([
                                                    dbc.Button("Download Excel", outline=True, color="dark", className="me-1",id="goals-btn-xlsx"),
                                                    dcc.Download(id="download-goals-xlsx"),
                                                ])
                                            ],
                                            className="controls_team"
                                        )
                                    ]
                                ),
                                
                            ],
                            sm=6
                        )
                    ]
                )
            ]
        ),
        html.Div(
            children=[
                dbc.Card(
                    children=[
                        html.H1("AFCON 2023 Results")
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
                        grid_data,
                        html.P(),
                        html.Div([
                            dbc.Button("Download Excel", outline=True, color="dark", className="me-1",id="data-btn-xlsx"),
                            dcc.Download(id="download-data-xlsx"),
                        ])
                    ],
                    className="controls_team"
                )
            ]
        )
    ]
)