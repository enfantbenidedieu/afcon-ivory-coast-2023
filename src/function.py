

# Load functions
from dash import html, dcc,dash_table
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
from dash_iconify import DashIconify
import dash_admin_components as dac
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
import matplotlib.colors as mcolors
import plotnine as pn
from scientisttools.extractfactor import get_eigenvalue

def NavItemBtn(btn_name,id_name,link, color):
    return dbc.NavItem(
                dbc.Button(
                    btn_name,
                    id = id_name,
                    outline=True,
                    href=link,
                    style={"textTransform": "none"},
                    color=color
                )
            )

def GithubBtn(btn_link):
    return dmc.Tooltip(
                label="Code source",
                position="bottom",
                withArrow=True,
                arrowSize=6,
                color="black",
                transition="scale",
                transitionDuration=300,
                ff="serif",
                className="m3 ms-3",
                children=[
                    dbc.Button(href=btn_link, 
                        className="btn", 
                        children=[
                            DashIconify(icon="radix-icons:github-logo",width=30), 
                        ]
                    )
                ]
            )


# Return DataFrame as DataTable
# https://dash.plotly.com/datatable/interactivity
def DataTable(data):
    return dash_table.DataTable(
        data=data.to_dict("records"),
        columns=[{"name": i, "id": i,} for i in data.columns],
        style_as_list_view=False,
        style_header={'backgroundColor': '#657E95','fontWeight': 'bold','color': 'white'},
        style_data={'color': 'white','backgroundColor': '#3B4D5E'},
        style_cell_conditional=[{'if': {'column_id': c},'textAlign': "center"} for c in data.columns[1:]],
        style_cell={
            'overflow': 'hidden',
            'textOverflow': 'ellipsis',
            'maxWidth': 0
        },
        style_table={'overflowX': 'auto'},
        fixed_columns={'headers': True, 'data': 1},
        editable=True,
        filter_action="native",
        sort_action="native",
        sort_mode="multi",
        column_selectable="single",
        row_deletable=False,
        selected_columns=[],
        selected_rows=[],
        page_action="native",
        page_current= 0,
        page_size= 10
    )

def InfosBox(box_title,box_value,box_icon,box_color):
    box = dac.InfoBox(
        title=box_title,
        value=box_value,
        color = box_color,
        icon = box_icon
    )
    return box

def ValueBox(box_title,box_value,box_icon,box_color,box_href=None):
    if box_href is None:
        box = dac.ValueBox(
        value=box_value,
        subtitle=box_title,
        color=box_color,
        icon = box_icon)
    else:
        box = dac.ValueBox(
        value=box_value,
        subtitle=box_title,
        color=box_color,
        icon = box_icon,
        href=box_href)

    return box

def controls_team(name,dropdown):
    card = dbc.Card(
        children=[
            html.Label(name),
            html.Br(),
            dropdown
        ],
        body=True,
        className="controls_team"
    )

##########################################################################################################
#   Principal Components Analysis (PCA) graphs
##########################################################################################################
    
###########################"
# Color in ["cos2","contrib"]

from ast import literal_eval
import numpy as np
from plotly.colors import *

def get_color_for_val(val, vmin, vmax, pl_colors):
    
    if pl_colors[0][:3] != 'rgb':
        raise ValueError('This function works only with Plotly  rgb-colorscales')
    if vmin >= vmax:
        raise ValueError('vmin should be < vmax')
    
    scale = [k/(len(pl_colors)-1) for k in range(len(pl_colors))] 
   
   
    colors_01 = np.array([literal_eval(color[3:]) for color in pl_colors])/255.  #color codes in [0,1]
   
    v= (val - vmin) / (vmax - vmin) # val is mapped to v in [0,1]
    #find two consecutive values in plotly_scale such that   v is in  the corresponding interval
    idx = 1
   
    while(v > scale[idx]): 
        idx += 1
    vv = (v - scale[idx-1]) / (scale[idx] -scale[idx-1] )
    
    #get   [0,1]-valued color code representing the rgb color corresponding to val
    val_color01 = colors_01[idx-1] + vv * (colors_01[idx ] - colors_01[idx-1])
    val_color_0255 = (255*val_color01+0.5).astype(int)
    return f'rgb{str(tuple(val_color_0255))}'

def plotly_pca_ind(self,
                    axis=[0,1],
                    title =None,
                    color ="black",
                    text_size = 12,
                    ind_sup=True,
                    color_sup = "blue",
                    legend_title=None,
                    add_ellipse=False, 
                    ellipse_type = "t",
                    confint_level = 0.95,
                    geom_ellipse = "polygon",
                    habillage = None,
                    quali_sup = True,
                    color_quali_sup = "red",
                    lim_contrib = None,
                    lim_cos2 = None):
    
    if self.model_ != "pca":
        raise ValueError("Error : 'self' must be an instance of class PCA.")
    
    if ((len(axis) !=2) or 
        (axis[0] < 0) or 
        (axis[1] > self.n_components_-1)  or
        (axis[0] > axis[1])) :
        raise ValueError("Error : You must pass a valid 'axis'.")

    coord = pd.DataFrame(self.row_coord_,index = self.row_labels_,columns=self.dim_index_)

    # Add categorical supplementary variables
    if self.quali_sup_labels_ is not None:
        coord[self.quali_sup_labels] = self.data_[self.quali_sup_labels_]
    
    # Using lim cos2
    if lim_cos2 is not None:
        if isinstance(lim_cos2,float):
            cos2 = (pd.DataFrame(self.row_cos2_,index = self.row_labels_,columns=self.dim_index_)
                       .iloc[:,axis].sum(axis=1).to_frame("cosinus").sort_values(by="cosinus",ascending=False)
                       .query(f"cosinus > {lim_cos2}"))
            if cos2.shape[0] != 0:
                coord = coord.loc[cos2.index,:]
    
    # Using lim contrib
    if lim_contrib is not None:
        if isinstance(lim_contrib,float):
            contrib = (pd.DataFrame(self.row_contrib_,index = self.row_labels_,columns=self.dim_index_)
                       .iloc[:,axis].sum(axis=1).to_frame("contrib").sort_values(by="contrib",ascending=False)
                       .query(f"contrib > {lim_contrib}"))
            if contrib.shape[0] != 0:
                coord = coord.loc[contrib.index,:]

    if color == "cos2":
        c = np.sum(self.row_cos2_[:,axis],axis=1)
        if legend_title is None:
            legend_title = "cos2"
    elif color == "contrib":
        c = np.sum(self.row_contrib_[:,axis],axis=1)
        if legend_title is None:
            legend_title = "Contrib"
    elif isinstance(color,np.ndarray):
        c = np.asarray(color)
        if legend_title is None:
            legend_title = "Cont_Var"
    elif hasattr(color, "labels_"):
            c = [str(x+1) for x in color.labels_]
            if legend_title is None:
                legend_title = "Cluster"
        
    # Initialize
    fig = go.Figure()

    if habillage is None :        
        # Using cosine and contributions
        if color in ["cos2","contrib"] or isinstance(color,np.ndarray):
            coord.loc[:,legend_title] = c
            coord[legend_title] = coord[legend_title].astype(float)
            # Initialize
            fig = px.scatter(coord,x="Dim."+str(axis[0]+1),y="Dim."+str(axis[1]+1),color=legend_title,
                                color_continuous_scale=["red", "green", "blue"])
            for i , name in enumerate(coord.index):
                fig = fig.add_annotation(x=coord.iloc[i,axis[0]], y=coord.iloc[i,axis[1]],text=name,font=dict(size=text_size, color=color))
            #fig.update_annotations()
        elif hasattr(color, "labels_"):
            coord.loc[:,legend_title] = c
            coord[legend_title] = coord[legend_title].astype(str)
            # Initialize
            fig = px.scatter(coord,x="Dim."+str(axis[0]+1),y="Dim."+str(axis[1]+1),color=legend_title,
                                color_continuous_scale=["red", "green", "blue"])
            for i , name in enumerate(coord.index):
                fig = fig.add_annotation(x=coord.iloc[i,axis[0]], y=coord.iloc[i,axis[1]],text=name)
            fig.update_annotations(font=dict(size=text_size,color=color))
        else:
            fig = px.scatter(coord,x="Dim."+str(axis[0]+1),y="Dim."+str(axis[1]+1))
            for i , name in enumerate(coord.index):
                fig = fig.add_annotation(x=coord.iloc[i,axis[0]], y=coord.iloc[i,axis[1]],text=name,
                                         font=dict(size=text_size,color=color))
            fig.update_traces(textposition='top center')
            fig.update_layout(showlegend=False)
            #fig.update_annotations(font=dict(size=text_size, color=color))
    else:
        if self.quali_sup_labels_ is not None:
            # Initialize
            fig = px.scatter(coord,x="Dim."+str(axis[0]+1),y="Dim."+str(axis[1]+1),color=habillage)
            for i , name in enumerate(coord.index):
                fig = fig.add_annotation(x=coord.iloc[i,axis[0]], y=coord.iloc[i,axis[1]],text=name,
                                         font=dict(size=text_size))
    
    if ind_sup:
        if self.row_sup_labels_ is not None:
            sup_coord = pd.DataFrame(self.row_sup_coord_,index=self.row_sup_labels_,columns=self.dim_index_)
            # Update figure
            fig.add_scatter(x=sup_coord.loc[:,"Dim."+str(axis[0]+1)],
                            y=sup_coord.loc[:,"Dim."+str(axis[1]+1)], mode="markers")
            for i , name in enumerate(sup_coord.index):
                fig = fig.add_annotation(x=sup_coord.iloc[i,axis[0]], y=sup_coord.iloc[i,axis[1]],text=name,
                                         font=dict(size=text_size,color=color_sup))
            
    if quali_sup:
        if self.quali_sup_labels_ is not None:
            mod_sup_coord = pd.DataFrame(self.mod_sup_coord_,columns=self.dim_index_,index=self.short_sup_labels_)
            fig.add_scatter(x=mod_sup_coord.loc[:,"Dim."+str(axis[0]+1)],
                            y=mod_sup_coord.loc[:,"Dim."+str(axis[1]+1)], mode="markers")
            for i , name in enumerate(mod_sup_coord.index):
                fig = fig.add_annotation(x=mod_sup_coord.iloc[i,axis[0]], y=mod_sup_coord.iloc[i,axis[1]],text=name,
                                         font=dict(size=text_size,color=color_quali_sup))

    # Add additionnal        
    proportion = self.eig_[2]
    xlabel = "Dim."+str(axis[0]+1)+" ("+str(round(proportion[axis[0]],2))+"%)"
    ylabel = "Dim."+str(axis[1]+1)+" ("+str(round(proportion[axis[1]],2))+"%)"

    if title is None:
        title = "Individuals factor map - PCA"
    # Add horizontal line
    fig.add_hline(y=0.0,line_width=1,line_dash="dot",line_color="black")
    # Add Vertical Line
    fig.add_vline(x=0.0,line_width=1,line_dash="dot",line_color="black")
    fig.update_layout(
        xaxis_title=xlabel,
        yaxis_title=ylabel,
        template="simple_white",
        margin=dict(autoexpand=True, l=0, t=0, r=0, b=0),
        height=450,
        width=800,
        font=dict(family="serif", size=14),
        legend=dict(orientation="v", x=0, y=0, bgcolor="rgba(0,0,0,0)")
        )
    return fig

# Correlation Circle
def plotly_pca_var(self,
                    axis=[0,1],
                    title =None,
                    color ="blue",
                    add_labels = True,
                    text_size = 12,
                    quanti_sup=True,
                    color_sup = "red",
                    linestyle_sup="dot",
                    legend_title = None,
                    add_hline = True,
                    add_vline=True,
                    va="middle", # "top", "middle","bottom"
                    hline_color="black",
                    hline_style="dot",
                    vline_color="black",
                    vline_style ="dot",
                    add_circle = True,
                    lim_cos2 = None,
                    lim_contrib = None) :
    
    if self.model_ != "pca":
        raise ValueError("Error : 'self' must be an instance of class PCA.")
    
    if ((len(axis) !=2) or 
        (axis[0] < 0) or 
        (axis[1] > self.n_components_-1)  or
        (axis[0] > axis[1])) :
        raise ValueError("Error : You must pass a valid 'axis'.")

    coord = pd.DataFrame(self.col_coord_,index = self.col_labels_,columns=self.dim_index_)

    # Using lim cos2
    if lim_cos2 is not None:
        if isinstance(lim_cos2,float):
            cos2 = (pd.DataFrame(self.col_cos2_,index = self.col_labels_,columns=self.dim_index_)
                       .iloc[:,axis].sum(axis=1).to_frame("cosinus").sort_values(by="cosinus",ascending=False)
                       .query(f"cosinus > {lim_cos2}"))
            if cos2.shape[0] != 0:
                coord = coord.loc[cos2.index,:]
    
    # Using lim contrib
    if lim_contrib is not None:
        if isinstance(lim_contrib,float):
            contrib = (pd.DataFrame(self.col_contrib_,index = self.col_labels_,columns=self.dim_index_)
                       .iloc[:,axis].sum(axis=1).to_frame("contrib").sort_values(by="contrib",ascending=False)
                       .query(f"contrib > {lim_contrib}"))
            if contrib.shape[0] != 0:
                coord = coord.loc[contrib.index,:]

    if color == "cos2":
        c = np.sum(self.col_cos2_[:,axis],axis=1)
        if legend_title is None:
            legend_title = "cos2"
    elif color == "contrib":
        c = np.sum(self.col_contrib_[:,axis],axis=1)
        if legend_title is None:
            legend_title = "Contrib"
    elif isinstance(color,np.ndarray):
        c = np.asarray(color)
        if legend_title is None:
            legend_title = "Cont_Var"
    
    # Initialize
    fig = go.Figure()
    
    if color in ["cos2","contrib"] or isinstance(color,np.ndarray):
        # Add gradients colors
        coord[legend_title] = c
        for i, name in enumerate(coord.index):
            fig = fig.add_trace(go.Scatter(x=[0,coord.iloc[i,axis[0]]], y=[0,coord.iloc[i,axis[1]]],
                                           name=name,
                                           line=dict(
                                               color=get_color_for_val(coord.iloc[i,-1],coord.iloc[:,-1].min(),coord.iloc[:,-1].max(),px.colors.sequential.RdBu)
                                            ),
                                            showlegend=False,
                                            marker= dict(
                                                size=10,
                                                symbol= "arrow-bar-up",
                                                angleref="previous",
                                                color=get_color_for_val(coord.iloc[i,-1],coord.iloc[:,-1].min(),coord.iloc[:,-1].max(), px.colors.sequential.RdBu),
                                                colorscale="RdBu",
                                                showscale=True
                                            )
                                            )
                                )
            # Add Text - Annotation
            if add_labels:
                # https://plotly.com/python/reference/layout/annotations/
                fig = fig.add_annotation(x=coord.iloc[i,axis[0]], y=coord.iloc[i,axis[1]],text=name,showarrow=False,yshift=10,valign=va,
                                            font=dict(size=text_size,
                                                    color=get_color_for_val(coord.iloc[i,-1],coord.iloc[:,-1].min(),coord.iloc[:,-1].max(),px.colors.sequential.RdBu)),
                                            align="center")
    elif hasattr(color, "labels_"):
        c = [str(x+1) for x in color.labels_]
        if legend_title is None:
            legend_title = "Cluster"
        coord[legend_title] = c
        for i, name in enumerate(coord.index):
            fig = fig.add_trace(go.Scatter(x=[0,coord.iloc[i,axis[0]]], y=[0,coord.iloc[i,axis[1]]],
                                           marker= dict(size=10,symbol= "arrow-bar-up", angleref="previous"),
                                           line=dict(color=color)))
    else:
        for i, name in enumerate(coord.index):
            fig = fig.add_trace(go.Scatter(x=[0,coord.iloc[i,axis[0]]], y=[0,coord.iloc[i,axis[1]]],
                                           name=name,
                                           marker= dict(size=text_size,symbol= "arrow-bar-up", angleref="previous"),
                                           line=dict(color=color)))
            if add_labels:
                # https://plotly.com/python/reference/layout/annotations/
                fig = fig.add_annotation(x=coord.iloc[i,axis[0]], y=coord.iloc[i,axis[1]],
                                         text=name,showarrow=False,yshift=10,valign=va,
                                         font=dict(color=color,size=text_size))
        # Remove legend
        fig.update_layout(showlegend=False)
    
    # Add supplementary continuous variables
    if quanti_sup:
        if self.quanti_sup_labels_ is not None:
            sup_coord = pd.DataFrame(self.col_sup_coord_,columns=self.dim_index_,index=self.col_sup_labels_)
            for i, name in enumerate(sup_coord.index):
                fig = fig.add_trace(go.Scatter(x=[0,sup_coord.iloc[i,axis[0]]], y=[0,sup_coord.iloc[i,axis[1]]],name=name,
                                               showlegend=False,
                                                marker= dict(size=text_size,symbol= "arrow-bar-up", angleref="previous"),
                                                line=dict(color=color_sup,dash=linestyle_sup)))

                if add_labels:
                    fig = fig.add_annotation(x=sup_coord.iloc[i,axis[0]], y=sup_coord.iloc[i,axis[1]],
                                             text=name,showarrow=False,yshift=10,valign=va,
                                            font=dict(color=color_sup,size=text_size))
        
    # Create circle
    if add_circle:
        fig.add_shape(type="circle",xref="x", yref="y",x0=-1, y0=-1, x1=1, y1=1,line_color="black")
    
    # Add additionnal        
    proportion = self.eig_[2]
    xlabel = "Dim."+str(axis[0]+1)+" ("+str(round(proportion[axis[0]],2))+"%)"
    ylabel = "Dim."+str(axis[1]+1)+" ("+str(round(proportion[axis[1]],2))+"%)"

    if title is None:
        title = "Variables factor map - PCA"
    # Set xlim
    fig.update_xaxes(range=[-1.1,1.1])
    # Set ylim
    fig.update_yaxes(range=[-1.1,1.1])
    # Add horizontal line
    if add_hline:
        fig.add_hline(y=0.0,line_width=1,line_dash=hline_style,line_color=hline_color)
     # Add Vertical Line
    if add_vline:
        fig.add_vline(x=0.0, line_width=1,line_dash=vline_style,line_color=vline_color) 
    # Update layout
    fig.update_layout(
        xaxis_title=xlabel,
        yaxis_title=ylabel,
        template="simple_white",
        margin=dict(autoexpand=True, l=0, t=0, r=0, b=0),
        height=450,
        #width=450,
        font=dict(family="serif", size=14),
        legend=dict(orientation="v", x=0, y=0, bgcolor="rgba(0,0,0,0)")
        )
    return fig

# Screeplot 
def plotly_screeplot(self,
                     choice="proportion",
                     color="navy"):
    
    eig = get_eigenvalue(self)
    if choice == "eigenvalue":
        eig = eig["eigenvalue"]
        text_labels = list([str(np.around(x,3)) for x in eig.values])
        ylabel = "Eigenvalue"
    elif choice == "proportion":
        eig = eig["proportion"]
        text_labels = list([str(np.around(x,1))+"%" for x in eig.values])
        ylabel = "Percentage of explained variance"

    df_eig = pd.DataFrame({"dim" : pd.Categorical(np.arange(1,len(eig)+1)),"eig" : eig.values})
    fig = px.bar(df_eig, x="dim", y='eig',title="Scree plot")
    # Add lines
    fig.add_trace(go.Scatter(x=df_eig["dim"], y=df_eig["eig"],line=dict(color="black")))
    # Add labels
    for i , name in enumerate(text_labels):
            fig = fig.add_annotation(x=df_eig.iloc[i,0], y=df_eig.iloc[i,1],text=name,font=dict(color="black"))
    # Update axis labels
    fig.update_layout(
        xaxis_title="Dimensions",
        yaxis_title=ylabel,
        template="simple_white",
        margin=dict(autoexpand=True, l=0, t=0, r=0, b=0),
        height=450,
        font=dict(family="serif", size=14),
        legend=dict(orientation="v", x=0, y=0, bgcolor="rgba(0,0,0,0)"),
        showlegend=False
        )
    # Update color
    fig.update_traces(marker_color=color)
    return fig

# Contributions plot
def plotly_contrib(self,
                 choice="ind",
                 axis=None,
                 xlabel=None,
                 top_contrib=10,
                 bar_width=None,
                 color="steelblue",
                 short_labels=False):
    
    if choice not in ["ind","var","mod"]:
        raise ValueError("Error : 'choice' not allowed.")

    if axis is None:
        axis = 0
    elif not isinstance(axis,int):
        raise ValueError("Error : 'axis' must be an integer.")
    elif axis < 0 or axis > self.n_components_:
        raise ValueError(f"Error : 'axis' must be an integer between 0 and {self.n_components_ - 1}.")
            
    if xlabel is None:
        xlabel = "Contributions (%)"
            
    if bar_width is None:
        bar_width = 0.5
    if top_contrib is None:
        top_contrib = 10
    elif not isinstance(top_contrib,int):
        raise ValueError("Error : 'top_contrib' must be an integer.")
        
    if choice == "ind":
        name = "individuals"
        contrib = self.row_contrib_[:,axis]
        labels = self.row_labels_
        if self.model_ == "ca":
            name = "rows"
    elif choice == "var":
        if self.model_ != "mca":
            name = "continues variables"
            contrib = self.col_contrib_[:,axis]
            labels  = self.col_labels_
            if self.model_ == "ca":
                name = "columns"
            if self.model_ == "famd":
                contrib = np.append(contrib,self.var_contrib_[:,axis],axis=0)
                labels = labels + self.quali_labels_
        else:
            name = "Categorical variables"
            contrib = self.var_contrib_[:,axis]
            labels = self.var_labels_     
    elif choice == "mod" and self.model_ in ["mca","famd"]:
        name = "categories"
        contrib = self.mod_contrib_[:,axis]
        if short_labels:
            labels = self.short_labels_
        else:
            labels = self.mod_labels_
    
    n = len(labels)
    n_labels = len(labels)
        
    if (top_contrib is not None) & (top_contrib < n_labels):
        n_labels = top_contrib
        
    limit = n - n_labels
    contrib_sorted = np.sort(contrib)[limit:n]
    labels_sort = pd.Series(labels)[np.argsort(contrib)][limit:n]

    # Add hline
    if self.model_ == "pca":
        hvalue = 100/len(self.col_labels_)
    elif self.model_ == "ca":
        hvalue = 100/(min(len(self.row_labels_)-1,len(self.col_labels_)-1))
    elif self.model_ == "mca":
        hvalue = 100/len(self.mod_labels_)
    elif self.model_ == "famd":
        hvalue = 100/(len(self.quanti_labels_) + len(self.mod_labels_) - len(self.quali_labels_))

    df = pd.DataFrame({"labels" : labels_sort, "contrib" : contrib_sorted})
    df = df.sort_values(by="contrib",ascending=False)

    fig = go.Figure()
    # Add 
    fig.add_trace(
        go.Bar(
            x = df["labels"],
            y=df["contrib"],
            width=[bar_width]*len(contrib_sorted),
            marker_color=color
        )
    )
    fig.update_layout(
        xaxis_title=name,
        yaxis_title=f"Contributions (%) of {name} to Dim-{axis+1}",
        template="simple_white",
        margin=dict(autoexpand=True, l=0, t=0, r=0, b=0),
        height=450,
        font=dict(family="serif", size=14),
        legend=dict(orientation="v", x=0, y=0, bgcolor="rgba(0,0,0,0)"),
        showlegend=False
        )
    # Add hline
    fig.add_hline(y=hvalue,line_width=1, line_dash="dash", line_color="red")
    return fig


# Cos2 plot
def plotly_cosines(self,
                 choice="ind",
                 axis=None,
                 xlabel=None,
                 top_cos2=10,
                 bar_width=None,
                 color="steelblue",
                 short_labels=False):
    if choice not in ["ind","var","mod","quanti_sup","quali_sup","ind_sup"]:
        raise ValueError("Error : 'choice' not allowed.")
    
    if axis is None:
        axis = 0
    elif not isinstance(axis,int):
        raise ValueError("Error : 'axis' must be an integer.")
    elif axis < 0 or axis > self.n_components_:
        raise ValueError(f"Error : 'axis' must be an integer between 0 and {self.n_components_ - 1}")

    if xlabel is None:
        xlabel = "Cos2 - Quality of representation"
    if bar_width is None:
        bar_width = 0.5
    if top_cos2 is None:
        top_cos2 = 10
        
    if choice == "ind":
        name = "individuals"
        if self.model_ == "ca":
            name = "rows"
        cos2 = self.row_cos2_[:,axis]
        labels = self.row_labels_
    elif choice == "var" :
        if self.model_ != "mca":
            name = "continues variables"
            cos2 = self.col_cos2_[:,axis]
            labels  = self.col_labels_
            if self.model_ == "ca":
                name = "columns"
        else:
            name = "categorical variables"
            cos2 = self.var_cos2_[:,axis]
            labels  = self.var_labels_
    elif choice == "mod" and self.model_ in ["mca","famd"]:
        name = "categories"
        cos2 = self.mod_cos2_[:,axis]
        if short_labels:
            labels = self.short_labels_
        else:
            labels = self.mod_labels_
    elif choice == "quanti_sup" and self.model_ != "ca":
        if ((self.quanti_sup_labels_ is not None) and (len(self.col_sup_labels_) >= 2)):
            name = "supplementary continues variables"
            cos2 = self.col_sup_cos2_[:,axis]
            labels = self.col_sup_labels_
        else:
            raise ValueError("Error : Factor Model must have at least two supplementary continuous variables.")
    elif choice == "quali_sup" and self.model_ !="ca":
        if self.quali_sup_labels_ is not None:
            name = "supplementary categories"
            cos2 = self.mod_sup_cos2_[:,axis]
            if short_labels:
                labels = self.short_sup_labels_
            else:
                labels = self.mod_sup_labels_
    
    # Start
    n = len(labels)
    n_labels = len(labels)
    if (top_cos2 is not None) & (top_cos2 < n_labels):
        n_labels = top_cos2
        
    limit = n - n_labels
    cos2_sorted = np.sort(cos2)[limit:n]
    labels_sort = pd.Series(labels)[np.argsort(cos2)][limit:n]

    df = pd.DataFrame({"labels" : labels_sort, "cos2" : cos2_sorted})

    df = df.sort_values(by="cos2",ascending=False)

    fig = go.Figure()
    # Add 
    fig.add_trace(
        go.Bar(
            x = df["labels"],
            y=df["cos2"],
            width=[bar_width]*len(cos2_sorted),
            marker_color=color
        )
    )
    fig.update_layout(
        xaxis_title=name,
        yaxis_title=f"Cosinus of {name} to Dim-{axis+1}",
        template="simple_white",
        margin=dict(autoexpand=True, l=0, t=0, r=0, b=0),
        height=450,
        font=dict(family="serif", size=14),
        legend=dict(orientation="v", x=0, y=0, bgcolor="rgba(0,0,0,0)"),
        showlegend=False
        )
    return fig

################################# Panel

# Match with data
def match_datalength(data,value):
    match value:
        case "head":
            return data.head(6)
        case "tail":
            return data.tail(6)
        case "all":
            return data

# Return table
def DataTable(data):
    return dash_table.DataTable(
        data=data.to_dict("records"),
        columns=[{"name": i, "id": i,} for i in data.columns],
        style_as_list_view=False,
        style_header={'backgroundColor': '#657E95','fontWeight': 'bold','color': 'white'},
        style_data={'color': 'white','backgroundColor': '#3B4D5E'},
        style_cell_conditional=[{'if': {'column_id': c},'textAlign': "center"} for c in data.columns[1:]],
        #editable=True,
        #filter_action="native",
        sort_action="native",
        sort_mode="multi",
        column_selectable="single",
        row_deletable=False,
        selected_columns=[],
        selected_rows=[],
        page_action="native",
        page_current= 0,
        page_size= 10
    )

# Panel Conditional 1 - Without Graph
def PanelConditional1(text=str,name=str):
    panel = dbc.Row(
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
                                    [dmc.Chip(x, value=x) for x in ["head","tail","all"]],
                                    value="head",
                                    multiple=False,
                                    id="pca-"+text+"-"+name+"-value"
                                )

                                ]
                            )
                        ]
                    )
                ],
                sm=3
            ),
            # https://dash.plotly.com/datatable
            dbc.Col(
                children=[
                    html.Div(id="pca-"+text+"-"+name+"-output")
                ],
                sm=9
            )
        ]
    )
    return panel

# Modal Header for Contribution
def GraphModalShow(text=str,name=str):
    modal = dbc.Modal(
                children=[
                    dbc.ModalBody(
                        children=[
                            html.Div(
                                children=[
                                    dbc.Row(
                                        children=[
                                            dbc.Col(
                                                children=[
                                                    dbc.Card(
                                                        children=[
                                                            html.H6("Axis"),
                                                            dcc.Input(
                                                                id="pca-"+text+"-"+name+"-axis-value",
                                                                type="number",
                                                                placeholder="Choisir un axe",
                                                                min=0,
                                                                max=2,
                                                                value=0
                                                            )
                                                        ],
                                                        body=True,
                                                        className="controls_team"
                                                    )
                                                ],
                                                width=3
                                            ),
                                            dbc.Col(
                                                children=[
                                                    dbc.Card(
                                                        children=[
                                                            html.H6("Top "+name),
                                                            dcc.Input(
                                                                id="pca-"+text+"-"+name+"-top-value",
                                                                type="text",
                                                                value=10,
                                                                placeholder="Entrer un nombre"
                                                            )
                                                        ],
                                                        body=True,
                                                        className="controls_team"
                                                    )
                                                ],
                                                width=3
                                            ),
                                            dbc.Col(
                                                children=[
                                                    dbc.Card(
                                                        children=[
                                                            html.H6("fill color"),
                                                            dcc.Dropdown(
                                                                id="pca-"+text+"-"+name+"-color-value",
                                                                options=[
                                                                    {"label" : x, "value" : x} for x in mcolors.CSS4_COLORS
                                                                ],
                                                                value="navy",
                                                                multi=False
                                                            )
                                                        ],
                                                        body=True,
                                                        className="controls_team"
                                                    )
                                                ],
                                                width=2
                                            ),
                                            dbc.Col(
                                                children=[
                                                    dbc.Card(
                                                        children=[
                                                            html.H6("Bar width"),
                                                            dcc.Slider(
                                                                id="pca-"+text+"-"+name+"-barwidth-value",
                                                                min=0.1,
                                                                max=1,
                                                                value=0.5,
                                                                step=0.1,
                                                                marks={0.1:"0.1",0.2:"0.2",0.3:"0.3",0.4:"0.4",0.5:"0.5",0.6:"0.6",0.7:"07",0.8:"0.8",0.9:"0.9",1:"1"}
                                                            )
                                                        ],
                                                        body=True,
                                                        className="controls_team"
                                                    )
                                                ],
                                                width=4
                                            )
                                        ]
                                    )
                                ]
                            ),
                            html.Div(
                                children=[
                                    dbc.Row(
                                        children=[
                                            dcc.Loading(dcc.Graph(id="pca-"+text+"-"+name+"-graph-output",config=dict(displayModeBar=False),responsive=True))
                                        ]
                                    )
                                ]
                            )
                        ]
                    ),
                    dbc.ModalFooter(
                        children=[
                            dbc.Button("Close", id="pca-"+text+"-"+name+"-close-btn", className="ms-auto", n_clicks=0)
                        ]
                    )
                ],
                id="pca-"+text+"-"+name+"-graph-modal",
                size="xl",
                is_open=False,
            )
    return modal

def PanelConditional2(text=str,name=str):
    # Set value name
    if name == "contrib":
        value_name = "Contribution"
    elif name == "cos2":
        value_name = "Cosinus"
    elif name == "corr":
        value_name = "Correlation"
    elif name == "vtest":
        value_name = "Vtest"
    
    panel = dbc.Row(
        children=[
            dbc.Col(
                children=[
                    dbc.Row(html.H6("Paramètres")),
                    html.P(),
                    dbc.Row(
                        children=[
                            html.Div(
                                className="selection d-flex justify-content-center mb-3",
                                children=[
                                    dmc.ChipGroup(
                                        [dmc.Chip(x,value=x) for x in ["head","tail","all"]],
                                        value="head",
                                        multiple=False,
                                        id="pca-"+text+"-"+name+"-value",
                                    )
                                ]
                            )
                        ]
                    ),
                    html.P(),
                    dbc.Row(
                        children=[
                            html.Div(
                                children=[
                                    dbc.Button(
                                        html.H6("Graphe "+value_name), 
                                        color="light", 
                                        outline=True,
                                        className="me-1",
                                        id="pca-"+text+"-"+name+"-graph-btn",
                                        n_clicks=0
                                    ),
                                    GraphModalShow(text,name)
                                ],
                                className="d-grid gap-2 col-6 mx-auto",
                            )
                        ]
                    )
                ],
                sm=3
            ),
            dbc.Col(
                children=[
                    html.Div(id="pca-"+text+"-"+name+"-output")
                ],
                sm=9
            )
        ]
    )
    return panel

def OverallPanelConditional(text):
    panel = html.Div(
        children=[
            html.P(),
            html.H5("Coordinates"),
            PanelConditional1(text=text,name="coord"),
            html.Hr(),
            html.H5("Contributions"),
            PanelConditional2(text=text,name="contrib"),
            html.Hr(),
            html.H5("Cos2 - Quality of representation"),
            PanelConditional2(text=text,name="cos2")

        ],
        id="pca-"+text+"res"
    )
    return panel
