import plotly.express as px
import plotly.data as pldata
import pandas as pd

# Load the wind dataset
df = pldata.wind(return_type='pandas')

# 3.1 Print first and last 10 lines
print('-----------------------------------------------------------------')
print("First 10 rows:")
print(df.head(10))
print('-----------------------------------------------------------------')
print("Last 10 rows:")
print(df.tail(10))

# 3.2 Clean the data - convert strength column to float


def convert_strength(value):
    # Remove 'mph' suffix first
    value = value.replace(' mph', '')

    # Handle case with '+' (e.g., "25+")
    if '+' in value:
        base = float(value.replace('+', ''))
        return base + 0.5

    # Handle range case with '-' (e.g., "0-1")
    elif '-' in value:
        low, high = map(float, value.split('-'))
        return (low + high) / 2

    # Handle simple numeric case
    return float(value)


# Apply the conversion function
df['strength'] = df['strength'].apply(convert_strength)
df["strength"] = df["strength"].astype("float")
# 3.3 Create interactive scatter plot
fig = px.scatter(
    df,
    x='strength',
    y='frequency',
    color='direction',
    title='Wind Strength vs Frequency by Direction',
    labels={
        'strength': 'Wind Strength (mph)',
        'frequency': 'Frequency',
        'direction': 'Wind Direction'
    }
)

# Update layout
fig.update_layout(
    title_x=0.5,
    plot_bgcolor='white',
    legend_title_text='Wind Direction'
)

# Add grid
fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')
fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')

# 3.4 Save the plot as HTML
fig.write_html('wind.html')

# Show the plot
fig.show()
