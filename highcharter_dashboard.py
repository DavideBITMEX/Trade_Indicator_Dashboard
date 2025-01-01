import dash
from dash import dcc, html
import pandas as pd
import sqlite3
import plotly.express as px
import geopandas as gpd
import folium

# Step 1: Connect to SQLite Database
conn = sqlite3.connect("trade_data.db")
df = pd.read_sql("SELECT * FROM trade_indicators", conn)
conn.close()

# Geospatial Data (Using a local file)
world = gpd.read_file("data/ne_110m_admin_0_countries.shp")
geo_df = world.merge(df, left_on="iso_a3", right_on="countryiso3code", how="left")

# Step 2: Initialize Dash App
app = dash.Dash(__name__)

# Step 3: Layout with Dropdowns, Charts, and Geospatial Map
app.layout = html.Div([
    html.H1("Trade Indicators Dashboard", style={"text-align": "center", "color": "#009EDB", "font-family": "Arial, sans-serif"}),

    html.P(
        "This dashboard provides an interactive view of trade indicators such as export growth over time, "
        "the top 10 countries by growth for a selected year, and a geospatial visualization of export data. "
        "Use the selectors below to customize the view.",
        style={"text-align": "center", "font-family": "Arial, sans-serif", "margin-bottom": "20px"}
    ),

    html.Div([
        html.Div([
            html.Label("Select Year:", style={"color": "#333", "font-family": "Arial, sans-serif"}),
            dcc.Dropdown(
                id='year-dropdown',
                options=[{'label': year, 'value': year} for year in sorted(df['date'].unique())],
                value='2023',
                style={"background-color": "#f9f9f9", "border": "1px solid #ccc", "font-family": "Arial, sans-serif"}
            )
        ], style={"width": "48%", "display": "inline-block", "padding": "10px"}),

        html.Div([
            html.Label("Select Country:", style={"color": "#333", "font-family": "Arial, sans-serif"}),
            dcc.Dropdown(
                id='country-dropdown',
                options=[{'label': country, 'value': country} for country in sorted(df['country'].unique())],
                value='European Union',
                style={"background-color": "#f9f9f9", "border": "1px solid #ccc", "font-family": "Arial, sans-serif"}
            )
        ], style={"width": "48%", "display": "inline-block", "padding": "10px"})
    ], style={"display": "flex", "justify-content": "space-between"}),

    html.Div([
        html.Div([
            dcc.Graph(id='ranking-chart', style={"height": "500px", "margin-bottom": "20px"}),  # Top 10 bar plot on top

            html.Div([
                html.H3("Geospatial Visualization of Trade Data", style={"text-align": "center", "color": "#009EDB", "font-family": "Arial, sans-serif"}),
                html.P(
                    "The map shows trade indicator data across countries. Each circle represents a country, "
                    "with the size and color indicating export growth rates. Hover over the circles for more details.",
                    style={"text-align": "center", "font-family": "Arial, sans-serif"}
                ),
                html.Iframe(id='map', srcDoc=None, width="100%", height="500", style={"border": "2px solid #ccc"})
            ])  # Map on the bottom
        ], style={"width": "48%", "display": "inline-block", "vertical-align": "top"}),

        html.Div([
            html.Div([
                dcc.Graph(id='line-chart', style={"height": "500px"})  # Time series plot in the upper half
            ], style={"height": "50%"}),

            html.Div([
    dcc.Markdown(
        """
        **Project Information:** This project was developed as a showcase of data visualization and interactive dashboards, 
        utilizing Python libraries such as Dash, Plotly, and Folium. Data is sourced from reliable public repositories like the World Bank API, 
        and integrated using SQLite for efficient querying.

        **Contact Information:** If you have any questions or would like to learn more, please reach out via email at 
        [davidebittellil@gmail.com](mailto:davidebittellil@gmail.com) or visit the
        [GitHub Repository](https://your-website.com) of the project.
        """,
        style={"padding": "10px", "font-family": "Arial, sans-serif", "color": "#333", "line-height": "1.6", "height": "500px"}
    )
], style={"height": "48%", "background-color": "#f9f9f9", "border": "1px solid #ccc", "padding": "10px"})
        ], style={"width": "48%", "display": "inline-block", "vertical-align": "top"})
    ], style={"display": "flex", "justify-content": "space-between"})
], style={"background-color": "#f4f4f4", "padding": "20px"})

# Step 4: Callbacks for Interactive Charts
@app.callback(
    dash.dependencies.Output('line-chart', 'figure'),
    [dash.dependencies.Input('country-dropdown', 'value')]
)
def update_line_chart(selected_country):
    filtered_df = df[df['country'] == selected_country].sort_values(by='date')  # Explicit sorting by date
    fig = px.line(
        filtered_df,
        x='date',
        y='value',
        title=f"Export Growth Over Time for {selected_country}",
        labels={'value': 'Growth Rate (%)', 'date': 'Year'},
        template="plotly_white"
    )
    fig.update_layout(
        title_font_color="#009EDB",
        font_family="Arial, sans-serif",
        xaxis=dict(
            tickangle=-45,  # Rotate x-axis labels by 45 degrees
            title=dict(text="Year", standoff=10)
        )
    )
    return fig

@app.callback(
    dash.dependencies.Output('ranking-chart', 'figure'),
    [dash.dependencies.Input('year-dropdown', 'value')]
)
def update_ranking_chart(selected_year):
    filtered_df = df[df['date'] == selected_year]
    sorted_df = filtered_df.sort_values('value', ascending=False).head(10)
    fig = px.bar(
        sorted_df,
        x='country',
        y='value',
        title=f"Top 10 Countries by Export Growth in {selected_year}",
        labels={'value': 'Growth Rate (%)', 'country': 'Country'},
        text='value',
        template="plotly_white"
    )
    fig.update_traces(texttemplate='%{text:.2f}', textposition='outside')
    fig.update_layout(
        title_font_color="#009EDB",
        font_family="Arial, sans-serif",
        margin=dict(l=100, r=100, t=50, b=50)
    )
    return fig

@app.callback(
    dash.dependencies.Output('map', 'srcDoc'),
    [dash.dependencies.Input('year-dropdown', 'value')]
)
def update_map(selected_year):
    year_data = geo_df[geo_df['date'] == selected_year]
    m = folium.Map(location=[10, 20], zoom_start=2)

    # Define a valid color scale
    from branca.colormap import LinearColormap
    valid_colors = ['#f7fbff', '#deebf7', '#c6dbef', '#9ecae1', '#6baed6', '#4292c6', '#2171b5', '#08519c', '#08306b']
    colormap = LinearColormap(colors=valid_colors, vmin=year_data['value'].min(), vmax=year_data['value'].max())

    for _, row in year_data.iterrows():
        if not pd.isnull(row['value']) and row['geometry'] is not None:
            folium.CircleMarker(
                location=[row['geometry'].centroid.y, row['geometry'].centroid.x],
                radius=max(3, row['value'] / 5),  # Size proportional to value
                color=colormap(row['value']),  # Use the colormap for dynamic coloring
                fill=True,
                fill_opacity=0.7,
                popup=f"{row['country']}: {row['value']:.2f}"
            ).add_to(m)

    # Add the legend for the colormap
    colormap.caption = "Export Growth Rate"
    colormap.add_to(m)

    return m._repr_html_()

# Step 5: Run Server
if __name__ == "__main__":
    app.run_server(debug=True, host="0.0.0.0", port=8050)
