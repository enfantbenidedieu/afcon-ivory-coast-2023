
from dash import html, dcc
import dash_bootstrap_components as dbc
import dash_admin_components as dac


from function import ValueBox
from data_preparation import group_stage_data1


######################################################################################################"
#   Ordinal Logistic Regression
#######################################################################################################"



tab_logit = html.Div(
    children=[
        dbc.Row(html.H1("Logistic Regression")),
        html.P(),
        dbc.Row(
            children=[
                html.Div(
                    children=[
                        ValueBox(box_title="Accuracy",
                                 box_value=0,
                                 box_icon="database",
                                 box_color="primary",
                                 box_href="https://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html"),
                        ValueBox(box_title="Precision",
                                 box_value=0,
                                 box_icon="bookmark",
                                 box_color="success",
                                 box_href="https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_score.html"),
                        ValueBox(box_title="Recall",
                                 box_value=0,
                                 box_icon="list",
                                 box_color="primary",
                                 box_href="https://scikit-learn.org/stable/modules/generated/sklearn.metrics.recall_score.html"),
                        ValueBox(box_title="Area Under Curve (AUC)",
                                 box_value=0,
                                 box_icon="suitcase",
                                 box_color="success",
                                 box_href="https://scikit-learn.org/stable/modules/generated/sklearn.metrics.auc.html")
                    ],
                    className='row'
                )
            ],
            id="id_header"
        ),
        html.Div(
            children=[
                dac.SimpleBox(
                    style={"height" : "500px","width":"100%"},
                    title="Coefficients"
                ),
                dac.SimpleBox(
                    style={"height" : "500px","width":"100%"},
                    title="Odds - Ratio"
                )

            ],
            className='row'
        ),
        html.Div(
            children=[
                dac.SimpleBox(
                    style={"height" : "500px","width":"100%"},
                    title="Confusion Matrix",
                    width=4
                ),
                dac.SimpleBox(
                    style={"height" : "500px","width":"100%"},
                    title="ROC Curve",
                    width=4
                ),
                dac.SimpleBox(
                    style={"height" : "500px","width":"100%"},
                    title="LIFT Curve",
                    width=4
                )

            ],
            className='row'
        ),
        html.Div(
            children=[
                dac.SimpleBox(
                    style={"height" : "500px","width":"100%"},
                    title="Feature importance",
                    width=4
                ),
                dac.Box([
                    dac.BoxHeader(
                    collapsible=True,
                    collapsed=True,
                    title="Feature permutation"),
                ],
                solid_header=True,
                width=4),
                dac.Box([
                    dac.BoxHeader(
                    collapsible=True,
                    collapsed=True,
                    title="Feature permutation"),
                ],
                solid_header=True,
                width=4)

            ],
            className='row'
        ),
        html.P(),
        dbc.Row(html.H1("Penalized Logistic Regression")),
        html.P(),
        dbc.Row(
            children=[
                dbc.Col(
                    children=[
                        dbc.Card(
                            children=[
                                html.Label("Select a penalized algorithm"),
                                dcc.Dropdown(
                                    id="penalized-method",
                                    options=[
                                        {"label":x,"value":y} 
                                        for x,y in zip(["Rigde","Lasso","Elastic Net"],["ridge","lasso","elastic-net"])
                                    ],
                                    value="ridge",
                                    multi=False,
                                    placeholder="select a penalized algorithm"
                                )
                            ],
                            body=True,
                            className="controls_team",
                        )
                    ],
                    width=3)
            ]
        ),
        dbc.Row(
            children=[
                html.Div(
                    children=[
                        ValueBox(box_title="Accuracy",
                                 box_value=0,
                                 box_icon="database",
                                 box_color="primary",
                                 box_href="https://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html"),
                        ValueBox(box_title="Precision",
                                 box_value=0,
                                 box_icon="bookmark",
                                 box_color="success",
                                 box_href="https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_score.html"),
                        ValueBox(box_title="Recall",
                                 box_value=0,
                                 box_icon="list",
                                 box_color="primary",
                                 box_href="https://scikit-learn.org/stable/modules/generated/sklearn.metrics.recall_score.html"),
                        ValueBox(box_title="Area Under Curve (AUC)",
                                 box_value=0,
                                 box_icon="suitcase",
                                 box_color="success",
                                 box_href="https://scikit-learn.org/stable/modules/generated/sklearn.metrics.auc.html")
                    ],
                    className='row'
                )
            ],
            id="id_header"
        ),
        html.Div(
            children=[
                dac.SimpleBox(
                    style={"height" : "500px","width":"100%"},
                    title="Confusion Matrix",
                    width=4
                ),
                dac.SimpleBox(
                    style={"height" : "500px","width":"100%"},
                    title="ROC Curve",
                    width=4
                ),
                dac.SimpleBox(
                    style={"height" : "500px","width":"100%"},
                    title="LIFT Curve",
                    width=4
                )

            ],
            className='row'
        )
    ]
)