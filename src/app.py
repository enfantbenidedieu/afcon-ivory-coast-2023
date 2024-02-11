# -*- coding: utf-8 -*-

from dash import Dash,html, dcc
import dash_bootstrap_components as dbc
from flask import Flask
from apps.sidebar import sidebar
from apps.navbar import navbar

from function import *
from callbacks import *

app_params = {
    "server": Flask(__name__),
    "title": "Africa Cup of Nations - Ivory Coast 2023",
    "update_title": "Wait a moment...",
    "url_base_pathname": "/",
    "external_stylesheets": [dbc.themes.MORPH,dbc.icons.FONT_AWESOME], # dbc.themes.MORPH
    "suppress_callback_exceptions": True,
    "meta_tags": [{'name': 'viewport', 'content': 'width=device-width, initial-scale=1.0'}]
}

server_params = {"debug": False}

app = Dash(__name__,**app_params)
server = app.server


CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
    'text-align' : 'justify',
    "background-color" : "black"
}


content = html.Div(id="page-content", style=CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id="url"),navbar,sidebar,content])

if __name__ == "__main__":
    app.run_server(**server_params,use_reloader=True)
