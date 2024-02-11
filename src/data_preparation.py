# -*- coding: utf-8 -*-

import pandas as pd

##### Import all sheet
files_xlsx = pd.ExcelFile("src/data/AFCON-2023.xlsx")

# Team information
team_infos =  pd.read_excel(files_xlsx, sheet_name="Team Infos")

# Stadium name 
Stadium = pd.read_excel(files_xlsx, sheet_name="Stadium")

# Overall Data
data = pd.read_excel(files_xlsx, sheet_name="AFCON-2023")

# Goals Data
goals = pd.read_excel(files_xlsx, sheet_name="Goals Overall")

### Goals Team
goals_team =  pd.read_excel(files_xlsx, sheet_name="Goals Team")

### Data set dictionnary
data_description = pd.read_excel(files_xlsx, sheet_name="Description")

