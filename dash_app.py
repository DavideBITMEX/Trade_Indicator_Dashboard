import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
import sqlite3

# Step 1: Connect to SQLite and Fetch Data
db_file = "trade_data.db"
conn = sqlite3.connect(db_file)
df = pd.read_sql("SELECT * FROM trade_indicators", conn)
conn.close()

# Step 2: Initialize Dash App
app = dash.Dash(__name__)

# Step 3: Layout with Dropdown and Two Charts
app.layout = html.Div([
    html.H1("Trade Indicators Dashboard"),
    html.Label("Select Year:"),
    dcc.Dropdown(
        id='year-dropdown',
        options=[{'label': year, 'value': year} for year in sorted(df['date'].unique())],
        value=sorted(df['date'].unique())[0]
    ),
    dcc.Graph(id='line-chart'),
    dcc.Graph(id='bar-chart')
])

# Step 4: Callbacks for Interactivity
@app.callback(
    [dash.dependencies.Output('line-chart', 'figure'),
     dash.dependencies.Output('bar-chart', 'figure')],
    [dash.dependencies.Input('year-dropdown', 'value')]
)
def update_charts(selected_year):
    # Filter the DataFrame based on the selected year
    filtered_df = df[df['date'] == selected_year]

    # Line Chart
    line_fig = px.line(filtered_df, x="date", y="value", title="Yearly Export Growth")

    # Bar Chart
    bar_fig = px.bar(filtered_df, x="date", y="value", title="Export Growth Comparison")

    return line_fig, bar_fig

# Step 5: Run the Dash App
if __name__ == "__main__":
    app.run_server(debug=True, host="0.0.0.0", port=8050)
