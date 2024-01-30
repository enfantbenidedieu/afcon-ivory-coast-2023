

import pandas as pd
import os
from scientisttools.decomposition import PCA
from statsmodels.miscmodels.ordinal_model import OrderedModel
from sklearn.preprocessing import StandardScaler

################################################## Data Preparation #########################################################

# Import dataset
data1 = pd.read_excel("src/data/AFCON-2023.xlsx",sheet_name=0)
# Nom des stades
data2 = pd.read_excel("src/data/AFCON-2023.xlsx",sheet_name=1)
# Données avec coordonnées et nom des coachs
data3 = pd.read_excel("src/data/AFCON-2023.xlsx",sheet_name=2)
# Données avec statistiques sur des buts
data4 = pd.read_excel("src/data/AFCON-2023.xlsx",sheet_name=3)

# Group stage data 
group_stage_data1 = data1[data1.step.isin(["Première journée","Deuxième journée","Troisième journée"])]
group_stage_data2 = data2[data2.step.isin(["Première journée","Deuxième journée","Troisième journée"])]
group_stage_data4 = data4[data4.step.isin(["Première journée","Deuxième journée","Troisième journée"])]

# Make a copy of original data
group_stage_odata1 = group_stage_data1.copy()
group_stage_date1_label = group_stage_odata1.date.astype(str).unique()

# Replace data
group_stage_data1["date"] = [x.replace("-","_") for x in group_stage_data1["date"].astype(str)]
group_stage_data2["date"] = [x.replace("-","_") for x in group_stage_data2["date"].astype(str)]
group_stage_date1_value = group_stage_data1.date.unique()

#### Round of 8
round_sixteen_data1 =  data1[data1.step.isin(["8è de finale"])]
round_sixteen_data1["date"] = [x.replace("-","_") for x in round_sixteen_data1["date"].astype(str)]

###################################################################################################################
#   Prepare dataset for Principal Components Analysis (PCA)
####################################################################################################################

# Make a copy
pca_dataset = group_stage_data1.copy()
# Recode step using
new_step = {
    "Première journée"  : "first",
    "Deuxième journée"  : "second",
    "Troisième journée" : "third" #,
    #"8è de finale"      : "8è_de_finale"
}
pca_dataset.step = pca_dataset.step.map(new_step)

# Drop date and group
pca_dataset = pca_dataset.drop(columns=["date","group"])

# Concatenate step and team-name
pca_dataset.insert(0,"team",pca_dataset[["team_name", "step"]].apply("_".join, axis=1))

# Drop step, team_name and foal_difference
pca_dataset = pca_dataset.drop(columns=["step","team_name","goal_difference"])

# Set team as index
pca_dataset = pca_dataset.set_index("team")
# Drop NA
pca_dataset = pca_dataset.dropna()

### Run PCA model
res_pca = PCA(
    normalize=True,
    n_components = None,
    row_labels=pca_dataset.index[:72],
    col_labels=pca_dataset.columns[:12],
    #row_sup_labels=pca_dataset.index[72:],
    quanti_sup_labels=["points"],
    quali_sup_labels=["issue"],
    parallelize=True).fit(pca_dataset)



##################################################################################################################################
#                                   Logistic Regression
##################################################################################################################################
columns = ["issue","goal_score","goal_encaisse","shots","shots_on_target","possession","passes","pass_accuracy","fouls","yellow_cards","red_cards"]
logit_data = group_stage_data1[columns]
# Transform to ordered categorica
logit_data["issue"]  = pd.Categorical(logit_data["issue"],ordered=True,categories=["loss","none","win"])

# Standardize the date
y = logit_data["issue"].to_frame()
X = logit_data[logit_data.columns[1:]]
sc = StandardScaler(with_mean=True,with_std=True)
sc.set_output(transform="pandas")
X_scale = sc.fit_transform(X)
D_scale = pd.concat([y,X_scale],axis=1)


features =  ["goal_score","goal_encaisse","shots","shots_on_target","possession","passes","pass_accuracy","fouls","yellow_cards","red_cards"]

ologit = OrderedModel(D_scale["issue"],D_scale[D_scale.columns[1:]],distr='logit').fit(method='bfgs', disp=False)

coef = pd.concat([ologit.params,ologit.bse,ologit.tvalues,ologit.pvalues,ologit.conf_int(0.05)],axis=1)
coef.columns = ["Estimate","Std. Error","z-value","Pr(>|z|)","[0.025","0.975]"]

