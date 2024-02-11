# -*- coding: utf-8 -*-

from dash import dcc, html, callback, Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objs as go
from data_preparation import *
from plydata.tidy import pivot_wider, pivot_longer
from datetime import date
import numpy as np

# Import NavLink
from navlink.overview import overview
from navlink.database import database
from navlink.dashboard import dashboard
from navlink.statistics import statistics
from function import *

colors_dict = {
    "CECAFA"  : "firebrick",
    "COSAFA"  : "navy",
    "UNAF"    : "orange",
    "UNIFFAC" : "green",
    "WAFU"    : "royalblue"
}

colors = ["firebrick","green","navy","darkblue","orange"]

color_for_nodes = ["red","blue","violet","maroon","firebrick","darkblue","orange"] 


team_url_flag = {
    "Ivory Coast"       : "/static/images/FIF_Côte_d'Ivoire_logo.png",
    "Guinea-Bissau"     : "/static/images/Guinea-Bissau_FF_(logo).png",
    "Nigeria"           : "/static/images/Nigeria_national_football_team.png",
    "Equatorial Guinea" : "/static/images/Equatorial_Guinea_FA.png",
    "Egypt"             : "/static/images/Egypt_national_football_team.png",
    "Mozambique"        : "/static/images/Mozambique_national_football_team.png",
    "Ghana"             : "/static/images/Ghana_FA.png",
    "Cape Verde"        : "/static/images/Cape_Verde_FA_(2020).png",
    "Senegal"           : "/static/images/Senegalese_Football_Federation_logo.svg.png",
    "Gambia"            : "/static/images/Gambia_Football_Federation_(association_football_federation)_logo.png",
    "Cameroon"          : "/static/images/Cameroon_2010crest.png",
    "Guinea"            : "/static/images/Fgf_guinee_logo_shirt.png",
    "Algeria"           : "/static/images/Algerian_NT_(logo).png",
    "Angola"            : "/static/images/Logo_Federaçao_Angolana_de_Futebol.png",
    "Burkina Faso"      : "/static/images/Burkina_Faso_FA.png",
    "Mauritania"        : "/static/images/Mauritania_national_football_team.png",
    "Tunisia"           : "/static/images/Tunisia_national_football_team_logo.png",
    "Namibia"           : "/static/images/Namibia_FA.png",
    "Mali"              : "/static/images/Mali_FF_(New).png",
    "South Africa"      : "/static/images/South_Africa_Flor.png",
    "Morocco"           : "/static/images/Royal_Moroccan_Football_Federation_logo.svg.png",
    "Tanzania"          : "/static/images/Tanzania_FF_(logo).png",
    "DR Congo"          : "/static/images/Congo_DR_FA.png",
    "Zambia"            : "/static/images/Zambia_national_footnall_team.png"
}


# Define stadium url
url_stadium = {
    "Olympic Stadium of Ebimpé"                   : "/static/images/Olympic-Stadium-of-Ebimpe.jpg",
    "Félix Houphouët-Boigny Stadium"              : "/static/images/Stade-Felix-Houphouët-Boigny.jpg",
    "Charles Konan Banny of Yamoussoukro Stadium" : "/static/images/Stade-Charles-Konan-Banny-de-Yamoussoukro.jpg",
    "Bouaké Stadium"                              : "/static/images/Stade-Bouake.jpg",
    "Amadou Gon Coulibaly Stadium"                : "/static/images/Amadou-Gon-Coulibaly-Stadium.jpg",
    "San Pédro Stadium"                           : "/static/images/Stade-de-San-Pedro.jpg"
}

###################################################################################"
#   Render page content
#####################################################################################

@callback(
    Output("page-content", "children"), 
    [Input("url", "pathname")]
)
def render_page_content(pathname):
    if pathname == "/":
        return overview
    elif pathname == "/dashboard":
        return dashboard
    elif pathname == "/statistics":
        return statistics
    elif pathname == "/database":
        return database


################################################################################################################################
#   Dashboard Page
################################################################################################################################

# Define setp value filter
def step_value_filter(step_value):
    # Set columns to select
    if step_value == "group-stage":
        cat_to_select = ["Matchday 1","Matchday 2","Matchday 3"]
    elif step_value == "round-of-16":
        cat_to_select = ["Round of 16"]
    elif step_value == "quarter-final":
        cat_to_select = ["Quarter-final"]
    elif step_value == "semi-final":
        cat_to_select = ["Semi-final"]
    elif step_value == "match-for-3rd-place":
        cat_to_select = ["Match for 3rd place"]
    elif step_value == "final":
        cat_to_select = ["Final"]
    
    return cat_to_select

# Informations about Team
def Team_Infos(infos_value):
    if infos_value == "nickname":
        infos_name = "Nickname"
    elif infos_value == "manager":
        infos_name = "Manager"
    elif infos_value == "appearance":
        infos_name = "Appearances"
    elif infos_value == "best-result":
        infos_name = "Best result"
    elif infos_value == "trophies":
        infos_name = "Trophies"
    elif infos_value == "sub-confederation":
        infos_name = "Sub confederation"
    
    return infos_name

# Callback of step output
@callback(
    Output("dashboard-step-output","children"),
    [Input("dashboard-step-value","value")]
)
def dashboard_step_output(step_value):

    # Get value
    cat_to_select = step_value_filter(step_value)    
    # Filter to select the step    
    df = data[data["Step"].isin(values=cat_to_select)]
    
    # Transform Date as string
    df["Date"] = df["Date"].astype("str")
    date_value = np.unique([x.replace("-","_") for x in df["Date"].astype(str)])
    date_label = df["Day"].astype(str).unique()

    # Return a Card
    card = dbc.Card(
        children=[
            html.Label("Select a Date"),
            dcc.Dropdown(
                id="dashboard-date-value",
                options=[{"label":lab,"value":val} for lab,val in zip(date_label,date_value)],
                value=date_value[0],
                multi=False,
                placeholder="select a date"
            )
        ],
        body=True,
        className="controls_team",
    )
    return card

@callback(
    Output("dashboard-date-output","children"),
    [Input("dashboard-step-value","value"),
     Input("dashboard-date-value","value")]
)
def dashboard_date_output(step_value,date_value):
    
    cat_to_select = step_value_filter(step_value)    

    data["Date"] = [x.replace("-","_") for x in data["Date"].astype("str")]
    # Filter to select the step
    df = data[(data["Step"].isin(values=cat_to_select) & data["Date"].isin(values=[date_value]))]

    card = dbc.Card(
        children=[
            html.Label("Select a team"),
            dcc.Dropdown(
                id="dashboard-team-value",
                options=[
                    {
                        "label": html.Span(
                            [
                                html.Img(src=team_url_flag[x], height=20),
                                html.Span(x, style={'font-size': 15, 'padding-left': 10}),
                            ], style={'align-items': 'center', 'justify-content': 'center'}
                        ),
                        "value": x,
                    }  for x in df["Team name"].to_list()
                ],
                value=df["Team name"].to_list()[0],
                multi=False,
                placeholder="select a team"
            )
        ],
        body=True,
        className="controls_team"
    )
    return card

@callback(
    [Output("dashboard-graph-output","figure"),
     Output("dashboard-stadium-output","children"),
     Output("dashboard-team-one-name-output","children"),
     Output("dashboard-team-one-flag-output","children"),
     Output("dashboard-team-one-others-output","children"),
     Output("dashboard-team-one-score-output","children"),
     Output("dashboard-team-two-name-output","children"),
     Output("dashboard-team-two-flag-output","children"),
     Output("dashboard-team-two-others-output","children"),
     Output("dashboard-team-two-score-output","children"),
     Output("dashboard-team-one-shots-output","children"),
     Output("dashboard-team-one-yellow-cards-output","children"),
     Output("dashboard-team-one-red-cards-output","children"),
     Output("dashboard-team-one-results-output","children"),
     Output("dashboard-team-two-results-output","children"),
     Output("dashboard-team-two-red-cards-output","children"),
     Output("dashboard-team-two-yellow-cards-output","children"),
     Output("dashboard-team-two-shots-output","children"),
     Output("dashboard-team-one-possession-output","figure"),
     Output("dashboard-team-one-duel-success-rate-output","figure"),
     Output("dashboard-team-two-duel-success-rate-output","figure"),
     Output("dashboard-team-two-possession-output","figure"),
     Output("dashboard-team-stats-bar-output","figure"),
     Output("dashboard-team-stats-sankey-output","figure")],
     [Input("dashboard-step-value","value"),
      Input("dashboard-date-value","value"),
      Input("dashboard-team-value","value"),
      Input("dashboard-team-one-others-value","value"),
      Input("dashboard-team-two-others-value","value"),
      Input("dashboard-team-stats-value","value")]
)
def dashboard_global_output(step_value,date_value,team_one_value,team_one_others,team_two_others,team_stats):

    # Define step value
    cat_to_select = step_value_filter(step_value)    

    # Transform date as character
    data["Date"] = [x.replace("-","_") for x in data["Date"].astype("str")]
    Stadium["Date"] = [x.replace("-","_") for x in Stadium["Date"].astype("str")]

    # Filter to select the step and date
    df1 = data[(data["Step"].isin(values=cat_to_select) & data["Date"].isin(values=[date_value]))]
    df2 = Stadium[(Stadium["Step"].isin(values=cat_to_select) & Stadium["Date"].isin(values=[date_value]))]

    # Fine the Team 2 using dataframe 2
    if team_one_value in df2.TeamA.to_list():
        team_two_value = df2[df2["TeamA"]==team_one_value]["TeamB"].values[0]
    else:
        team_two_value = df2[df2["TeamB"]==team_one_value]["TeamA"].values[0]

    #### Columns to select
    columns = ["Possession","Duels success rate","Aerial duels won","Passing accuracy",
               "Crossing accuracy","Shooting accuracy","Tackles success rate"]

    df_team_one = df1[df1["Team name"] == team_one_value][columns].T
    df_team_one.columns = ["score"]
    df_team_two = df1[df1["Team name"] == team_two_value][columns].T
    df_team_two.columns = ["score"]

    list_scores1 = [df_team_one.index[i].capitalize() +' = ' + str(df_team_one['score'][i]) for i in range(len(df_team_one))]
    text_scores_teamA = team_one_value
    for i in list_scores1:
        text_scores_teamA += '<br>' + i
    
    list_scores2 = [df_team_two.index[i].capitalize() +' = ' + str(df_team_two['score'][i]) for i in range(len(df_team_two))]
    text_scores_teamB = team_two_value
    for i in list_scores2:
        text_scores_teamB += '<br>' + i
    
    polar_fig = go.Figure(data=go.Scatterpolar(
        name = text_scores_teamA,
        r=df_team_one["score"],
        theta=df_team_one.index,
        mode = 'markers',
        fill='toself', 
        marker_color = 'rgb(45,0,198)',   
        opacity =1, 
        hoverinfo = "text",
        text=[df_team_one.index[i] +' = ' + str(df_team_one['score'][i]) for i in range(len(df_team_one))]
    ))
    polar_fig.add_trace(go.Scatterpolar(
        name= text_scores_teamB,
        r=df_team_two["score"],
        theta=df_team_two.index,
        fill='toself',
        marker_color = 'rgb(255,171,0)',
        hoverinfo = "text" ,
        text=[df_team_two.index[i].capitalize() +' = ' + str(df_team_two['score'][i]) for i in range(len(df_team_two))]
        ))
    polar_fig.update_layout(
        polar=dict(
            hole=0.1,
            bgcolor="black",
            radialaxis=dict(
                visible=True,
                type='linear',
                autotypenumbers='strict',
                autorange=False,
                range=[0, 1+max(df_team_one.max().values,df_team_two.max().values)[0]],
                angle=90,
                showline=False,
                showticklabels=False, ticks='',
                gridcolor='black'),
                ),
        width = 450,
        height = 450,
        margin=dict(l=80, r=80, t=20, b=20),
        showlegend=False,
        template="plotly_dark",
        plot_bgcolor = 'rgba(0, 0, 0, 0)',
        paper_bgcolor = 'rgba(0, 0, 0, 0)',
        font_color="black",
        font_size= 10,
        yaxis = dict(tickfont = dict(size=10))
    )
    polar_fig.update_polars(angularaxis_color="white",angularaxis_tickangle=0)
    
    ## Extract Score
    score_team_one = df1[df1["Team name"] == team_one_value]["Goals"].values[0]
    score_team_two = df1[df1["Team name"] == team_two_value]["Goals"].values[0]
    color_card_one = None
    color_card_two = None
    if score_team_one == score_team_two:
        color_card_one = "light"
        color_card_two = "light"
        icon_team_one = "fa-solid fa-equals"
        icon_team_two = "fa-solid fa-equals"
    elif score_team_one > score_team_two:
        color_card_one = "success"
        color_card_two = "danger"
        icon_team_one = "fa-solid fa-thumbs-up"
        icon_team_two = "fa-solid fa-thumbs-down"
    else:
        color_card_one = "danger"
        color_card_two = "success"
        icon_team_one = "fa-solid fa-thumbs-down"
        icon_team_two = "fa-solid fa-thumbs-up"

    # Set team one color card
    card_team_one = dbc.Card(
        dbc.CardBody([
            html.Span(
                [
                    html.I(className=icon_team_one,style={'font-size': 30}),
                    html.Span(f"{team_one_value} : {int(score_team_one)}", style={'font-size': 20, 'padding-left': 10}),
                ]
            )]),
        className='controls_team',
        color=color_card_one
    )

    # Set team two color card
    card_team_two = dbc.Card(
        dbc.CardBody([
            html.Span(
                [
                    html.I(className=icon_team_two,style={'font-size': 30}),
                    html.Span(f"{team_two_value} : {int(score_team_two)}", style={'font-size': 20, 'padding-left': 10}),
                ]
            )]),
        className='controls_team',
        color=color_card_two
    )

    team_one_flag = html.Img(src=team_url_flag[team_one_value],className="playerImg")
    team_two_flag = html.Img(src=team_url_flag[team_two_value],className="playerImg")

    # Stadium name
    stadium_name = df2[((df2["TeamA"]==team_one_value) & (df2["TeamB"]==team_two_value)) | ((df2["TeamA"]==team_two_value) & (df2["TeamB"]==team_one_value))]["Stadium"].values[0]
    stadium_span =  html.Span(
        [
            html.Img(src=url_stadium[stadium_name], height=40,style={"text-align" : "center"}),
            html.Span(stadium_name, style={'font-size': 40, 'padding-left': 10,"font-weight":"bold","color":"red"}),
            ], style={'align-items': 'center', 'justify-content': 'center',"text-align":"center"}
        ),
    
    # Set others infos for team one
    team_one_infos = team_infos[team_infos["Team name"] == team_one_value][Team_Infos(team_one_others)].values[0]
    team_two_infos = team_infos[team_infos["Team name"] == team_two_value][Team_Infos(team_two_others)].values[0]

    ############################################################# Second Div informations #################################

    ##### Team one 
    team_one_shots         = df1[df1["Team name"] == team_one_value]["Shots"].values[0]
    team_one_yellow_cards  = df1[df1["Team name"] == team_one_value]["Yellow cards"].values[0]
    team_one_red_cards     = df1[df1["Team name"] == team_one_value]["Red cards"].values[0]
    team_one_result        = df1[df1["Team name"] == team_one_value]["Result"].values[0]
    team_one_result = html.Span(
        [
            html.I(className=icon_team_one,style={'font-size': 15}),
            html.Span(f"{team_one_result}", style={'font-size': 15, 'padding-left': 10}),
            ]
        )

    ###### Team two
    team_two_shots         = df1[df1["Team name"] == team_two_value]["Shots"].values[0]
    team_two_yellow_cards  = df1[df1["Team name"] == team_two_value]["Yellow cards"].values[0]
    team_two_red_cards     = df1[df1["Team name"] == team_two_value]["Red cards"].values[0]
    team_two_result        = df1[df1["Team name"] == team_two_value]["Result"].values[0]
    team_two_result = html.Span(
        [
            html.I(className=icon_team_two,style={'font-size': 15}),
            html.Span(f"{team_two_result}", style={'font-size': 15, 'padding-left': 10}),
            ]
        ) 

    gauge_possession_one = go.Figure(go.Indicator(
        domain={'x': [0, 1], 'y': [0, 1]},
        value= df1[df1["Team name"] == team_one_value]["Possession"].values[0],
        mode="number+delta+gauge",
        delta = {'reference': 50},
        number={'font_color':'white','suffix': "%"},
        gauge={'axis': {'range': [None, 100]}, 'bar': {'color': "#5000bf"}}))
    gauge_possession_one.update_layout(
        height = 200,
        margin=dict(l=10, r=10, t=40, b=10),
        showlegend=False,
        template="plotly_dark",
        plot_bgcolor = 'rgba(0, 0, 0, 0)',
        paper_bgcolor = 'rgba(0, 0, 0, 0)',
        font_color="black",
        font_size= 14
    )

    gauge_duel_success_rate_one = go.Figure(go.Indicator(
        domain={'x': [0, 1], 'y': [0, 1]},
        value=df1[df1["Team name"] == team_one_value]["Duels success rate"].values[0],
        mode="number+delta+gauge",
        delta = {'reference': 50},
        number={'font_color':'white','suffix': "%"},
        gauge={'axis': {'range': [None, 100]}, 'bar': {'color': "#5000bf"}}))
    gauge_duel_success_rate_one.update_layout(
        height = 200,
        margin=dict(l=10, r=10, t=40, b=10),
        showlegend=False,
        template="plotly_dark",
        plot_bgcolor = 'rgba(0, 0, 0, 0)',
        paper_bgcolor = 'rgba(0, 0, 0, 0)',
        font_color="black",
        font_size= 14
    )

    gauge_possession_two = go.Figure(go.Indicator(
        domain={'x': [0, 1], 'y': [0, 1]},
        value = df1[df1["Team name"] == team_two_value]["Possession"].values[0],
        mode="number+delta+gauge",
        delta = {'reference': 50},
        number={'font_color':'white','suffix': "%"},
        gauge={'axis': {'range': [None, 100]}, 'bar': {'color': "rgb(255,171,0)"}}))
    gauge_possession_two.update_layout(
        height = 200,
        margin=dict(l=10, r=10, t=40, b=10),
        showlegend=False,
        template="plotly_dark",
        plot_bgcolor = 'rgba(0, 0, 0, 0)',
        paper_bgcolor = 'rgba(0, 0, 0, 0)',
        font_color="black",
        font_size= 14
    )

    gauge_duel_success_rate_two = go.Figure(go.Indicator(
        domain={'x': [0, 1], 'y': [0, 1]},
        value=df1[df1["Team name"] == team_two_value]["Duels success rate"].values[0],
        mode="number+delta+gauge",
        delta = {'reference': 50},
        number={'font_color':'white','suffix': "%"},
        gauge={'axis': {'range': [None, 100]}, 'bar': {'color': "rgb(255,171,0)"}}))
    gauge_duel_success_rate_two.update_layout(
        height = 200,
        margin=dict(l=10, r=10, t=40, b=10),
        showlegend=False,
        template="plotly_dark",
        plot_bgcolor = 'rgba(0, 0, 0, 0)',
        paper_bgcolor = 'rgba(0, 0, 0, 0)',
        font_color="black",
        font_size= 14
    )
    
    # Set Team Stats
    if team_stats == "general":
        teamStats = ["Possession","Duels success rate","Aerial duels won","Interceptions","Offsides","Corners won"]
        xlabel = "General"
    elif team_stats == "distribution":
        teamStats = ["Passes","Long passes","Passing accuracy","PA in opponents half(%)","Crosses","Crossing accuracy"]
        xlabel = "Distribution"
    elif team_stats == "attack":
        teamStats = ["Goals","Shots","Shots on target","Blocked shots","Shots outside the box","Shots inside the box","Shooting accuracy"]
        xlabel = "Attack"
    elif team_stats == "defence":
        teamStats = ["Tackles","Tackles success rate","Clearances"]
        xlabel = "Defence"
    elif team_stats == "discipline":
        teamStats = ["Fouls conceded","Yellow cards","Red cards"]
        xlabel = "Discipline"
    
    # Insert "Team name"
    teamStats.insert(0,"Team name")
    team_Stats = df1[df1["Team name"].isin(values=[team_one_value,team_two_value])][teamStats]

    # Transform to long dataframe & set columns 2 nmeds
    team_Stats_long = team_Stats.melt(id_vars=["Team name"]).rename(columns={"variable":xlabel})
    
    # Transform to short dataframe and set index
    team_Stats_tab = pivot_wider(team_Stats_long,names_from="Team name",values_from="value").set_index(xlabel)

    # Compute proportion by team and reset index
    team_Stats_tab_prop = team_Stats_tab.apply(lambda x : 100*x/np.sum(x),axis=1).reset_index()

    # Reset index
    team_Stats_tab = team_Stats_tab.reset_index()

    # Transform to long dataframe
    team_Stats_tab = pivot_longer(team_Stats_tab,cols=[team_one_value,team_two_value],names_to="Team name",values_to="Value")
    team_Stats_tab_prop = pivot_longer(team_Stats_tab_prop,cols=[team_one_value,team_two_value],names_to="Team name",values_to="Proportion")

    # Merge the two table by 
    team_Stats_table = team_Stats_tab.merge(team_Stats_tab_prop,on= [xlabel,"Team name"])
    team_Stats_table["Proportion"] = team_Stats_table["Proportion"].round(1)

    # Stacked bar plot
    stacked_bar = px.bar(
        team_Stats_table, 
        y=xlabel, 
        x="Proportion",
        color="Team name",
        orientation="h",
        color_discrete_map={team_one_value: 'navy',team_two_value: 'green'},
        text="Proportion",
        text_auto='.3s')
    stacked_bar.update_layout(
        yaxis_title = "Proportion (%)",
        xaxis_title = xlabel,
        template="plotly_dark",
        margin=dict(autoexpand=True, l=0, t=0, r=0, b=0),
        height=300,
        font=dict(family="serif", size=14),
        plot_bgcolor='black',
        paper_bgcolor='black',
        legend=dict(orientation="h",
                    yanchor="top",
                    y=1.1,
                    xanchor="center",
                    x=0.5,
                    bgcolor="rgba(0,0,0,0)",
                    title=dict(text=f'<b> Team name </b>')),
        barmode="stack"
    )
    stacked_bar.update_traces(texttemplate='%{text:.2s}%',textposition='inside', insidetextanchor='middle')

    ########################################################## Sankey plot ##################################################
    # Original psot : https://lifewithdata.com/2022/08/29/how-to-create-a-sankey-diagram-in-plotly-python/

    links = team_Stats_table.iloc[:,[1,0,2]]
    links.columns = ["source","target","value"]

    # Find all the unique values in both the source and target columns
    unique_source_target = list(pd.unique(links[['source','target']].values.ravel('k')))

    #we need to create a mapping dictionary. We will use a dictionary comprehension to do that.
    mapping_dict = {k: v for v, k in enumerate(unique_source_target)}

    # we need to map these values to the links dataframe that we created earlier.
    links.loc[:,'source'] = links['source'].map(mapping_dict)
    links.loc[:,'target'] = links['target'].map(mapping_dict)

    # we will convert this dataframe into a dictionary.
    links_dict = links.to_dict(orient='list')

    ### update color list
    nodes_colors = color_for_nodes[1:len(unique_source_target)]
    # identify position of team one and team two in unique source target
    index_one = unique_source_target.index(team_one_value)
    index_two = unique_source_target.index(team_two_value)
    # Replace value
    nodes_colors[index_one] = "navy"
    nodes_colors[index_two] = "green"

    # Let’s create the Sankey diagram. Here we need to define two things – the node and the link of the Sankey diagram.
    sankey_fig = go.Figure(data=[go.Sankey(
        node = dict(
            pad = 15,
            thickness=20,
            line=dict(color='white', width=0.5),
            label = unique_source_target,
            color='green'
        ),
        link = dict(
            source= links_dict['source'],
            target = links_dict['target'],
            value = links_dict['value']
        )
    )
    ])
    sankey_fig.update_layout(
        xaxis_title = "links",
        template="plotly_dark",
        margin=dict(autoexpand=True, l=0, t=0, r=0, b=0),
        height=300,
        font=dict(family="serif", size=14),
        plot_bgcolor='black',
        paper_bgcolor='black'
    )
    sankey_fig.update_traces(node_color = nodes_colors)

    return (polar_fig,stadium_span,
            html.H3(team_one_value),team_one_flag,html.H5(team_one_infos),card_team_one,
            html.H3(team_two_value),team_two_flag,html.H5(team_two_infos),card_team_two,
            html.H6(f"{team_one_shots}"),html.H6(f"{team_one_yellow_cards}"),html.H6(f"{team_one_red_cards}"),team_one_result,
            team_two_result,html.H6(f"{team_two_yellow_cards}"),html.H6(f"{team_two_red_cards}"),html.H6(f"{team_two_shots}"),
            gauge_possession_one,gauge_duel_success_rate_one,
            gauge_duel_success_rate_two,gauge_possession_two,
            stacked_bar,sankey_fig)

######################################################################################################################################
#   Statistics paage
#######################################################################################################################################

######## Number of country by sub confedertion
@callback(
    Output("statistics-before-afcon-country-sub-confederation-graph-output","figure"),
    [Input("statistics-before-afcon-country-sub-confederation-graph-value","value")]
)
def country_sub_confederation_graph(graph):
    # Count sub confederation 
    data =  team_infos.groupby("Sub confederation",as_index=False).size()
    data.columns = ["labels","Freq"]
    
    if graph == "pie-chart":
        fig = pie_chart(data=data,label="labels",value="Freq",colors=list(colors_dict.values()))
    else:
        fig = go.Figure()
        for lab in data["labels"].unique():
            df = data[data["labels"]==lab]
            fig.add_traces(go.Bar(y=df["labels"],
                                  x=df["Freq"],
                                  text=df["Freq"],
                                  marker_color=colors_dict[lab],
                                  orientation="h",
                                  name=lab))
        fig.update_layout(
            height=300,
            template="simple_white",
            xaxis_title = "Number of country",
            yaxis_title = "Sub confederation",
            margin=dict(autoexpand=True, l=0, r=0, b=0, t=0),
            hovermode="x",
            font=dict(family="serif", color="black"),
            yaxis=dict(categoryorder='total ascending',color="white"),
            xaxis=dict(showgrid=True,showline=True,color="white"),
            plot_bgcolor='black',
            paper_bgcolor='black',
            showlegend = False
        )
        fig.update_traces(textposition='inside', insidetextanchor='end')
    
    return fig


################# Trophies by sub confederation
@callback(
    Output("statistics-before-afcon-trophy-sub-confederation-graph-output","figure"),
    [Input("statistics-before-afcon-trophy-sub-confederation-graph-value","value")]
)
def trophie_graph(graph):

    # Extract 
    data = (team_infos[["Sub confederation","Trophies"]].pivot_table(index=["Sub confederation"],values=["Trophies"],aggfunc="sum")
            .reset_index(names="labels")
            .rename(columns={"titres" : "Freq"}))
    data.columns = ["labels","Freq"]
    
    if graph == "pie-chart":
        fig = pie_chart(data=data,label="labels",value="Freq",colors=list(colors_dict.values()))
    else:
        fig = go.Figure()
        for lab in data["labels"].unique():
            df = data[data["labels"]==lab]
            fig.add_traces(go.Bar(y=df["labels"],
                                  x=df["Freq"],
                                  text=df["Freq"],
                                  marker_color=colors_dict[lab],
                                  orientation="h",
                                  name=lab))
        fig.update_layout(
            height=300,
            template="plotly_dark",
            xaxis_title = "Number of country",
            yaxis_title = "Sub confederation",
            margin=dict(autoexpand=True, l=0, r=0, b=0, t=0),
            hovermode="x",
            font=dict(family="serif", color="black"),
            yaxis=dict(categoryorder='total ascending',color="white"),
            xaxis=dict(showgrid=True,showline=True,color="white"),
            plot_bgcolor='black',
            paper_bgcolor='black',
            showlegend=False
        )
    
    return fig

######## Country by sub confederation with number of trophies

@callback(
    Output("statistics-before-afcon-names-graph-output","figure"),
    [Input("statistics-before-afcon-names-graph-value","value")]
)
def names_graph_output(value):

    # Filter using value
    data = team_infos[team_infos["Sub confederation"]==value][["Team name","Trophies"]].set_index("Team name").reset_index()
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
            template="plotly_dark",
            yaxis_title="Country",
            xaxis_title = "Number of trophies",
            margin=dict(autoexpand=True, l=0, r=0, b=0, t=0),
            hovermode="x",
            font=dict(family="serif", color="white"),
            xaxis=dict(categoryorder='total ascending',color="white"),
            yaxis=dict(
                showgrid=True,
                showline=True,
                color="white"
            ),
            plot_bgcolor='black',
            paper_bgcolor='black',
        )
    return fig

######## Order country by : trophie, appearances

@callback(
    Output("statistics-before-afcon-country-graph-output","figure"),
    [Input("statistics-before-afcon-country-graph-value","value")]
)
def country_graph_output(value):

    if value == "titre":
        data = team_infos[["Team name","Trophies"]]
        color_value = "navy"
        ylabel = "Number of trophies"
    elif value == "appearances":
        data = team_infos["Team name"].to_frame()
        data.insert(1,"Appearances",[int(x.split(" (")[0]) for x in team_infos["Appearances"]])
        color_value = "green"
        ylabel = "Number of appearances"
    
    data = data.merge(team_infos[["Team name","Sub confederation"]],on="Team name")
    # Set columns
    data.columns = ["labels","Freq","Sub confederation"]

    fig = go.Figure()
    for lab in colors_dict.keys():
        df = data[data["Sub confederation"] == lab]
        fig.add_traces(go.Bar(
            x=df["labels"], 
            y=df["Freq"],
            marker=dict(color=colors_dict[lab]),
            text=df["Freq"]
            ))

    fig.update_layout(
        height=300,
        template="simple_white",
        margin=dict(autoexpand=True, l=0, r=0, b=0, t=0),
        hovermode="x",
        font=dict(family="serif", color="black"),
        xaxis=dict(categoryorder='total descending',title = "Country",color="white"),
        yaxis=dict(showgrid=True,showline=True,title =  ylabel,color="white"),
        plot_bgcolor='black',
        paper_bgcolor='black',
        showlegend=False
    )
    fig.update_xaxes(tickangle=45)  
    
    return fig

############# Order goals by : players, country, date, sub confederation, step

@callback(
    Output("statistics-during-afcon-goal-graph-output","figure"),
    [Input("statistics-during-afcon-goal-graph-value","value")]
)
def goal_plotly(value):

    # Merging dataset
    merge_dataset = goals.merge(team_infos[["Team name","Sub confederation"]],on=["Team name"])
    merge_dataset["Date"] = merge_dataset["Date"].astype(str)

    # Define grouping value
    if value == "players":
        grouping_val = "Name"
    elif value == "country":
        grouping_val = "Team name"
    elif value == "date":
        grouping_val = "Date"
    elif value == "sub-confederation":
        grouping_val = "Sub confederation"
    elif value == "step":
        grouping_val = "Step"

    # Group by grouping vlue
    data = merge_dataset.groupby(grouping_val,as_index=False)["But"].sum()

    # Define columns
    data.columns = ["labels","Freq"]

    # ####
    if value == "players":
        data = data.sort_values(by="Freq").tail(10)
        color_value = "green"
        xlabel = "Players"
    elif value == "country":
        color_value = "navy"
        xlabel = "Country"
    elif value == "date":
        data["labels"] = [x.replace("-","_") for x in data["labels"]]
        color_value = "firebrick"
        xlabel = "Date"
    elif value == "sub-confederation":
        color_value = "orange"
        xlabel = "Sub confederation"
    elif value == "step":
        color_value = "royalblue"
        xlabel = "Step of competition"
    
    # # Create figure
    fig = go.Figure(
        go.Bar(
            x=data["labels"], 
            y=data["Freq"],
            marker=dict(color=color_value),
            text=data["Freq"]
        )
    )
    fig.update_layout(
        height=300,
        template="plotly_dark",
        margin=dict(autoexpand=True, l=0, r=0, b=0, t=0),
        hovermode="x",
        font=dict(family="serif", color="black"),
        xaxis=dict(categoryorder='total descending',title=xlabel,color="white"),
        yaxis=dict(showgrid=True,showline=True,title="Number of goals scored",color="white"),
        plot_bgcolor='black',
        paper_bgcolor='black'
    )
    fig.update_xaxes(tickangle=45)  
    
    return fig


################ Order country by : goals scored, goals conceced, goals difference

@callback(
    Output("statistics-during-afcon-country-goal-graph-output","figure"),
    [Input("statistics-during-afcon-country-goal-graph-value","value")]
)
def country_goal_graph(value):

    if value == "goal-scored":
        data = goals_team.groupby("Team name",as_index=False)["Goals scored"].sum()
        color_value = "green"
        ylabel = "Number of goals scored"
    elif value == "goal-conceded":
        data = goals_team.groupby("Team name",as_index=False)["Goals conceded"].sum()
        color_value = "red"
        ylabel = "Number of goals conceced"
    elif value == "goal-difference":
        data = goals_team.groupby("Team name",as_index=False)["Goals difference"].sum()
        color_value = "navy"
        ylabel = "Number of goals in difference"

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
        template="plotly_dark",
        margin=dict(autoexpand=True, l=0, r=0, b=0, t=0),
        hovermode="x",
        font=dict(family="serif", color="black"),
        xaxis=dict(categoryorder='total descending',title="Country",color="white"),
        yaxis=dict(showgrid=True,showline=True,title="Number of goals scored",color="white"),
        plot_bgcolor='black',
        paper_bgcolor='black'
    )
    fig.update_xaxes(tickangle=45)
    return fig


#####################################################################################################################
#   Download DataFrame as xlsx
#####################################################################################################################

@callback(
    Output("download-team-infos-xlsx", "data"),
    Input("team-infos-btn-xlsx", "n_clicks"),
    prevent_initial_call=True,
)
def func(n_clicks):
    return dcc.send_data_frame(team_infos.to_excel, "AFCON - Ivory Coast 2023-"+str(date.today())+".xlsx", sheet_name="Team Infos")

@callback(
    Output("download-stadium-xlsx", "data"),
    Input("stadium-btn-xlsx", "n_clicks"),
    prevent_initial_call=True,
)
def func(n_clicks):
    return dcc.send_data_frame(Stadium.to_excel, "AFCON - Ivory Coast 2023-"+str(date.today())+".xlsx", sheet_name="Stadium")


@callback(
    Output("download-goals-xlsx", "data"),
    Input("goals-btn-xlsx", "n_clicks"),
    prevent_initial_call=True,
)
def func(n_clicks):
    return dcc.send_data_frame(goals.to_excel, "AFCON - Ivory Coast 2023-"+str(date.today())+".xlsx", sheet_name="Goals")


@callback(
    Output("download-data-xlsx", "data"),
    Input("data-btn-xlsx", "n_clicks"),
    prevent_initial_call=True,
)
def func(n_clicks):
    return dcc.send_data_frame(data.to_excel, "AFCON - Ivory Coast 2023-"+str(date.today())+".xlsx", sheet_name="AFCON-2023")