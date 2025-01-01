# 🇪🇺 Trade Indicators: Data Pipeline and Dashboard

### Key Features
- **Data Ingestion:** Fetches trade indicator data dynamically from the World Bank API for all countries.
- **Data Transformation:** Cleans and processes raw data into an analysis-ready format.
- **Data Storage:** Utilizes a SQLite database for lightweight and efficient data storage.
- **Data Visualization:** Provides an interactive dashboard using Python's Dash framework, featuring:
  - Time-series visualizations of trade data trends.
  - Geospatial mapping of trade indicators.
  - Top 10 country rankings based on export growth.

## Technologies Used
### **Programming and Frameworks:**
- **Python 3.9+**: Core language for data processing, visualization, and API interactions.
- **Dash**: Framework for building the interactive dashboard.
- **Pandas**: Data manipulation and transformation.
- **Geopandas**: Handling geospatial data for mapping.
- **Folium**: Creating dynamic and interactive maps.
- **Plotly**: Generating interactive visualizations.

### **Data Storage:**
- **SQLite**: Lightweight relational database used for storing cleaned trade indicator data.

### **DevOps and Deployment:**
- **Docker**: Containerized the application for consistent and reproducible environments.
- **Render**: Cloud hosting service used for deploying the dashboard, ensuring global accessibility.

### **Version Control:**
- **Git**: For versioning and collaborative development.
- **GitHub**: Repository hosting for project code and documentation.

---

## Project Structure
```plaintext
.
├── data_pipeline.py         # Script for fetching, cleaning, and storing data in SQLite
├── highcharter_dashboard.py # Dash application for data visualization
├── Dockerfile               # Containerization instructions for the project
├── requirements.txt         # List of Python dependencies
├── data/                    # Folder containing geospatial shapefiles for mapping
├── trade_data.db            # SQLite database storing processed trade indicator data
├── README.md                # Project overview and setup instructions
├── Setup_Instructions.md    # Detailed instructions for setting up and running the project

