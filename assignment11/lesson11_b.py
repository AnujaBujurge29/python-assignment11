import plotly.express as px
import plotly.data as pldata

# Load built-in iris dataset
df = pldata.iris(return_type='pandas')

# Create scatter plot
fig = px.scatter(
    df,
    x='sepal_length',
    y='petal_length',
    color='species',
    title="Iris Data, Sepal vs. Petal Length",
    hover_data=["petal_length"]
)

# Save and auto-open the plot as an HTML file
fig.write_html("iris.html", auto_open=True)

# Note: Avoid using fig.show() — it often hangs in some environments.
