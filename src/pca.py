
from dash import dcc, html
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
from function import *
from data_preparation import *
from scientisttools.extractfactor import get_pca_ind, get_pca_var


Row = get_pca_ind(self=res_pca)
Var = get_pca_var(self=res_pca)

pca_markdown = '''
[Principal component analysis (PCA)](https://en.wikipedia.org/wiki/Principal_component_analysis) allows us to summarize and to visualize the information in a data set containing individuals/observations described by multiple inter-correlated quantitative variables. Each variable could be considered as a different dimension. If you have more than 3 variables in your data sets, it could be very difficult to visualize a multi-dimensional hyperspace.

Principal component analysis is used to extract the important information from a multivariate data table and to express this information as a set of few new variables called **principal components**. These new variables correspond to a linear combination of the originals. The number of principal components is less than or equal to the number of original variables.

The information in a given data set corresponds to the total variation it contains. The goal of PCA is to identify directions (or principal components) along which the variation in the data is maximal.

>
> In other words, PCA reduces the dimensionality of a multivariate data to two or three principal components, that can be visualized graphically, with minimal loss of information.
>
'''

cards = dbc.CardGroup(
    [
        dbc.Card(
            dbc.CardBody(
                [
                    dbc.CardImg(
                        src="/static/images/principal_components_analysis.png",
                        className="img-fluid rounded-start",
                    )
                ]
            )
        ),
        dbc.Card(
            dbc.CardBody(
                [
                    dcc.Markdown(pca_markdown) 
                ]
            )
        )
    ]
)

pca_modal = html.Div(
    [
        dbc.Row(
            [
                dbc.Card(
                children=[
                    html.Div([
                        dbc.Button(
                        html.H1("Principal Components Analysis (PCA)"), id="pca-btn-open", n_clicks=0,
                        outline=True, color="light", className="me-1")
                    ],
                    className="d-grid gap-2")
                ],
                body=True,
                className="attributes_card",
            )
            ],
            align="center"
        ),
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle(html.H2("PCA - Principal Component Analysis Essentials"))),
                dbc.ModalBody(
                    children=[
                        cards
                    ]
                ),
                dbc.ModalFooter(dbc.Button("Close", id="pca-btn-close", className="ms-auto", n_clicks=0)),
            ],
            id="pca-modal",
            size = "xl",
            is_open=False,
        ),
    ]
)

# Initialize point RadiotButtons choices
ptsradiobtn_choice =  [{"label": "Individus", "value": "IndActif"}]

# Add Supplementary Individuals
if res_pca.row_sup_labels_ is not None:
    val = {"label": "Individus supplémentaires", "value": "IndSupActif"}
    ptsradiobtn_choice.append(val)

# Add Supplementary Categories
if res_pca .quali_sup_labels_ is not None:
    val =  {"label": "Modalités supplémentaires", "value": "ModSupActif"}
    ptsradiobtn_choice.append(val)

body = html.Div(
    children=[
        dbc.Row(html.H1("Principal Components Analysis (PCA)")),
        html.P(),
        dbc.Row(
            children=[
                html.Div(
                    children=[
                        dcc.Tabs(
                            id="pca-tabs",
                            value='pca-graphs-tab',
                            children=[
                                dcc.Tab(label="Graphs", value="pca-graphs-tab"),
                                dcc.Tab(label="Values", value="pca-values-tab"),
                                dcc.Tab(label="Automatic description of axes", value="pca-description-tab"),
                                dcc.Tab(label="Summary of dataset", value="pca-summary-tab"),
                                dcc.Tab(label="Data", value="pca-data-tab"),
                            ]
                        ),
                        html.Div(id="pca-tabs-content"),
                    ],
                    id="main-panel"
                )
            ],
            align='bottom',
            id="pca-body"
        )

    ]
)


tab_graphes = html.Div(
    children=[
        dbc.Card(
            children=[
                dbc.CardBody(
                    children=[
                        dbc.Row(
                            children=[
                                dbc.Col(
                                    children=[
                                        dbc.Card(
                                            children=[
                                                dbc.Row(
                                                    children=[
                                                        dbc.Col(
                                                            children=[
                                                                html.Label("Axis:")
                                                            ],
                                                            sm=2
                                                        ),
                                                        dbc.Col(
                                                            children=[
                                                                dcc.Dropdown(
                                                                    id ="axis1",
                                                                    options=[
                                                                        {"label": x,"value" : x}  for x in range(res_pca.n_components_)
                                                                    ],
                                                                    value=0,
                                                                    multi=False,
                                                                    placeholder='axe vertical'
                                                                )
                                                            ],
                                                            sm=5
                                                        ),
                                                        dbc.Col(
                                                            children=[
                                                                dcc.Dropdown(
                                                                    id ="axis2",
                                                                    options=[
                                                                        {"label": x,"value" : x}  for x in range(res_pca.n_components_)
                                                                    ],
                                                                    value=1,
                                                                    multi=False,
                                                                    placeholder='axe horizontal'
                                                                )
                                                            ],
                                                            sm=5
                                                        )
                                                    ]
                                                )
                                            ],
                                            body=True,
                                            className="attributes_card",
                                        )
                                    ],
                                    sm=4
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
                                                html.H5("Individuals Factor Map - PCA",className="text-center mt-3 mb-1"),
                                                html.P(),
                                                html.Div(
                                                    className="selection d-flex justify-content-center mb-3",
                                                    children=[
                                                        dmc.ChipGroup(
                                                            [dmc.Chip(x, value=x) for x in ["black","blue","green"]],
                                                            value="black",
                                                            multiple=False,
                                                            id="pca-row-graph-color"
                                                        )
                                                    ]
                                                ),
                                                dcc.Loading(dcc.Graph(id="pca-row-graph-output",config=dict(displayModeBar=False),responsive=True))
                                            ],
                                            className="attributes_card"
                                        )

                                    ],
                                    sm=7
                                ),
                                dbc.Col(
                                    children=[
                                        dbc.Card(
                                            children=[
                                                html.H5("Variables Factor Map - PCA",className="text-center mt-3 mb-1"),
                                                html.P(),
                                                html.Div(
                                                    className="selection d-flex justify-content-center mb-3",
                                                    children=[
                                                        dmc.ChipGroup(
                                                            [dmc.Chip(x, value=x) for x in ["black","blue","green"]],
                                                            value="black",
                                                            multiple=False,
                                                            id="pca-var-graph-color"
                                                        )
                                                    ]
                                                ),
                                                dcc.Loading(dcc.Graph(id="pca-var-graph-output",config=dict(displayModeBar=False),responsive=True))
                                            ],
                                            className="attributes_card"

                                        )
                                    ],
                                    sm=5
                                )
                            ]
                        )
                    ]
                )
            ]
        )
    ]
)


tab_valeurs = html.Div(
    children=[
        dbc.Card(
            children=[
                dbc.CardBody(
                    children=[
                        dbc.Row(html.H4("Which outputs do you want ?")),
                        html.P(),
                        dbc.Row(
                            children=[
                                html.Div(
                                    className="selection d-flex justify-content-center mb-3",
                                    children=[
                                        dmc.ChipGroup(
                                            [dmc.Chip(lab, value=val) 
                                             for lab,val in zip(["Eigenvalues","Results of the variables","Results of the individuals",
                                                                 "Results of the supplementary individuals","Results of the supplementary variables","Results of the categorical variables"],
                                                                ["eigen-res","var-res","ind-res","ind-sup-res","var-sup-res","mod-sup-res"])],
                                            value="eigen-res",
                                            multiple=False,
                                            id="pca-value-choice"
                                        )

                                    ]
                                )
                            ]
                        ),
                        dbc.Row(html.Div(id="pca-value-output"))
                    ]
                )
            ]
        )
    ]
)

eigen_div = html.Div(
        children=[
            html.P(),
            dbc.Row(
                children=[
                    dbc.Col(
                        children=[
                            dbc.Row(html.H6("Parameters")),
                            html.P(),
                            dbc.Row(
                                children=[
                                    html.Div(
                                        className="selection d-flex justify-content-center mb-3",
                                        children=[
                                            dmc.ChipGroup(
                                            [dmc.Chip(lab, value=val) 
                                             for lab,val in zip(["Eigenvalue","Proportion"],["eigenvalue","proportion"])],
                                            value="proportion",
                                            multiple=False,
                                            id="pca-scree-graph-value"
                                        )

                                        ]
                                    )
                                ]
                            )
                        ],
                        sm=3
                    ),
                    dbc.Col(
                        children=[
                            dcc.Loading(dcc.Graph(id="pca-scree-graph-output",config=dict(displayModeBar=False),responsive=True))
                        ],
                        sm=9
                    )
                ]
            ),
            html.Hr(),
            PanelConditional1(text="eigen",name="table")
        ]
    )

# Variables Div
var_div = OverallPanelConditional(text="var")

# Individuals Div
ind_div = OverallPanelConditional(text="ind")

# Supplementary individuals
ind_sup_div = html.Div(
        children=[
            html.P(),
            html.H5("Coordinates"),
            PanelConditional1(text="ind-sup",name="coord"),
            html.Hr(),
            html.H5("Cos2 - Quality of representation"),
            PanelConditional1(text="ind-sup",name="cos2")
        ],
        id="pca-ind-sup-res"
    )


# Supplementary variables
var_sup_div = html.Div(
        children=[
            html.P(),
            html.H5("Coordinates"),
            PanelConditional1(text="var-sup",name="coord"),
            html.Hr(),
            html.H5("Cos2 - Quality of representation"),
            PanelConditional1(text="var-sup",name="cos2")
        ],
        id="pca-var-sup-res"
    )

var_qual_div = html.Div(
        children=[
            html.P(),
            html.H5("Coordinates"),
            PanelConditional1(text="mod-sup",name="coord"),
            html.Hr(),
            html.H5("V-test"),
            PanelConditional1(text="mod-sup",name="vtest")
        ]
    )

############################################################

tab_description = html.Div(
    children=[
        dbc.Card(
            children=[
                dbc.CardBody(
                    children=[
                        dbc.Row(
                            children=[
                                dbc.Col(
                                    children=[
                                        dbc.Row(html.H6("p-Value")),
                                        html.P(),
                                        dbc.Row(
                                            children=[
                                                html.Div(
                                                    className="selection d-flex justify-content-center mb-3",
                                                    children=[
                                                        dmc.ChipGroup(
                                                            [dmc.Chip(lab, value=val) 
                                                            for lab,val in zip(["Significance level 1%","Significance level 5%","Significance level 10%","None"],
                                                                               [0.01,0.05,0.1,1.0])],
                                                            value=0.05,
                                                            multiple=False,
                                                            id="pca-description-pvalue-value"
                                                        )
                                                    ]
                                                )
                                            ]
                                        )
                                    ],
                                    sm=6
                                ),
                                dbc.Col(
                                    children=[
                                        dbc.Row(html.H6("Choose the dimensions")),
                                        html.P(),
                                        dbc.Row(
                                            children=[
                                                html.Div(
                                                    className="selection d-flex justify-content-center mb-3",
                                                    children=[
                                                        dmc.ChipGroup(
                                                            [dmc.Chip(lab, value=val) 
                                                            for lab,val in zip(["Dimension 1","Dimension 2","Dimension 3"],
                                                                                ["Dim.1","Dim.2","Dim.3"])],
                                                            value="Dim.1",
                                                            multiple=False,
                                                            id="pca-description-dimension-value"
                                                        )
                                                    ]
                                                )
                                            ]
                                        )
                                    ],
                                    sm=6
                                )
                            ]
                        ),
                        html.P(),
                        dbc.Row(
                            children=[
                                html.H5("Quantitative"),
                                PanelConditional1(text="continuous",name="desc"),
                                html.Hr(),
                                html.H5("Qualitative"),
                                PanelConditional1(text="categorical",name="desc")
                            ]
                        ),

                    ]
                )

            ]
        )
    ]
)

###########################################
tab_summary = html.Div(
    children=[
        dbc.Card(
            children=[
                dbc.CardBody(
                    children=[
                        dbc.Row(html.H4("Which outputs do you want ?")),
                        html.P(),
                        dbc.Row(
                            children=[
                                html.Div(
                                    className="selection d-flex justify-content-center mb-3",
                                    children=[
                                        dmc.ChipGroup(
                                            [dmc.Chip(lab, value=val) 
                                             for lab,val in zip(["Descriptive statistics","Histogram","Correlation Matrix"],
                                                                ["pca-summary-stats","pca-summary-hist","pca-summary-corrmatrix"])],
                                            value="pca-summary-stats",
                                            multiple=False,
                                            id="pca-summary-value"
                                        )

                                    ]
                                )
                            ]
                        ),
                        dbc.Row(html.Div(id="pca-summary-output"))
                    ]
                )
            ]
        )
    ]
)

statistics_div = html.Div(
        children=[
            html.H5("Descriptive statistics"),
            html.P(),
            PanelConditional1(text="stats",name="desc")
        ]
    )

col_labels = list(res_pca.col_labels_)
if res_pca.quanti_sup_labels_ is not None:
    col_labels = [*col_labels, *res_pca.quanti_sup_labels_]

hist2_div = html.Div(
        children=[
            html.P(),
            dbc.Row(
                children=[
                    dbc.Col(
                        children=[
                            html.Label("Choose a variable"),
                            dcc.Dropdown(
                                id="pca-hist-graph-value",
                                options=[
                                    {"label" : x, "value" : x} for x in col_labels
                                ],
                                value=col_labels[0],
                                multi=False,
                                placeholder='Choose a variable'
                            ),
                            html.P(),
                            html.Label("fill color"),
                            dcc.Dropdown(
                                id="pca-hist-graph-fill-value",
                                options=[
                                    {"label" : x, "value" : x} for x in mcolors.CSS4_COLORS
                                ],
                                value="navy",
                                multi=False,
                                placeholder="Choose a fill color"
                            )
                        ],
                        sm=3
                    ),
                    dbc.Col(
                        children=[
                            dcc.Loading(dcc.Graph(id="pca-hist-graph-output",config=dict(displayModeBar=False),responsive=True))
                        ],
                        sm=9
                    )
                ]
            ),
            html.Br()
        ]
    )

hist_div = html.Div(
    children=[
        dbc.Card(
            children=[
                dbc.CardBody(
                    children=[
                        dbc.Row(
                            children=[
                                dbc.Col(
                                    children=[
                                        dbc.Card(
                                            children=[
                                                html.Label("Choose a variable"),
                                                dcc.Dropdown(
                                                    id="pca-hist-graph-value",
                                                    options=[
                                                        {"label" : x, "value" : x} for x in col_labels
                                                    ],
                                                    value=col_labels[0],
                                                    multi=False,
                                                    placeholder='Choose a variable'
                                                ),
                                                html.P(),
                                                html.Label("fill color"),
                                                dcc.Dropdown(
                                                    id="pca-hist-graph-fill-value",
                                                    options=[
                                                        {"label" : x, "value" : x} for x in mcolors.CSS4_COLORS
                                                    ],
                                                    value="navy",
                                                    multi=False,
                                                    placeholder="Choose a fill color"
                                                )
                                            ],
                                            body=True,
                                            className="controls_team"
                                        )
                                    ],
                                    sm=3
                                ),
                                dbc.Col(
                                    children=[
                                        dbc.Card(
                                            children=[
                                                dcc.Loading(dcc.Graph(id="pca-hist-graph-output",config=dict(displayModeBar=False),responsive=True))
                                            ],
                                            className="attributes_card"
                                        )
                                    ],
                                    sm=9
                                )
                            ]
                        )
                    ]
                )

            ]
        )

    ]
)

corr_matrix_div = html.Div(
        children=[
            html.H5("Correlation matrix"),
            html.P(),
            PanelConditional1(text="corr",name="matrix")
        ]
    )

tab_data = html.Div(
        children=[
            dbc.Card(
                children=[
                    dbc.CardBody(
                        children=[
                            html.H5("Data"),
                            html.P(),
                            PanelConditional1(text="overall",name="data")
                        ]
                    )
                ]
            )
        ]
    )

principal_component_analysis = html.Div(
    id="main-app", className="main-app",
    children=[
        body
    ]
)