import requests
import pandas as pd
import logging

""" class GetApi():
    def __init__(self, url):
        self.url = 'http://103.150.197.96:5005/api/v1/rekapitulasi_v2/jabar/harian?level=kab'

    def get_api_data(self):
        try:
            response = requests.get(self.url)
            
            if response.status_code == 200:
                result = response.json()['data']['content']
                logging.info('GET DATA FROM API COMPLETED')
                df = pd.json_normalize(result)
                logging.info('LOAD DATA TO DATAFRAME READY')
                return df
            else:
                logging.error(f"Failed to retrieve data. Status code: {response.status_code}")
                return None

        except Exception as e:
            logging.error(f"An error occurred: {str(e)}")
            return None

# Contoh penggunaan
if __name__ == "__main__":
    # Mengatur opsi pandas untuk menampilkan seluruh baris dan kolom
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)

    api_data = GetApi(url='http://103.150.197.96:5005/api/v1/rekapitulasi_v2/jabar/harian?level=kab')
    df_result = api_data.get_api_data()

    # Lakukan sesuatu dengan df_result, seperti menampilkannya atau menyimpannya ke file
    if df_result is not None:
        print("Data from API:")
        print(df_result)

        # Menyimpan DataFrame ke file CSV
        ##df_result.to_csv('data_from_api.csv', index=False)
        ##print("Data from API exported to 'data_from_api.csv'")
    else:
        print("Failed to retrieve data from API.")
 """


class GetApi():
    def __init__(self, url):
        self.url = 'http://103.150.197.96:5005/api/v1/rekapitulasi_v2/jabar/harian?level=kab'

    def get_api_data(self):
        response = requests.get(self.url)
        result = response.json()['data']['content']
        logging.info('GET DATA FROM API COMPLETED')
        df = pd.json_normalize(result)
        logging.info('LOAD DATA TO DATAFRAME READY')
        return df

    