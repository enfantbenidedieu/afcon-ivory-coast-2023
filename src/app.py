#
from dash import Dash,html, dcc
import dash_bootstrap_components as dbc
from flask import Flask
from apps.sidebar import sidebar
from apps.header import header

from function import *
from callbacks import *



#######################################################################################################################

# Parameters

add = {
            "href": "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css",
            #"href": "https://fontawesome.com/icons",
            "rel": "stylesheet",
            "integrity": "sha512-iBBXm8fW90+nuLcSKlbmrPcLa0OT92xO1BIsZ+ywDWZCvqsWgccV3gFoRBv0z+8dLJgyAHIhR35VZc2oM/gI1w==",
            "crossorigin": "anonymous",
            "referrerpolicy": "no-referrer",
        }
app_params = {
    "server": Flask(__name__),
    "title": "Africa Cup of Nations - Ivory Coast 2023",
    "update_title": "Wait a moment...",
    "url_base_pathname": "/",
    "external_stylesheets": [dbc.themes.MORPH,dbc.icons.FONT_AWESOME],
    "suppress_callback_exceptions": True,
    "meta_tags": [{'name': 'viewport', 'content': 'width=device-width, initial-scale=1.0'}]
}

server_params = {"debug": False}

app = Dash(__name__,**app_params)
app.title = "AFCON Ivory Coast 2023"
server = app.server


CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
    'textAlign' : 'justify',
}


content = html.Div(id="page-content", style=CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id="url"),header,sidebar,content])

if __name__ == "__main__":
    app.run_server(**server_params,use_reloader=True)
