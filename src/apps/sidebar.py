# -*- coding: utf-8 -*-

from dash import html
import dash_bootstrap_components as dbc

SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "18.5rem",
    "padding": "2rem 1rem",
    "background-color": "black",  # "#f8f9fa"
}

sidebar = html.Div(
    [
        html.Hr(),
        html.P(),
        dbc.Nav(
            [
                dbc.NavLink(html.Span([html.I(className="fa-solid fa-house"),
                                       html.Span("Overview", style={'font-size': 15, 'padding-left': 10})]),
                                       href = '/', active="exact"),
                dbc.NavLink(html.Span([html.I(className="fa-solid fa-dashboard"),
                                       html.Span("Dashboard", style={'font-size': 15, 'padding-left': 10})]),
                                       href="/dashboard", active="exact"),
                dbc.NavLink(html.Span([html.I(className="fa-solid fa-chart-line"),
                                       html.Span("Statistics", style={'font-size': 15, 'padding-left': 10})]),
                                       href="/statistics", active="exact"),
                dbc.NavLink(html.Span([html.I(className="fa-solid fa-database"),
                                       html.Span("Database", style={'font-size': 15, 'padding-left': 10})]),
                                       href="/database", active="exact")
            ],
            vertical=True,
            pills=True,
        )
    ],
    style=SIDEBAR_STYLE,
)