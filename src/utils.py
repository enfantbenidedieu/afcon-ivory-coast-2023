update_layout = dict(
    height=60,
    hovermode="x",
    template="plotly_dark",
    margin=dict(autoexpand=True, l=0, r=0, b=0, t=0),
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=dict(
        showline=True,
        linecolor='white',
        showticklabels=False,
        gridcolor="rgba(79, 79, 79, 0.113)",
        showgrid=True
    ),
    yaxis=dict(
        showticklabels=False,
        showline=False,
        showgrid=False
    ),
    hoverlabel=dict(
        bgcolor="white",
        bordercolor="rgba(0,0,0,0)",
        font=dict(
                color="black",
                size=11,
                family="serif"
        )
    )
)