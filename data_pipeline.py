import requests
import pandas as pd
import sqlite3
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def fetch_data_for_all_countries(indicator="NE.EXP.GNFS.KD.ZG"):
    """Fetch data for all countries from the World Bank API."""
    base_url = f"https://api.worldbank.org/v2/country/all/indicator/{indicator}?format=json&per_page=10000"
    try:
        logging.info("Fetching data for all countries from World Bank API...")
        response = requests.get(base_url)
        response.raise_for_status()
        data_json = response.json()
        return data_json[1]  # The second element holds the actual data
    except Exception as e:
        logging.error(f"Failed to fetch data: {e}")
        raise

def clean_data(data_list):
    """Clean and transform the data."""
    try:
        logging.info("Cleaning data...")
        df = pd.DataFrame(data_list)
        df = df[['countryiso3code', 'country', 'date', 'value']]  # Keep relevant columns

        # Extract the name of the country if it's a dictionary
        if isinstance(df['country'].iloc[0], dict):
            df['country'] = df['country'].apply(lambda x: x.get('value', '') if isinstance(x, dict) else x)

        df.dropna(subset=['value'], inplace=True)  # Remove rows with missing values
        df['value'] = df['value'].astype(float)    # Ensure numeric type
        return df
    except Exception as e:
        logging.error(f"Data cleaning failed: {e}")
        raise



def save_to_database(df):
    """Save the data to SQLite and add metadata."""
    try:
        logging.info("Saving data to SQLite database...")
        conn = sqlite3.connect("trade_data.db")
        df.to_sql("trade_indicators", conn, if_exists="replace", index=False)

        # Add metadata
        metadata = pd.DataFrame([{'ingestion_time': datetime.now()}])
        metadata.to_sql("metadata", conn, if_exists="replace", index=False)
        conn.close()
        logging.info("Data successfully saved to database.")
    except Exception as e:
        logging.error(f"Database operation failed: {e}")
        raise

if __name__ == "__main__":
    data_list = fetch_data_for_all_countries()
    df = clean_data(data_list)
    save_to_database(df)
    logging.info("Pipeline executed successfully.")
