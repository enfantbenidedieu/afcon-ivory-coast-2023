

from dash import html
import dash_bootstrap_components as dbc
from function import NavItemBtn

# Header button
button_afcon = NavItemBtn('AFCON','afcon',"https://www.cafonline.com/caf-africa-cup-of-nations/", "primary")
button_pca = NavItemBtn(btn_name='PCA',id_name='pca',link='https://en.wikipedia.org/wiki/Principal_component_analysis',color="primary")
button_ologit = NavItemBtn(btn_name='Logistic Regression',id_name='logit',link="https://www.statsmodels.org/dev/examples/notebooks/generated/ordinal_regression.html",color='info')
button_lda = NavItemBtn('LDA','lda',"https://github.com/enfantbenidedieu/scientisttools/blob/master/scientisttools/discriminant_analysis.py",'info')
button_cart = NavItemBtn('CART','cart',"https://scikit-learn.org/stable/modules/classes.html#module-sklearn.tree",'primary')
button_knn = NavItemBtn('Knn','knn',"https://scikit-learn.org/stable/modules/classes.html#module-sklearn.neighbors",'primary')
button_github = NavItemBtn(btn_name='Github',id_name='github',link='https://github.com/enfantbenidedieu/scientisttools',color="info")
button_dash = NavItemBtn('Dash','dash','https://dash.plotly.com/',"primary")
button_plotly = NavItemBtn('Plotly','plotly','https://plotly.com/python/',"info")


# Header
header = dbc.Navbar(
        dbc.Container(
            children=[
                dbc.Row(
                    children=[
                        dbc.Col(
                            html.Img(
                                id="logo",
                                src="/static/images/afcon-2023.png",
                                height="45px",
                            ),
                            md="auto",
                        ),
                        dbc.Col(
                            children=[
                                html.Div(
                                    children=[
                                        html.H1("Africa Cup of Nations - Ivory Coast 2023",style={"color":"white"})
                                    ],
                                    id="app-title",
                                )
                            ],
                            md=True,
                            align="center",
                        ),
                    ],
                    align="center",
                ),
                dbc.Row(
                    children=[
                        dbc.Col(
                            children=[
                                dbc.NavbarToggler(id="navbar-toggler"),
                                dbc.Collapse(
                                    dbc.Nav(
                                        children=[
                                            button_afcon,
                                            button_pca,
                                            button_ologit,
                                            button_lda,
                                            button_cart,
                                            button_knn,
                                            button_github,
                                            button_dash,
                                            button_plotly
                                        ],
                                        navbar=True,
                                    ),
                                    id="navbar-collapse",
                                    navbar=True,
                                )
                            ],
                            md=2,
                        ),
                    ],
                    align="center",
                ),
            ],
            fluid=True,
        ),
        dark=False,
        color="dark",
        sticky="top",
        id="id_navbar"
    )
