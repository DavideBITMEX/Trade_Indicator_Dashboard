# Project Setup and Execution Instructions

This document provides detailed instructions to set up and run the project, including the creation and activation of a virtual environment, installing necessary dependencies, and running the Dash app.

---

## **Initial Setup**

1. **Clone the Project Folder**  
   Navigate to your desired directory and clone or create the project folder:
   ```bash
   mkdir UN_proj
   cd UN_proj
   ```

2. **Create a Virtual Environment**  
   Run the following command to create a virtual environment:
   ```bash
   python3 -m venv venv
   ```

3. **Activate the Virtual Environment**  
   - **macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```
   - **Windows**:
     ```bash
     venv\Scripts\activate
     ```
            **Installing geopandas**
            /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

            echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
            eval "$(/opt/homebrew/bin/brew shellenv)"

            brew install proj gdal

            pip install geopandas
            pip install folium
            pip install dash-extensions




            

4. **Install Required Dependencies**  
   After activating the virtual environment, install the necessary packages:
   ```bash
   pip install pandas requests plotly dash
   ```

5. **Verify Installation**  
   Test the installation by importing the libraries in Python:
   ```bash
   python3
   ```
   Then, type:
   ```python
   import pandas
   import requests
   import plotly
   import dash
   ```
   Exit Python with:
   ```python
   exit()
   ```

---

## **Running the Data Pipeline**

1. Ensure you are in the `UN_proj` directory:
   ```bash
   cd /path/to/UN_proj
   ```

2. Run the data pipeline script to fetch, clean, and store the data in SQLite:
   ```bash
   python3 data_pipeline.py
   ```

3. Check the SQLite database (`trade_data.db`) for the processed data if needed:
   ```bash
   sqlite3 trade_data.db
   ```
   Run the following SQL commands to inspect the data:
   ```sql
   .tables
   SELECT * FROM trade_indicators LIMIT 5;
   .exit
   ```

---

## **Running the Dash App**

1. Run the Dash app:
   ```bash
   python3 highcharter_dashboard.py
   ```

2. Open your browser and navigate to:
   ```
   http://localhost:8050
   ```

3. If the terminal is blocked by the running app, you have the following options:

   ### Option 1: Use Another Terminal
   - Open a new terminal session.
   - Navigate to the project directory:
     ```bash
     cd /path/to/UN_proj
     ```

   ### Option 2: Run the App in the Background
   - **macOS/Linux**:
     ```bash
     python3 highcharter_dashboard.py &
     ```
   - **Windows**:
     ```bash
     start python highcharter_dashboard.py
     ```

   ### Option 3: Use a Terminal Multiplexer (Optional)
   For advanced users, use `tmux` or `screen` to manage multiple sessions.

---

## **Reactivating the Virtual Environment**

1. Navigate to the project directory:
   ```bash
   cd /path/to/UN_proj
   ```

2. Activate the virtual environment:
   - **macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```
   - **Windows**:
     ```bash
     venv\Scripts\activate
     ```

3. Ensure dependencies are installed (only needed once):
   ```bash
   pip install pandas requests sqlite3 plotly dash
   ```

---

## **Troubleshooting**

### Error: `ModuleNotFoundError: No module named 'pandas'`
Ensure the virtual environment is activated and `pandas` is installed:
```bash
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
pip install pandas
```

### Error: `Database operation failed`
Inspect the data pipeline script (`data_pipeline.py`) to ensure proper data cleaning before saving to SQLite.

---

## **Deactivating the Virtual Environment**
After completing your work, deactivate the virtual environment:
```bash
deactivate
```
Press Ctrl + C in the terminal where the dashboard is running to stop the current process.
---

## **Notes**
- The virtual environment isolates project dependencies, ensuring consistency.
- Run the data pipeline script (`data_pipeline.py`) whenever new data is required.
- Use the `highcharter_dashboard.py` script to launch the interactive dashboard.
