
# load packages
from dash import dcc, html
import dash_bootstrap_components as dbc
import dash_admin_components as dac


markdown = """

## Overview

The **Africa Cup of Nations** (French: __Coupe d'Afrique des Nations__), sometimes referred to as the **TotalEnergies Africa Cup of Nations** for sponsorship reasons, or simply **AFCON** or **CAN**, is the main international men's **association football** competition in Africa. 
It is **sanctioned** by the **Confederation of African Football** (CAF), and was first held in 1957. 
Since 1968, it has been held every two years, switching to odd-numbered years[n 1] in 2013.

In the first tournament in 1957, there were only three participating nations: Egypt, Sudan, and Ethiopia. 
South Africa was originally scheduled to join, but was disqualified due to the apartheid policies of the government then in power. 
Since then, the tournament has expanded greatly, making it necessary to hold a qualifying tournament. 
The number of participants in the final tournament reached 16 in 1998 (16 teams were to compete in 1996, 
but Nigeria withdrew, reducing the field to 15, and the same happened with Togo's withdrawal in 2010), 
and until 2017, the format had been unchanged, with the 16 teams being drawn into four groups of four teams each, 
with the top two teams of each group advancing to a "knock-out" stage. On 20 July 2017, the Africa Cup of Nations 
was moved from January to June and expanded from 16 to 24 teams.

Egypt is the most successful nation in the cup's history, winning the tournament seven times. 
Three trophies have been awarded during the tournament's history, with Cameroon five times and Ghana four times. 
The current trophy was first awarded in 2002. Egypt won an unprecedented three consecutive titles in 2006, 2008, and 2010. 
In 2013, the tournament format was switched to being held in odd-numbered years so as not to interfere with the FIFA World Cup.
Senegal are the tournament's current champions, having beaten Egypt on penalties in the 2021 final.

For more, see [https://en.wikipedia.org/wiki/Africa_Cup_of_Nations](https://en.wikipedia.org/wiki/Africa_Cup_of_Nations)
"""


presentation = html.Div([
    html.Div(
        [
            dac.UserCard(
                type=2,
                src = "/static/images/duverier.jpg",
                color = "info",
                title = "Duvérier DJIFACK Z.",
                subtitle = "Data Scientist & Quantitative Risk Analyst",
                elevation = 4,
                children="I'm the author of scientisttools package and others. I also found the DJIFACKLAB laboratory"
            ),
        ]
    ),
    html.Div([
        dac.SimpleBox(
            style={"height" : "500px","width":"100%"},
            title="Africa Cup of Nations",
            children=[
                dcc.Markdown(markdown)
            ],
            width=12
        ),
    ]),
    
])