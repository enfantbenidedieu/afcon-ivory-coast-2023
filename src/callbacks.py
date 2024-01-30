


from dash import dcc, html, callback, Input, Output, State
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
import plotly.express as px
import plotly.graph_objs as go
from data_preparation import *

from dashboard import dashboard
from pca import principal_component_analysis
from afcon import presentation


from method.ologit import tab_logit
from method.database import tab_database
from method.compare import tab_compare

from scientisttools.extractfactor import (
    get_eigenvalue,
    get_pca_ind,
    get_pca_var,
    dimdesc
)

# Import 
from dashboard import tab_overall
# Import all div
from pca import (
    pca_modal, 
    tab_graphes, 
    tab_valeurs,
    eigen_div,
    var_div, 
    ind_div,
    ind_sup_div,
    var_sup_div,
    var_qual_div,
    tab_description,
    tab_summary,
    statistics_div,
    hist_div,
    corr_matrix_div,
    tab_data)
from function import (
    plotly_pca_ind, 
    plotly_pca_var,
    plotly_screeplot,
    plotly_contrib,
    plotly_cosines,
    match_datalength,
    DataTable)
    
from utils import *

colors_dict = {
    "CECAFA"  : "firebrick",
    "COSAFA"  : "navy",
    "UNAF"    : "orange",
    "UNIFFAC" : "green",
    "WAFU"    : "royalblue"
}

colors = ["firebrick", "green", "","darkblue","orange"]


team_url_flag = {
    "Côte d'Ivoire"      : "/assets/FIF_Côte_d'Ivoire_logo.png",
    "Guinée - Bissau"    : "/assets/Guinea-Bissau_FF_(logo).png",
    "Nigeria"            : "/assets/Nigeria_national_football_team.png",
    "Guinée Equatoriale" : "/assets/Equatorial_Guinea_FA.png",
    "Egypte"             : "/assets/Egypt_national_football_team.png",
    "Mozambique"         : "/assets/Mozambique_national_football_team.png",
    "Ghana"              : "/assets/Ghana_FA.png",
    "Cap - Vert"         : "/assets/Cape_Verde_FA_(2020).png",
    "Sénégal"            : "/assets/Senegalese_Football_Federation_logo.svg.png",
    "Gambie"             : "/assets/Gambia_Football_Federation_(association_football_federation)_logo.png",
    "Cameroun"           : "/assets/Cameroon_2010crest.png",
    "Guinée"             : "/assets/Fgf_guinee_logo_shirt.png",
    "Algérie"            : "/assets/Algerian_NT_(logo).png",
    "Angola"             : "/assets/Logo_Federaçao_Angolana_de_Futebol.png",
    "Burkina Faso"       : "/assets/Burkina_Faso_FA.png",
    "Mauritanie"         : "/assets/Mauritania_national_football_team.png",
    "Tunisie"            : "/assets/Tunisia_national_football_team_logo.png",
    "Namibie"            : "/assets/Namibia_FA.png",
    "Mali"               : "/assets/Mali_FF_(New).png",
    "Afrique du Sud"     : "/assets/South_Africa_Flor.png",
    "Maroc"              : "/assets/Royal_Moroccan_Football_Federation_logo.svg.png",
    "Tanzanie"           : "/assets/Tanzania_FF_(logo).png",
    "RDC"                : "/assets/Congo_DR_FA.png",
    "Zambie"             : "/assets/Zambia_national_footnall_team.png"
}




###################################################################################"
#   
#####################################################################################


@callback(
    Output("page-content", "children"), 
    [Input("url", "pathname")]
)
def render_page_content(pathname):
    if pathname == "/":
        return presentation
    elif pathname == "/database":
        return tab_database
    elif pathname == "/dashboard":
        return dashboard
    elif pathname == '/principal-component-analysis':
        return principal_component_analysis
    elif pathname == "/logistic-regression":
        return tab_logit
    elif pathname == '/linear-discriminant-analysis':
        return html.H1('Analyse discriminante linéaire')
    elif pathname == '/classification-and-regression-tree':
        return html.H1('Arbre de décision')
    elif pathname == "/k-nearest-neighbors":
        return html.H1("K- plus proches voisins")
    elif pathname == '/model-compare':
        return tab_compare
    elif pathname == '/variable-selection':
        return html.H1("Variable sélection")
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )





cards1 = dbc.Row(
    children=[
        dbc.Col(
            children=[
                dbc.Card(
                    dbc.CardBody(
                        [
                            html.Div("Passes", className="card-title1"),
                            html.Div(id="P_passesA",className="card_info1"),
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
                        html.Div("Cartons Jaunes", className="card-title1"),
                        html.Div(id="P_yellowcardA",className="card_info1"),
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
                        html.Div("Cartons rouges", className="card-title1"),
                        html.Div(id="P_redcardA",className="card_info1"),
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
                        html.Div("Issue", className="card-title1"),
                        html.Div(id="P_issueA",className="card_info1"),
                    ]
                )
                ,className='attributes_card')
            ],
            sm=3
        )
    ]
)

cards2 = dbc.Row(
    children=[
        dbc.Col(
            children=[
                dbc.Card(
                dbc.CardBody(
                    [
                        html.Div("Issue", className="card-title2"),
                        html.Div(id="P_issueB",className="card_info2"),
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
                        html.Div("Cartons rouges", className="card-title2"),
                        html.Div(id="P_redcardB",className="card_info2"),
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
                        html.Div("Cartons Jaunes", className="card-title2"),
                        html.Div(id="P_yellowcardB",className="card_info2"),
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
                            html.Div("Passes", className="card-title2"),
                            html.Div(id="P_passesB",className="card_info2"),
                        ]
                    )
                ,className='attributes_card')
            ],
            sm=3
        )
    ]
)

cards3 = html.Div([
    dbc.Row([
        dbc.Col([
            dbc.Card(
                dbc.CardBody(
                    [
                        html.Div("Possession (%)", className="card-title1"),
                        dcc.Loading(dcc.Graph(id="P_possessonA",config=dict(displayModeBar=False),responsive=True)),
                    ]
                ),
                className='attributes_card'
            )
        ],
        sm=6),
        dbc.Col([
            dbc.Card(
                dbc.CardBody(
                    [
                        html.Div("Pass Accuracy (%)", className="card-title1"),
                        dcc.Loading(dcc.Graph(id="P_passaccuracyA",config=dict(displayModeBar=False),responsive=True)),
                    ]
                ),
                className='attributes_card'
            )
        ],
        sm=6)
    ])
])


cards3 = html.Div([
    dbc.Row([
        dbc.Col([
            dbc.Card(
                dbc.CardBody(
                    [
                        html.Div("Possession (%)", className="card-title2"),
                        dcc.Loading(dcc.Graph(id="P_possessionA",config=dict(displayModeBar=False),responsive=True)),
                    ]
                ),
                className='attributes_card'
            )
        ],
        sm=6),
        dbc.Col([
            dbc.Card(
                dbc.CardBody(
                    [
                        html.Div("Pass Accuracy (%)", className="card-title2"),
                        dcc.Loading(dcc.Graph(id="P_passaccuracyA",config=dict(displayModeBar=False),responsive=True)),
                    ]
                ),
                className='attributes_card'
            )
        ],
        sm=6)
    ])
])

cards4 = html.Div([
    dbc.Row([
        dbc.Col([
            dbc.Card(
                dbc.CardBody(
                    [
                        html.Div("Pass Accuracy (%)", className="card-title1"),
                        dcc.Loading(dcc.Graph(id="P_passaccuracyB",config=dict(displayModeBar=False),responsive=True)),
                    ]
                ),
                className='attributes_card'
            )
        ],
        sm=6),
        dbc.Col([
            dbc.Card(
                dbc.CardBody(
                    [
                        html.Div("Possession (%)", className="card-title1"),
                        dcc.Loading(dcc.Graph(id="P_possessionB",config=dict(displayModeBar=False),responsive=True)),
                    ]
                ),
                className='attributes_card'
            )
        ],
        sm=6)
    ])
])

score_card = dbc.Row([
    dbc.Col([html.Div(id="ScoreA")],sm=5),
    dbc.Col([html.H3("VS",style={"text-align":"center"})],sm=2),
    dbc.Col([html.Div(id="ScoreB")],sm=5),

])

tab1_content = html.Div(
    children=[
        dbc.Card(
            children=[
                dbc.CardBody(
                    children=[
                        dbc.Row(html.Div(id="stadium")),
                        html.Hr(),
                        dbc.Row(
                            children=[
                                dbc.Col(
                                    children=[
                                        dbc.Card(
                                            children=[
                                                html.Label("Select a Date"),
                                                dcc.Dropdown(
                                                    id="date",
                                                    options=[
                                                        {"label":x,"value":y} 
                                                        for x,y in zip(group_stage_date1_label,group_stage_date1_value)
                                                    ],
                                                    value=group_stage_date1_value[0],
                                                    multi=False,
                                                    placeholder="select a date"
                                                )
                                            ],
                                            body=True,
                                            className="controls_team",
                                        )
                                    ],
                                    width=3
                                ),
                                dbc.Col(
                                    children=[
                                        html.Div(id="id_team")
                                    ],
                                    width=3
                                ),
                                dbc.Col(
                                    children=[
                                        score_card
                                    ]
                                )
                            ],
                            align="between"
                        ),
                        dbc.Row(
                            children=[
                                dbc.Col(
                                    children=[
                                        dbc.Row(html.Div(id="teamA")),
                                        html.Hr(),
                                        dbc.Row(html.Div(id="teamA_flag",style={"text-align":"center"})),
                                        html.Hr(),
                                        dbc.Row([
                                            html.Div(
                                                className="selection d-flex justify-content-center mb-3",
                                                children=[
                                                dmc.ChipGroup(
                                                    [dmc.Chip(lab,value=val,variant="outline")
                                                    for lab,val in zip(["Nickname","Head coach","Appearances","Best result","Titres","Sub confederation"],
                                                                    ["nickname","manager", "appearances", "best_result","titres","sub_confederation"])],
                                                    id="teamA-infos",
                                                    value="nickname",
                                                    multiple=False
                                                )
                                            ])
                                        ]),
                                        html.P(),
                                        dbc.Row(children=[html.Div(id="teamA-values-output")])                                        
                                    ],
                                    sm=4,
                                    align="left"
                                ),
                                dbc.Col(
                                    children=[
                                        dcc.Loading(dcc.Graph(id="graph_example",config=dict(displayModeBar=False)))
                                    ],
                                    sm=4,
                                    align="center"
                                ),
                                dbc.Col(
                                    children=[
                                        dbc.Row(html.Div(id="teamB")),
                                        html.Hr(),
                                        dbc.Row(html.Div(id="teamB_flag",style={"text-align":"center"})),
                                        html.Hr(),
                                        dbc.Row([
                                            html.Div(
                                                className="selection d-flex justify-content-center mb-3",
                                                children=[
                                                    dmc.ChipGroup(
                                                        [dmc.Chip(lab,value=val,variant="outline")
                                                        for lab,val in zip(["Nickname","Head coach","Appearances","Best result","Titres","Sub confederation"],
                                                                        ["nickname","manager", "appearances", "best_result","titres","sub_confederation"])],
                                                        id="teamB-infos",
                                                        value="nickname",
                                                        multiple=False
                                                    )
                                                ]
                                            )  
                                        ]),
                                        html.P(),
                                        dbc.Row(html.Div(id="teamB-values-output",className="selection d-flex justify-content-center mb-3"))
                                    ],
                                    sm=4,
                                    align="right"
                                )
                            ],
                            justify="between"
                        ),
                        dbc.Row(
                            children=[
                                dbc.Col(
                                    children=[
                                        cards1
                                    ],
                                    sm=6
                                ),
                                dbc.Col([cards2],sm=6)
                            ]
                        ),
                        html.P(),
                        dbc.Row([
                            dbc.Col([cards3],sm=6),
                            dbc.Col([cards4],sm=6)
                        ])
                    ]
                )
            ]
        )
    ]
)

# callback
@callback(
    Output("dashboard-tabs-content", "children"), 
    [Input("dashboard-tabs-value", "value")]
)
def switch_tab(at):
    if at == "dashboard-groupstage-tab":
        return tab1_content
    elif at == "dashboard-roundof16-tab":
        return html.H1("Choose a date")
    elif at == "dashboard-overall-tab":
        return tab_overall
    return html.P("This shouldn't ever be displayed...")

@callback(
    Output("id_team","children"),
    [Input("date","value")]
)
def select_team(dat):
    # Filter on team
    df = group_stage_data1[group_stage_data1.date==dat]
    return dbc.Card(
        children=[
            html.Label("Select a team"),
            dcc.Dropdown(
                id="team",
                options=[
                    {"label" : x , "value" : x} for x in df["team_name"].to_list()
                ],
                value=df["team_name"].to_list()[0],
                multi=False
            )
        ],
        body=True,
        className="controls_team"
    )


@callback(
    [Output("graph_example","figure"),
    Output("teamA","children"),
    Output("teamA_flag","children"),
    Output("teamB","children"),
    Output("teamB_flag","children"),
    Output("ScoreA","children"),
    Output("ScoreB","children"),
    Output("stadium","children")],
    [Input("date","value"),
     Input("team","value")]
)

def graph_example(dat,team1):

    # Filter using date and name in data2
    df = group_stage_data2[group_stage_data2.date==dat]
    if team1 in df.teama.to_list():
        team2 = df[df.teama==team1]["teamb"].values[0]
    else:
        team2 = df[df.teamb==team1]["teama"].values[0]

    # Columns to select
    columns = ["shots","shots_on_target","fouls","corners"]

    df_teamA = group_stage_data1[((group_stage_data1.date == dat) & (group_stage_data1.team_name == team1))][columns].T
    df_teamA.columns = ["score"]
    df_teamB = group_stage_data1[((group_stage_data1.date == dat) & (group_stage_data1.team_name == team2))][columns].T
    df_teamB.columns = ["score"]

    list_scores1 = [df_teamA.index[i].capitalize() +' = ' + str(df_teamA['score'][i]) for i in range(len(df_teamA))]
    text_scores_teamA = team1
    for i in list_scores1:
        text_scores_teamA += '<br>' + i
    
    list_scores2 = [df_teamB.index[i].capitalize() +' = ' + str(df_teamB['score'][i]) for i in range(len(df_teamB))]
    text_scores_teamB = team2
    for i in list_scores2:
        text_scores_teamB += '<br>' + i
    
    fig = go.Figure(data=go.Scatterpolar(
        name = text_scores_teamA,
        r=df_teamA["score"],
        theta=df_teamA.index,
        mode = 'markers',
        fill='toself', 
        marker_color = 'rgb(45,0,198)',   
        opacity =1, 
        hoverinfo = "text",
        text=[df_teamA.index[i] +' = ' + str(df_teamA['score'][i]) for i in range(len(df_teamA))]
    ))
    fig.add_trace(go.Scatterpolar(
        name= text_scores_teamB,
        r=df_teamB["score"],
        theta=df_teamB.index,
        fill='toself',
        marker_color = 'rgb(255,171,0)',
        hoverinfo = "text" ,
        text=[df_teamB.index[i].capitalize() +' = ' + str(df_teamB['score'][i]) for i in range(len(df_teamB))]
        ))
    fig.update_layout(
        polar=dict(
            hole=0.1,
            bgcolor="white",
            radialaxis=dict(
                visible=True,
                type='linear',
                autotypenumbers='strict',
                autorange=False,
                range=[0, 1+max(df_teamA.max().values,df_teamB.max().values)[0]],
                angle=90,
                showline=False,
                showticklabels=False, ticks='',
                gridcolor='black'),
                ),
        width = 500,
        height = 500,
        margin=dict(l=80, r=80, t=20, b=20),
        showlegend=False,
        template="plotly_dark",
        plot_bgcolor = 'rgba(0, 0, 0, 0)',
        paper_bgcolor = 'rgba(0, 0, 0, 0)',
        font_color="black",
        font_size= 15
    )

    # Set 
    score_teamA = group_stage_data1[((group_stage_data1.date == dat) & (group_stage_data1.team_name == team1))]["goal_score"].values[0]
    score_teamB = group_stage_data1[((group_stage_data1.date == dat) & (group_stage_data1.team_name == team2))]["goal_score"].values[0]
    color_cardA = None
    color_cardB = None
    if score_teamA == score_teamB:
        color_cardA = "light"
        color_cardB = "light"
    elif score_teamA > score_teamB:
        color_cardA = "success"
        color_cardB = "danger"
    else:
        color_cardA = "danger"
        color_cardB = "success"

    # Set team A color card
    card_teamA = dbc.Card(
        dbc.CardBody([html.H4(f"{team1} : {int(score_teamA)}")]),
        className='controls_team',
        color=color_cardA
    )

    # Set team B color card
    card_teamB = dbc.Card(
        dbc.CardBody([html.H4(f"{int(score_teamB)} : {team2}")]),
        className='controls_team',
        color=color_cardB
    )

    # Stadium name
    stadium = df[((df.teama==team1) & (df.teamb==team2)) | ((df.teama==team2) & (df.teamb==team1))]["stadium"].values[0]

    #teamA_flag = html.Img(src='/assets/player_1.png',className="playerImg")
    teamA_flag = html.Img(src=team_url_flag[team1],className="playerImg")
    teamB_flag = html.Img(src=team_url_flag[team2],className="playerImg")

    return (fig,
            html.H3(f"{team1}"),teamA_flag,
            html.H3(f"{team2}"),teamB_flag,
            card_teamA, card_teamB,
            html.H1(f"{stadium}"))


@callback(
    [Output("teamA-values-output","children"),
     Output("teamB-values-output","children")],
    [Input("date","value"),
     Input("team","value"),
     Input("teamA-infos","value"),
     Input("teamB-infos","value")]
)

def team_infos(dat,team1,teamA_value,teamB_value):
    # Filter using date and name in data2
    df = group_stage_data2[group_stage_data2.date==dat]
    if team1 in df.teama.to_list():
        team2 = df[df.teama==team1]["teamb"].values[0]
    else:
        team2 = df[df.teamb==team1]["teama"].values[0]

    # Informations for team A
    teamA_infos = data3[data3.team_name == team1][teamA_value].values[0]
    teamB_infos = data3[data3.team_name == team2][teamB_value].values[0]

    return (html.H5(f"{teamA_infos}"),html.H5(f"{teamB_infos}"))


@callback(
    [Output("P_passesA","children"),
     Output("P_yellowcardA","children"),
     Output("P_redcardA","children"),
     Output("P_issueA","children"),
     Output("P_issueB","children"),
     Output("P_redcardB","children"),
     Output("P_yellowcardB","children"),
     Output("P_passesB","children")],
    [Input("date","value"),
     Input("team","value")]
)
def team_card_value(dat,team1):

    # Filter using date and name in data2
    df = group_stage_data2[group_stage_data2.date==dat]
    if team1 in df.teama.to_list():
        team2 = df[df.teama==team1]["teamb"].values[0]
    else:
        team2 = df[df.teamb==team1]["teama"].values[0]
    
    #########################"
    ## Team A
    passes_A = group_stage_data1[((group_stage_data1.date == dat) & (group_stage_data1.team_name == team1))]["passes"].values[0]
    yellowcard_A = group_stage_data1[((group_stage_data1.date == dat) & (group_stage_data1.team_name == team1))]["yellow_cards"].values[0]
    redcard_A = group_stage_data1[((group_stage_data1.date == dat) & (group_stage_data1.team_name == team1))]["red_cards"].values[0]
    issue_A = group_stage_data1[((group_stage_data1.date == dat) & (group_stage_data1.team_name == team1))]["issue"].values[0]

    passes_B = group_stage_data1[((group_stage_data1.date == dat) & (group_stage_data1.team_name == team2))]["passes"].values[0]
    yellowcard_B = group_stage_data1[((group_stage_data1.date == dat) & (group_stage_data1.team_name == team2))]["yellow_cards"].values[0]
    redcard_B = group_stage_data1[((group_stage_data1.date == dat) & (group_stage_data1.team_name == team2))]["red_cards"].values[0]
    issue_B = group_stage_data1[((group_stage_data1.date == dat) & (group_stage_data1.team_name == team2))]["issue"].values[0]

    return (passes_A,yellowcard_A,redcard_A,issue_A,
            issue_B,redcard_B,yellowcard_B,passes_B)



@callback(
    [Output("P_possessionA","figure"),
     Output("P_passaccuracyA","figure"),
     Output("P_passaccuracyB","figure"),
     Output("P_possessionB","figure")],
     [Input("date","value"),
     Input("team","value")]
)
def gauge_plot(dat,team1):
    # Filter using date and name in data2
    df = group_stage_data2[group_stage_data2.date==dat]
    if team1 in df.teama.to_list():
        team2 = df[df.teama==team1]["teamb"].values[0]
    else:
        team2 = df[df.teamb==team1]["teama"].values[0]

    ##################################################  Gauge
    possession_A =  group_stage_data1[((group_stage_data1.date == dat) & (group_stage_data1.team_name == team1))]["possession"].values[0]
    pass_accuracy_A = group_stage_data1[((group_stage_data1.date == dat) & (group_stage_data1.team_name == team1))]["pass_accuracy"].values[0]
    gauge_possession_A = go.Figure(go.Indicator(
        domain={'x': [0, 1], 'y': [0, 1]},
        value=possession_A,
        mode="gauge+number",
        gauge={'axis': {'range': [None, 100]}, 'bar': {'color': "#5000bf"}}))
    gauge_possession_A.update_layout(
        height = 300,
        margin=dict(l=10, r=10, t=40, b=10),
        showlegend=False,
        template="plotly_dark",
        plot_bgcolor = 'rgba(0, 0, 0, 0)',
        paper_bgcolor = 'rgba(0, 0, 0, 0)',
        font_color="black",
        font_size= 15
    )

    gauge_pass_A = go.Figure(go.Indicator(
        domain={'x': [0, 1], 'y': [0, 1]},
        value=pass_accuracy_A,
        mode="gauge+number",
        gauge={'axis': {'range': [None, 100]}, 'bar': {'color': "#5000bf"}}))
    gauge_pass_A.update_layout(
        height = 300,
        margin=dict(l=10, r=10, t=40, b=10),
        showlegend=False,
        template="plotly_dark",
        plot_bgcolor = 'rgba(0, 0, 0, 0)',
        paper_bgcolor = 'rgba(0, 0, 0, 0)',
        font_color="black",
        font_size= 15
    )

    possession_B =  group_stage_data1[((group_stage_data1.date == dat) & (group_stage_data1.team_name == team2))]["possession"].values[0]
    pass_accuracy_B = group_stage_data1[((group_stage_data1.date == dat) & (group_stage_data1.team_name == team2))]["pass_accuracy"].values[0]
    gauge_possession_B = go.Figure(go.Indicator(
        domain={'x': [0, 1], 'y': [0, 1]},
        value=possession_B,
        mode="gauge+number",
        gauge={'axis': {'range': [None, 100]}, 'bar': {'color': "rgb(255,171,0)"}}))
    gauge_possession_B.update_layout(
        height = 300,
        margin=dict(l=10, r=10, t=40, b=10),
        showlegend=False,
        template="plotly_dark",
        plot_bgcolor = 'rgba(0, 0, 0, 0)',
        paper_bgcolor = 'rgba(0, 0, 0, 0)',
        font_color="black",
        font_size= 15
    )

    gauge_pass_B = go.Figure(go.Indicator(
        domain={'x': [0, 1], 'y': [0, 1]},
        value=pass_accuracy_B,
        mode="gauge+number",
        gauge={'axis': {'range': [None, 100]}, 'bar': {'color': "rgb(255,171,0)"}}))
    gauge_pass_B.update_layout(
        height = 300,
        margin=dict(l=10, r=10, t=40, b=10),
        showlegend=False,
        template="plotly_dark",
        plot_bgcolor = 'rgba(0, 0, 0, 0)',
        paper_bgcolor = 'rgba(0, 0, 0, 0)',
        font_color="black",
        font_size= 15
    )

    return (gauge_possession_A,gauge_pass_A,gauge_pass_B,gauge_possession_B)


########################

#############""

@callback(
    Output("country-sub-confederation-graph-output","figure"),
    [Input("country-sub-confederation-graph-value","value")]
)
def country_sub_confederation_graph(graph):
    # Count sub confederation 
    data =  data3.groupby("sub_confederation",as_index=False).size()
    data.columns = ["labels","Freq"]
    
    if graph == "pie-chart":
        fig = go.Figure(
            go.Pie(
                labels=list(data["labels"]),
                values=list(data["Freq"]),
                marker=dict(colors=colors),
                hoverinfo="label+value+percent",
                textinfo="label+value",
                texttemplate="%{label}<br>%{value:,.i}", 
                textposition="outside",
                hole=.57,
                rotation=60,
                insidetextorientation="radial"
            )
        )
        fig.update_layout(
            template="simple_white",
            margin=dict(autoexpand=True, l=0, t=0, r=0, b=0),
            height=300,
            font=dict(family="serif", size=14),
            legend=dict(orientation="v", x=0, y=0, bgcolor="rgba(0,0,0,0)"),
        )
    else:
        fig = go.Figure(
            go.Bar(
                y=data["labels"], 
                x=data["Freq"],
                orientation='h',
                marker=dict(color="navy"),
                text=data["Freq"]
            )
        )
        fig.update_layout(
            height=300,
            template="simple_white",
            margin=dict(autoexpand=True, l=0, r=0, b=0, t=0),
            hovermode="x",
            font=dict(family="serif", color="black"),
            yaxis=dict(categoryorder='total ascending'),
            xaxis=dict(
                showgrid=True,
                showline=True,
            )
        )
    
    return fig



@callback(
    Output("trophy-sub-confederation-graph-output","figure"),
    [Input("trophy-sub-confederation-graph-value","value")]
)
def trophie_graph(graph):

    # Extract 
    data = (data3[["sub_confederation","titres"]].pivot_table(index=["sub_confederation"],values=["titres"],aggfunc="sum")
            .reset_index(names="labels")
            .rename(columns={"titres" : "Freq"}))
    

    if graph == "pie-chart":
        fig = go.Figure(
            go.Pie(
                labels=list(data["labels"]),
                values=list(data["Freq"]),
                marker=dict(colors=colors),
                hoverinfo="label+value+percent",
                textinfo="label+value",
                texttemplate="%{label}<br>%{value:,.i}", 
                textposition="outside",
                hole=.57,
                rotation=60,
                insidetextorientation="radial"
            )
        )
        fig.update_layout(
            template="simple_white",
            margin=dict(autoexpand=True, l=0, t=0, r=0, b=0),
            height=300,
            font=dict(family="serif", size=14),
            legend=dict(orientation="v", x=0, y=0, bgcolor="rgba(0,0,0,0)"),
        )
    else:
        fig = go.Figure(
            go.Bar(
                y=data["labels"], 
                x=data["Freq"],
                orientation='h',
                marker=dict(color="navy"),
                text=data["Freq"]
            )
        )
        fig.update_layout(
            height=300,
            template="simple_white",
            margin=dict(autoexpand=True, l=0, r=0, b=0, t=0),
            hovermode="x",
            font=dict(family="serif", color="black"),
            yaxis=dict(categoryorder='total ascending'),
            xaxis=dict(
                showgrid=True,
                showline=True,
            )
        )
    
    return fig


@callback(
    Output("country-graph-output","figure"),
    [Input("country-graph-value","value")]
)
def country_graph_output(value):

    if value == "titre":
        data = data3[["team_name","titres"]]
        color_value = "navy"
    elif value == "appearances":
        data = data3["team_name"].to_frame()
        data.insert(1,"appearances",[int(x.split(" (")[0]) for x in data3["appearances"]])
        color_value = "green"
    
    data = data.merge(data3[["team_name","sub_confederation"]],on="team_name")
    # Set columns
    data.columns = ["labels","value","color"]


    fig = go.Figure(
        go.Bar(
            x=data["labels"], 
            y=data["value"],
            marker=dict(color=color_value),
            text=data["value"]
            )
        )
    fig.update_layout(
            height=300,
            template="simple_white",
            margin=dict(autoexpand=True, l=0, r=0, b=0, t=0),
            hovermode="x",
            font=dict(family="serif", color="black"),
            xaxis=dict(categoryorder='total descending'),
            yaxis=dict(
                showgrid=True,
                showline=True,
            )
        )
    fig.update_xaxes(tickangle=45)  
    
    return fig


@callback(
    Output("names-graph-output","figure"),
    [Input("names-graph-value","value")]
)
def names_graph_output(value):

    # Filter using value
    data = data3[data3["sub_confederation"]==value][["team_name","titres"]].set_index("team_name").reset_index()
    # Set Columns
    data.columns =  ["labels","value"]
    data = data.sort_values(by="value")

    fig = go.Figure(
        go.Bar(
            y=data["labels"], 
            x=data["value"],
            orientation='h',
            marker=dict(color=colors_dict[value]),
            text=data["value"]
            )
        )
    fig.update_layout(
            height=300,
            template="simple_white",
            margin=dict(autoexpand=True, l=0, r=0, b=0, t=0),
            hovermode="x",
            font=dict(family="serif", color="black"),
            xaxis=dict(categoryorder='total ascending'),
            yaxis=dict(
                showgrid=True,
                showline=True,
            )
        )
    return fig

@callback(
    Output("goal_graph","figure"),
    [Input("goal_value","value")]
)
def goal_plotly(value):

    merge_dataset = data4.merge(data3[["team_name","sub_confederation"]],on=["team_name"])
    
    merge_dataset.date = merge_dataset.date.astype(str)
    # Groupy 
    data = merge_dataset.groupby(value,as_index=False)["total_but"].sum()
    # Set columns
    data.columns = ["labels","value"]

    if value == "date":
        data["labels"] = [x.replace("-","_") for x in data["labels"]]

    if value == "name":
        color_value = "green"
    elif value == "team_name":
        color_value = "navy"
    elif value == "date":
        color_value = "firebrick"
    elif value == "sub_confederation":
        color_value = "orange"
    elif value == "step":
        color_value = "royalblue"

    # Create figure
    fig = go.Figure(
        go.Bar(
            x=data["labels"], 
            y=data["value"],
            marker=dict(color=color_value),
            text=data["value"]
        )
    )
    fig.update_layout(
        height=300,
        template="simple_white",
        margin=dict(autoexpand=True, l=0, r=0, b=0, t=0),
        hovermode="x",
        font=dict(family="serif", color="black"),
        xaxis=dict(categoryorder='total descending'),
        yaxis=dict(
            showgrid=True,
            showline=True,
        )
    )
    fig.update_xaxes(tickangle=45)  
    
    return fig


@callback(
    Output("country-goal-graph","figure"),
    [Input("country-goal-value","value")]
)
def country_goal_graph(value):

    if value == "goal-scored":
        data = data1.groupby("team_name",as_index=False)["goal_score"].sum()
        color_value = "green"
    elif value == "goal-conceded":
        data = data1.groupby("team_name",as_index=False)["goal_encaisse"].sum()
        color_value = "red"
    elif value == "goal-difference":
        data = data1.groupby("team_name",as_index=False)["goal_difference"].sum()
        color_value = "navy"

    # Set columns
    data.columns = ["labels","value"]
    
    fig = go.Figure(
        go.Bar(
            x=data["labels"], 
            y=data["value"],
            marker=dict(color=color_value),
            text=data["value"]
            )
        )
    fig.update_layout(
            height=300,
            template="simple_white",
            margin=dict(autoexpand=True, l=0, r=0, b=0, t=0),
            hovermode="x",
            font=dict(family="serif", color="black"),
            xaxis=dict(categoryorder='total descending'),
            yaxis=dict(
                showgrid=True,
                showline=True,
            )
        )
    fig.update_xaxes(tickangle=45)  
    
    return fig

#######################################################################################################################
#   Principal Components Analysis (PCA)
#######################################################################################################################
@callback(
    Output("pca-modal", "is_open"),
    [Input("pca-btn-open", "n_clicks"), 
     Input("pca-btn-close", "n_clicks")],
    [State("pca-modal", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open
    
# callback
@callback(
    Output("pca-tabs-content", "children"), 
    [Input("pca-tabs", "value")]
)
def switch_tab(value):
    if value == "pca-graphs-tab":
        return tab_graphes
    elif value == "pca-values-tab":
        return tab_valeurs
    elif value == "pca-description-tab":
        return tab_description
    elif value == "pca-summary-tab":
        return tab_summary
    elif value == "pca-data-tab":
        return tab_data

##### Update axis 2 dropdown
@callback(
        Output("axis2","options"),
        [Input("axis1","value")]
)
def update_axis2_options(value):
    val_list = [x for x in range(res_pca.n_components_) if x > value]
    return [{'label': i, 'value': i} for i in val_list]

########## Update axis 1 dropwdown
@callback(
        Output("axis1","options"),
        [Input("axis2","value")]
)
def update_axis1_options(value):
    val_list = [x for x in range(res_pca.n_components_) if x < value]
    return [{'label': i, 'value': i} for i in val_list]

#### Return Individuals Factor Map
@callback(
    Output("pca-row-graph-output","figure"),
    [Input("axis1","value"),
     Input("axis2","value"),
     Input("pca-row-graph-color","value")]
)
def pca_row_graph_output(axis1,axis2,color):
    
    # Change supplementary row color
    if color == "black":
        color_sup = "blue"
    elif color == "blue":
        color_sup = "black"
    elif color == "green":
        color_sup = "navy"

    fig = plotly_pca_ind(
        self=res_pca,
        axis=[axis1,axis2],
        color=color,
        color_sup=color_sup,
        text_size=12,
        title="",
        quali_sup=True
        )
    return fig

#### Return Variables Factor Map
@callback(
    Output("pca-var-graph-output","figure"),
    [Input("axis1","value"),
     Input("axis2","value"),
     Input("pca-var-graph-color","value")]
)
def pca_row_graph_output(axis1,axis2,color):
    # Change supplementary row color
    if color == "black":
        color_sup = "blue"
    elif color == "blue":
        color_sup = "black"
    elif color == "green":
        color_sup = "navy"

    fig = plotly_pca_var(
        self=res_pca,
        axis=[axis1,axis2],
        color=color,
        color_sup=color_sup,
        text_size=12,
        title="",
        add_circle=False,
        quanti_sup=True,
        )
    return fig


#### Values tabs
@callback(
    Output("pca-value-output","children"),
    [Input("pca-value-choice","value")]
)
def pca_value_output(value):
    if value == "eigen-res":
        return eigen_div
    elif value == "var-res":
        return var_div
    elif value == "ind-res":
        return ind_div
    elif value == "ind-sup-res":
        return ind_sup_div
    elif value == "var-sup-res":
        return var_sup_div
    elif value == "mod-sup-res":
        return var_qual_div

# Scree plot
@callback(
    Output("pca-scree-graph-output","figure"),
    [Input("pca-scree-graph-value","value")]
)
def pca_scree_graph_output(value):
    if value == "eigenvalue":
        color_value = "navy"
    else:
        color_value = "green"

    fig = plotly_screeplot(
        self=res_pca,
        choice=value,
        color=color_value
    )
    return fig

# Return Eigen table output
#################################################################################
#         Return Eigen Data as DataFrame
#--------------------------------------------------------------------------------
@callback(
    Output("pca-eigen-table-output","children"),
    [Input("pca-eigen-table-value","value")]
)
def pca_eigen_table_output(value):
    eigen = get_eigenvalue(res_pca).round(4).reset_index().rename(columns={"index":"Dimensions"})
    eigen = match_datalength(data=eigen,value=value)
    return DataTable(data=eigen)


#####################################################################################
#       Return Variables Elements
#-------------------------------------------------------------------------------------
# Return Variables Coordinates
@callback(
    Output("pca-var-coord-output","children"),
    [Input("pca-var-coord-value","value")]
)
def pca_var_coord_output(varcoordlen):
    varcoord = get_pca_var(res_pca)["coord"].round(4).reset_index().rename(columns={"index":"Variables"})
    varcoord = match_datalength(data=varcoord,value=varcoordlen)
    return DataTable(data=varcoord)

# Return Variables Contributions
@callback(
    Output("pca-var-contrib-output","children"),
    [Input("pca-var-contrib-value","value")]
)
def pca_var_contrib_output(varcontriblen):
    varcontrib = get_pca_var(res_pca)["contrib"].round(4).reset_index().rename(columns={"index":"Variables"})
    varcontrib = match_datalength(data=varcontrib,value=varcontriblen)
    return DataTable(data=varcontrib)

# Activate variable contribution modal
@callback(
    Output("pca-var-contrib-graph-modal", "is_open"),
    [Input("pca-var-contrib-graph-btn", "n_clicks"),
     Input("pca-var-contrib-close-btn","n_clicks")],
    [State("pca-var-contrib-graph-modal", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

@callback(
    Output("pca-var-contrib-graph-output","figure"),
    [Input("pca-var-contrib-axis-value","value"),
    Input("pca-var-contrib-top-value","value"),
    Input("pca-var-contrib-color-value","value"),
    Input("pca-var-contrib-barwidth-value","value")]
)
def pca_var_contrib_graph_output(axis,top,color,barwidth):
    fig = plotly_contrib(
        self=res_pca,
        choice="var",
        axis=axis,
        top_contrib=int(top),
        color=color,
        bar_width=barwidth
    )
    return fig

#### Return cos2 variables
@callback(
    Output("pca-var-cos2-output","children"),
    [Input("pca-var-cos2-value","value")]
)
def pca_var_cos2_output(varcos2len):
    varcos2 = get_pca_var(res_pca)["cos2"].round(4).reset_index().rename(columns={"index":"Variables"})
    varcos2 = match_datalength(data=varcos2,value=varcos2len)
    return DataTable(data=varcos2)

# Activate variable cos2 modal
@callback(
    Output("pca-var-cos2-graph-modal", "is_open"),
    [Input("pca-var-cos2-graph-btn", "n_clicks"),
     Input("pca-var-cos2-close-btn","n_clicks")],
    [State("pca-var-cos2-graph-modal", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

@callback(
    Output("pca-var-cos2-graph-output","figure"),
    [Input("pca-var-cos2-axis-value","value"),
    Input("pca-var-cos2-top-value","value"),
    Input("pca-var-cos2-color-value","value"),
    Input("pca-var-cos2-barwidth-value","value")]
)
def pca_var_cos2_graph_output(axis,top,color,barwidth):
    fig = plotly_cosines(
        self=res_pca,
        choice="var",
        axis=axis,
        top_cos2=int(top),
        color=color,
        bar_width=barwidth
    )
    return fig


#####################################################################################################
# Return Individuals Elements
######################################################################################################

######################################################################################
#       Return Individuals Elements
#---------------------------------------------------------------------------------------
# Individuals coordinates
@callback(
    Output("pca-ind-coord-output","children"),
    [Input("pca-ind-coord-value","value")]
)
def pca_ind_coord_output(indcoordlen):
    rowcoord = get_pca_ind(res_pca)["coord"].round(4).reset_index().rename(columns={"index" : "Individus"})
    rowcoord = match_datalength(data=rowcoord,value=indcoordlen)
    return DataTable(data=rowcoord)

# Return Individuals Contributions
@callback(
    Output("pca-ind-contrib-output","children"),
    [Input("pca-ind-contrib-value","value")]
)
def pca_ind_contrib_output(indcontriblen):
    rowcontrib = get_pca_ind(res_pca)["contrib"].round(4).reset_index().rename(columns={"index" : "Individus"})
    rowcontrib = match_datalength(data=rowcontrib,value=indcontriblen)
    return DataTable(data=rowcontrib)

# Activate rows contribution modal
@callback(
    Output("pca-ind-contrib-graph-modal", "is_open"),
    [Input("pca-ind-contrib-graph-btn", "n_clicks"),
     Input("pca-ind-contrib-close-btn","n_clicks")],
    [State("pca-ind-contrib-graph-modal", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

@callback(
    Output("pca-ind-contrib-graph-output","figure"),
    [Input("pca-ind-contrib-axis-value","value"),
    Input("pca-ind-contrib-top-value","value"),
    Input("pca-ind-contrib-color-value","value"),
    Input("pca-ind-contrib-barwidth-value","value")]
)
def pca_ind_contrib_graph_output(axis,top,color,barwidth):
    fig = plotly_contrib(
        self=res_pca,
        choice="ind",
        axis=axis,
        top_contrib=int(top),
        color=color,
        bar_width=barwidth
    )
    return fig

# Individuals Cos2
@callback(
    Output("pca-ind-cos2-output","children"),
    [Input("pca-ind-cos2-value","value")]
)
def pca_ind_cos2_output(indcos2len):
    rowcos2 = get_pca_ind(res_pca)["cos2"].round(4).reset_index().rename(columns={"index" : "Individus"})
    rowcos2 = match_datalength(data=rowcos2,value=indcos2len)
    return DataTable(data=rowcos2)

# Activate variable cos2 modal
@callback(
    Output("pca-ind-cos2-graph-modal", "is_open"),
    [Input("pca-ind-cos2-graph-btn", "n_clicks"),
     Input("pca-ind-cos2-close-btn","n_clicks")],
    [State("pca-ind-cos2-graph-modal", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

@callback(
    Output("pca-ind-cos2-graph-output","figure"),
    [Input("pca-ind-cos2-axis-value","value"),
    Input("pca-ind-cos2-top-value","value"),
    Input("pca-ind-cos2-color-value","value"),
    Input("pca-ind-cos2-barwidth-value","value")]
)
def pca_ind_cos2_graph_output(axis,top,color,barwidth):
    fig = plotly_cosines(
        self=res_pca,
        choice="ind",
        axis=axis,
        top_cos2=int(top),
        color=color,
        bar_width=barwidth
    )
    return fig


############################## Ad supplementary coordinates

# Supplementary continuous variables
@callback(
    Output("pca-var-sup-coord-output","children"),
    [Input("pca-var-sup-coord-value","value")]
)
def pca_var_sup_coord_output(varsupcoordlen):
    varsupcoord = get_pca_var(res_pca)["quanti_sup"]["coord"].round(4).reset_index().rename(columns={"index" : "Variables"})
    varsupcoord = match_datalength(data=varsupcoord,value=varsupcoordlen)
    return DataTable(data=varsupcoord)

# Supplementary continuous cosinus
@callback(
    Output("pca-var-sup-cos2-output","children"),
    [Input("pca-var-sup-cos2-value","value")])
def pca_var_sup_cos2_output(varsupcos2len):
    varsupcos2 = get_pca_var(res_pca)["quanti_sup"]["cos2"].round(4).reset_index().rename(columns={"index" : "Variables"})
    varsupcos2 = match_datalength(data=varsupcos2,value=varsupcos2len)
    return DataTable(data=varsupcos2)

###### Categoricl variables
# Supplementary Variables/Categories coordinates
@callback(
    Output("pca-mod-sup-coord-output","children"),
    [Input("pca-mod-sup-coord-value","value")]
)
def pca_mod_sup_coord_output(modsupcoordlen):
    modsupcoord = get_pca_var(res_pca)["quali_sup"]["coord"].round(4).reset_index().rename(columns={"index" : "Variables"})
    modsupcoord = match_datalength(data=modsupcoord,value=modsupcoordlen)
    return DataTable(data=modsupcoord)

# Supplementray variables/categories v-test
@callback(
    Output("pca-mod-sup-vtest-output","children"),
    [Input("pca-mod-sup-vtest-value","value")]
)
def pca_mod_sup_vtest_outout(modsupvtestlen):
    modsupvtest = get_pca_var(res_pca)["quali_sup"]["vtest"].round(4).reset_index().rename(columns={"index" : "Variables"})
    modsupvtest = match_datalength(data=modsupvtest,value=modsupvtestlen)
    return DataTable(data=modsupvtest)


###############################################################################################################################
#  Automatic Description of axes

@callback(
    Output("pca-continuous-desc-output", "children"), 
    [Input("pca-description-pvalue-value","value"),
     Input("pca-description-dimension-value","value"),
     Input("pca-continuous-desc-value","value")]
)
def pca_continuous_desc_output(pvalue,Dimdesc,lenvalue):
    DimDesc = dimdesc(self=res_pca,axis=None,proba=pvalue)
    if isinstance(DimDesc[Dimdesc],dict):
        DimDescQuanti = DimDesc[Dimdesc]["quanti"].reset_index().rename(columns={"index":"Variables"})
    elif isinstance(DimDesc[Dimdesc],pd.DataFrame):
        DimDescQuanti = DimDesc[Dimdesc].reset_index().rename(columns={"index":"Variables"})
    else:
        DimDescQuanti = pd.DataFrame()
    DimDescQuanti = match_datalength(DimDescQuanti,lenvalue)
    return  DataTable(data=DimDescQuanti)

@callback(
    Output("pca-categorical-desc-output", "children"), 
    [Input("pca-description-pvalue-value","value"),
     Input("pca-description-dimension-value","value"),
     Input("pca-categorical-desc-value","value")]
)
def pca_categorical_desc_output(pvalue,Dimdesc,lenvalue):
    DimDesc = dimdesc(self=res_pca,axis=None,proba=pvalue)
    if isinstance(DimDesc[Dimdesc],dict):
        DimDescQuali = DimDesc[Dimdesc]["quali"].reset_index().rename(columns={"index":"Variables"})
    else:
        DimDescQuali = pd.DataFrame()
    DimDescQuali = match_datalength(DimDescQuali,lenvalue)
    return  DataTable(data=DimDescQuali)

##########################################################################

#### Values tabs
@callback(
    Output("pca-summary-output","children"),
    [Input("pca-summary-value","value")]
)
def pca_summary_output(value):
    if value == "pca-summary-stats":
        return statistics_div
    elif value == "pca-summary-hist":
        return hist_div
    elif value == "pca-summary-corrmatrix":
        return corr_matrix_div
    

# Descriptive statistics
@callback(
    Output("pca-stats-desc-output","children"),
    [Input("pca-stats-desc-value","value")]
)
def pca_stats_desc_output(lenvalue):
    data = res_pca.active_data_
    if res_pca.quanti_sup_labels_ is not None:
        quanti_sup = res_pca.data_[res_pca.quanti_sup_labels_]
        data = pd.concat([data,quanti_sup],axis=1)
        if res_pca.row_sup_labels_ is not None:
            data = data.drop(index=res_pca.row_sup_labels_)

    StatsDesc = data.describe(include="all").round(4).T.reset_index().rename(columns={"index":"Variables"})
    StatsDesc = match_datalength(data=StatsDesc,value=lenvalue)
    return DataTable(data=StatsDesc)

###########################################################################################
# Histogram
@callback(
    Output("pca-hist-graph-output","figure"),
    [Input("pca-hist-graph-value","value"),
     Input("pca-hist-graph-fill-value","value")]
)
def pca_hist_graph_output(varlabel,fillcolor):
    data = res_pca.active_data_
    if res_pca.quanti_sup_labels_ is not None:
        quanti_sup = res_pca.data_[res_pca.quanti_sup_labels_]
        data = pd.concat([data,quanti_sup],axis=1)
        if res_pca.row_sup_labels_ is not None:
            data = data.drop(index=res_pca.row_sup_labels_)
    
    fig = px.histogram(data,x=varlabel,color_discrete_sequence = [fillcolor])
    fig.update_layout(
        xaxis_title=varlabel,
        yaxis_title="count",
        template="simple_white",
        margin=dict(autoexpand=True, l=0, t=0, r=0, b=0),
        height=450,
        font=dict(family="serif", size=14),
        legend=dict(orientation="v", x=0, y=0, bgcolor="rgba(0,0,0,0)"),
        showlegend=False
        )
    fig.update_traces(marker_line_width=1,marker_line_color="white")
    return fig

# Correlation Matrix
@callback(
    Output("pca-corr-matrix-output","children"),
    [Input("pca-corr-matrix-value","value")]
)
def pca_corr_matrix_output(lenvalue):
    data = res_pca.active_data_
    if res_pca.quanti_sup_labels_ is not None:
        quanti_sup = res_pca.data_[res_pca.quanti_sup_labels_]
        data = pd.concat([data,quanti_sup],axis=1)
        if res_pca.row_sup_labels_ is not None:
            data = data.drop(index=res_pca.row_sup_labels_)
    corr_mat = data.corr(method="pearson").round(4).reset_index().rename(columns={"index":"Variables"})
    corr_mat = match_datalength(corr_mat,lenvalue)
    return DataTable(data = corr_mat)

###############################################################################################################
#   Overall Data
################################################################################################################
@callback(
    Output("pca-overall-data-output","children"),
    [Input("pca-overall-data-value","value")]
)
def pca_overall_data_output(lenvalue):
    overalldata = res_pca.data_.reset_index().rename(columns={"Index" : "Individus"})
    overalldata = match_datalength(data=overalldata,value=lenvalue)
    return DataTable(data = overalldata)


###################################################################################################################
#  Logistic Regression Callback
####################################################################################################################

@callback(
    Output("target-graph-output","figure"),
    [Input("target-graph-value","value")]
)
def target_graph_output(graph):
    data = group_stage_data1.groupby("issue",as_index=False).size()
    data.columns = ["labels","Freq"]
    
    # Set columns
    color  = ["red","navy","green"]

    if graph == "pie-chart":
        fig = go.Figure(
            go.Pie(
                labels=list(data["labels"]),
                values=list(data["Freq"]),
                marker=dict(colors=color),
                hoverinfo="label+value+percent",
                textinfo="label+value",
                texttemplate="%{label}<br>%{value:,.i}", 
                textposition="outside",
                hole=.57,
                rotation=60,
                insidetextorientation="radial"
            )
        )
        fig.update_layout(
            template="simple_white",
            margin=dict(autoexpand=True, l=0, t=0, r=0, b=0),
            height=300,
            font=dict(family="serif", size=14),
            legend=dict(orientation="v", x=0, y=0, bgcolor="rgba(0,0,0,0)"),
        )
    else:
        fig = go.Figure(
            go.Bar(
                y=data["labels"], 
                x=data["Freq"],
                orientation='h',
                marker_color=color,
                text=data["Freq"]
            )
        )
        fig.update_layout(
            height=300,
            template="simple_white",
            margin=dict(autoexpand=True, l=0, r=0, b=0, t=0),
            hovermode="x",
            font=dict(family="serif", color="black"),
            yaxis=dict(categoryorder='total ascending'),
            xaxis=dict(
                showgrid=True,
                showline=True,
            )
        )
    
    return fig


###########################################################################################
# Histogram
@callback(
    Output("feature-graph-output","figure"),
    [Input("feature-graph-value","value"),
     Input("feature-graph-type-value","value"),
     Input("feature-graph-fill-value","value")]
)
def feature_graph_output(varlabel,graph,fillcolor):
    data = group_stage_data1.copy()
    if graph == "histogram":
        fig = px.histogram(data,x=varlabel,color_discrete_sequence = [fillcolor])
        fig.update_layout(
            xaxis_title=varlabel,
            yaxis_title="count",
            template="simple_white",
            margin=dict(autoexpand=True, l=0, t=0, r=0, b=0),
            height=450,
            font=dict(family="serif", size=14),
            legend=dict(orientation="v", x=0, y=0, bgcolor="rgba(0,0,0,0)"),
            showlegend=False
            )
        fig.update_traces(marker_line_width=1,marker_line_color="white")
    else:
        fig = px.box(data, y=varlabel)
        fig.update_layout(
            xaxis_title=varlabel,
            yaxis_title="value",
            template="simple_white",
            margin=dict(autoexpand=True, l=0, t=0, r=0, b=0),
            height=450,
            font=dict(family="serif", size=14),
            legend=dict(orientation="v", x=0, y=0, bgcolor="rgba(0,0,0,0)"),
            showlegend=False
            )
        fig.update_traces(marker=dict(size=5, symbol='circle', color=fillcolor), 
                          box=dict(facecolor=fillcolor, linewidth=2), 
                          whisker=dict(color='green', width=2), 
                          selector=dict(mode='markers'))
    return fig


@callback(
    Output("feature-target-graph-output","figure"),
    [Input("feature-boxplot-graph-value","value"),
     Input("feature-target-graph-type-value","value")]
)
def feature_target_graph_output(varlabel,graph):
    data = group_stage_data1.copy()
    # Set color
    color  = ["red","navy","green"]

    if graph == "histogram":
        fig = px.histogram(data,x=varlabel,color="issue",color_discrete_map = {"loss": "red","none": "navy","win":"green"})
        fig.update_layout(
            xaxis_title=varlabel,
            yaxis_title="Value",
            template="simple_white",
            margin=dict(autoexpand=True, l=0, t=0, r=0, b=0),
            height=450,
            font=dict(family="serif", size=14),
            legend=dict(orientation="h",yanchor="bottom",y=1.02,xanchor="right",x=1,font=dict(size=14,color="black")),
            showlegend=True
            )
        fig.update_traces(marker_line_width=1,marker_line_color="white")
    else:
        fig = px.box(data, x="issue",y=varlabel,color="issue",color_discrete_map = {"loss": "red","none": "navy","win":"green"})
        fig.update_layout(
            xaxis_title="issue",
            yaxis_title=varlabel,
            template="simple_white",
            margin=dict(autoexpand=True, l=0, t=0, r=0, b=0),
            height=450,
            font=dict(family="serif", size=14),
            legend=dict(orientation="h",yanchor="bottom",y=1.02,xanchor="right",x=1),
            showlegend=True
            )
    return fig