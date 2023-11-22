import plotly.graph_objects as go

# Create the figure
fig = go.Figure()

# Add the x-axis
fig.add_trace(go.Scatter3d(
    x=[0, 1],
    y=[0, 0],
    z=[0, 0],
    mode='lines',
    name='x-axis',
    line=dict(color='red', width=3)
))

# Add the y-axis
fig.add_trace(go.Scatter3d(
    x=[0, 0],
    y=[0, 1],
    z=[0, 0],
    mode='lines',
    name='y-axis',
    line=dict(color='green', width=3)
))

# Add the z-axis
fig.add_trace(go.Scatter3d(
    x=[0, 0],
    y=[0, 0],
    z=[0, 1],
    mode='lines',
    name='z-axis',
    line=dict(color='blue', width=3)
))

# Set the layout
fig.update_layout(
    scene=dict(
        xaxis=dict(title='X'),
        yaxis=dict(title='Y'),
        zaxis=dict(title='Z')
    )
)

# Show the plot
fig.show()
