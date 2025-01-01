# UN Project: Data Pipeline and Dashboard

## Overview
This project demonstrates an end-to-end data pipeline and dashboard designed for the Associate Data Engineer role at the UN. The pipeline:
- Fetches trade indicator data from the World Bank API.
- Cleans and stores the data in a SQLite database.
- Visualizes the data using a Dash dashboard.

## Project Structure
- `data_pipeline.py`: Fetches, cleans, and stores the data in SQLite.
- `dash_app.py`: Dash application to visualize the data.
- `Dockerfile`: Instructions to containerize the project.
- `requirements.txt`: Python dependencies.

## Steps to Run the Project

### Local Environment
1. Install Python 3.9+ and the required dependencies:
   ```bash
   pip install -r requirements.txt
