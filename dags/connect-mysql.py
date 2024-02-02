import requests
import pandas as pd
import mysql.connector
from sqlalchemy import create_engine
import logging

class GetApi():
    def __init__(self, url, mysql_config):
        self.url = url
        self.mysql_config = mysql_config

    def get_api_data(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()  # Raises HTTPError for bad responses
            result = response.json()['data']['content']
            logging.info('GET DATA FROM API COMPLETED')
            df = pd.json_normalize(result)
            logging.info('LOAD DATA TO DATAFRAME READY')
            return df
        except requests.exceptions.RequestException as e:
            logging.error(f"Error fetching data from API: {e}")
            return None

    def load_to_mysql(self, df, table_name):
        try:
            engine = create_engine(self.mysql_config)

            # Jika tabel belum ada, maka tabel akan dibuat
            df.to_sql(table_name, con=engine, index=False, if_exists='replace')

            logging.info('DATA LOADED TO MYSQL SUCCESSFULLY')
        except Exception as e:
            logging.error(f"Error loading data to MySQL: {e}")

if __name__ == "__main__":
 
    mysql_config = "mysql+mysqlconnector://root:prbKei29_@localhost:3306/staging_fpde16"


    api_url = 'http://103.150.197.96:5005/api/v1/rekapitulasi_v2/jabar/harian?level=kab'


    table_name = 'covid_jabar'  

    # Inisialisasi objek GetApi
    api_loader = GetApi(api_url, mysql_config)

    # Ambil data dari API
    api_data = api_loader.get_api_data()

    if api_data is not None:
        # Muat data ke MySQL
        api_loader.load_to_mysql(api_data, table_name)
