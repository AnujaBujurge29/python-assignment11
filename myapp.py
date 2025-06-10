# Dash components you need
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import plotly.data as pldata

# Initialize Dash app
app = Dash(__name__)
server = app.server
# 4.1 loads the datasets
df = px.data.gapminder()

# 4.2 Get unique countries and sort them
countries = sorted(df['country'].unique())

# 4.3 Layout: Create the HTML components
app.layout = html.Div([
    html.H1('GDP Per Capita By Country',
            style={'textAlign': 'center', 'marginBottom': 30}),

    dcc.Dropdown(
        id="country-dropdown",
        options=[{"label": country, "value": country}
                 for country in countries],
        value="Canada",  # Set initial value to Canada
        style={'width': '50%', 'margin': 'auto'}
    ),

    dcc.Graph(id="gdp-growth")
])

# 4.4 Callback for dynamic updates


@app.callback(
    Output("gdp-growth", "figure"),
    [Input("country-dropdown", "value")]
)
def update_graph(country):
    # Filter data for selected country
    filtered_df = df[df['country'] == country]

    # Create line plot
    fig = px.line(
        filtered_df,
        x="year",
        y="gdpPercap",
        title=f"GDP Per Capita Over Time - {country}",
        labels={
            'year': 'Year',
            'gdpPercap': 'GDP Per Capita ($)'
        }
    )

    # 4.5 Update layout for better appearance
    fig.update_layout(
        title_x=0.5,
        plot_bgcolor='white',
        paper_bgcolor='white'
    )

    return fig


# Run the app
if __name__ == "__main__":
    app.run(debug=True)
