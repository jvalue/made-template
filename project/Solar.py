import os
import requests
import zipfile
import pandas as pd
import sqlite3


def download_zipfile(url, output_path):
    if not os.path.isfile(output_path):
        response = requests.get(url)
        if response.status_code == 200:
            with open(output_path, 'wb') as out:
                out.write(response.content)
            print(f"Downloaded the file to {output_path}")
        else:
            raise Exception(f"Failed to download file from {url}")
    else:
        print(f"File already exists at {output_path}")


def extract_zipfile(zip_path, extract_to):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
        print(f"Extracted the file tod {extract_to}")


def convert_csv_to_sqlite(extract_to, csv_filename, db_filename, table_name):
    csv_path = os.path.join(extract_to, csv_filename)
    if os.path.isfile(csv_path):
        df = pd.read_csv(csv_path)
        db_path = os.path.join(extract_to, db_filename)
        conn = sqlite3.connect(db_path)
        df.to_sql(table_name, conn, if_exists="replace", index=False)
        conn.close()
        print(f"Saved {csv_filename} to {db_filename} in table {table_name}")
    else:
        raise FileNotFoundError(f"{csv_filename} not found in {extract_to}")


base_dir = '../data'
zip_path = os.path.join(base_dir, 'archive.zip')
extract_to = os.path.join(base_dir)
url = 'https://storage.googleapis.com/kaggle-data-sets/1296/2322/bundle/archive.zip?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20240605%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20240605T131315Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=574161479b9e52681ae0e479ac5342d12712d6fd454216ac3db3fc49f217407e909ced47358bada13609b7c49bd1fcb157c82b62f4e2e56a2e57078af0bd3e0b2ec6a0be52aa14cbc579a59b50cfaac566e74f757e78bc1a98245cff85f6f1f166a9dc519c1aaf685bd29bcf4af211325f91b40be87343dc5f811df46966375357142c3293a7136e21655c62c0490d98f2f8dbaf5901667356e3d0486598e8f802bf16c564bcddd1016f307ca4d18444a7047a66a6d7e8266dee39d8d6d9c8794cc0aabe963f15dc6eb200509f777230ebf1e5b69e718d5760edf4bb1fd79ec729cfbcbe9652150122aa1704935e4a9571b15eac8c381bab076ef3d0a180da12'

os.makedirs(extract_to, exist_ok=True)

download_zipfile(url, zip_path)
extract_zipfile(zip_path, extract_to)

csv_filename = 'SolarPrediction.csv'
sqlite_filename = 'solar_data.db'
table_name = 'solar_prediction'

convert_csv_to_sqlite(extract_to, csv_filename, sqlite_filename, table_name)

os.remove("../data/archive.zip")
os.remove("../data/SolarPrediction.csv")
