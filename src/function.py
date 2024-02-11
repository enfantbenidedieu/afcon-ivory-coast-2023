

# Load functions

import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
from dash_iconify import DashIconify
import dash_ag_grid as dag
import dash_admin_components as dac
import plotly.graph_objects as go
import plotly.express as px


def InfosBox(box_title,box_value,box_icon,box_color):
    box = dac.InfoBox(
        id="info-box",
        title=box_title,
        value=box_value,
        color = box_color,
        icon = box_icon
    )
    return box

def ValueBox(box_title,box_value,box_icon,box_color,box_href=None):
    if box_href is None:
        box = dac.ValueBox(
        id="value-box",
        value=box_value,
        subtitle=box_title,
        color=box_color,
        icon = box_icon)
    else:
        box = dac.ValueBox(
        id="value-box",
        value=box_value,
        subtitle=box_title,
        color=box_color,
        icon = box_icon,
        href=box_href)

    return box


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




#####
styles = {
    "label": {
        "&[data-checked]": {
            "&, &:hover": {
                "backgroundColor": "black",
                "color": "white",
            },
        },
    }
}


####################""

def pie_chart(data,label,value,colors):

    fig = go.Figure(
            go.Pie(
                labels=data[label],
                values=data[value],
                marker=dict(colors=colors),
                hoverinfo="label+value+percent",
                textinfo="label+value",
                texttemplate="%{label}<br>%{value:,.i}", 
                textposition="outside",
                pull=[0]*4+[.2],
                insidetextorientation="radial"
            )
        )
    fig.update_layout(
        template="plotly_dark",
        margin=dict(autoexpand=True, l=0, t=0, r=0, b=0),
        height=300,
        font=dict(family="serif", size=14),
        showlegend=False,
        plot_bgcolor='black',
        paper_bgcolor='black'
    )
    return fig