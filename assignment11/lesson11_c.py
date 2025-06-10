# Dash components you need
from dash import Dash, dcc, html, Input, Output

# Dash relies on Plotly to actually do the plotting.  Plotly creates an HTML page with lots of JavaScript.
import plotly.express as px

# This is only needed to give access to the Plotly built in datasets.
import plotly.data as pldata

# This loads one of the datasets
df = pldata.stocks(return_type='pandas', indexed=False, datetimes=True)


# Initialize Dash app
# This creates the app object, to wich various things are added below.
# __name__ is the name of the running Python module, which is your main module in this case
app = Dash(__name__)

# Layout: This section creates the HTML components
app.layout = html.Div([                     # This div is for the dropdown you see at the top, and also for the graph itself
    dcc.Dropdown(                           # This creates the dropdown
        id="stock-dropdown",
                                            # This populates the dropdown with the list of stocks
        options=[{"label": symbol, "value": symbol} for symbol in df.columns],
        value="GOOG"                        # This is the initial value
    ),

    dcc.Graph(id="stock-price")     # And the graph itself has to have an ID
])

# Callback for dynamic updates


@app.callback(
    # this is a decorator.  This decorator is decorating the update_graph() function.
    # Because of the decorator, the update_graph() will be called when the stock-dropdown changes,
    # passing the value selected in the dropdown.
    Output("stock-price", "figure"),
    [Input("stock-dropdown", "value")]
)
def update_graph(symbol):  # This function is what actually does the plot,
    # by calling Plotly, in this case a line chart of date (which is the index) vs. the chosen stock price.
    fig = px.line(df, x="date", y=symbol, title=f"{symbol} Price")
    return fig


# Run the app
# if this is the main module of the program, and not something included by a different module
if __name__ == "__main__":
    # start the Flask web server
    app.run(debug=True)
