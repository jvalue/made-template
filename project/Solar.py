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


base_dir = 'C:/Users/hatef/OneDrive/Desktop/Made-fau'
zip_path = os.path.join(base_dir, 'archive.zip')
extract_to = os.path.join(base_dir, 'data')
url = 'https://storage.googleapis.com/kaggle-data-sets/1296/2322/bundle/archive.zip?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20240523%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20240523T134509Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=1f64ab44a9aabe7f0785bd02d3bd6838fffb95d07ef73885e6f56c97125cfa965a44a31792352da9e1512826dfd766a6e24e0d61ca943990bfeee52278556531204f67a9bf67342af5585b3b68d866a974e6c9a23830aa2cec6f9ef3d6fea86a5979e01ee71fb088b814e34d509ba9ccc220ad3aeca2def6ec3a55d9a92822a58c916ac5650ab99f3119503e33915b0394cfb62206f5e6a32fb4dd72ed2d773857a7bc0aca55d6bec1219754f8d77863bdeeeb9ffa37e67effb571c54072aac4d55c7b5a20fce9dbd73a5de5412ac16d994067a39fbed875ef913c79808d9e4f55011cce14a6dc20ef085e347adb368e3ddf492d0a6f3e332463f5c3aeca348e'

os.makedirs(extract_to, exist_ok=True)

download_zipfile(url, zip_path)
extract_zipfile(zip_path, extract_to)

csv_filename = 'SolarPrediction.csv'
sqlite_filename = 'solar_data.sqlite'
table_name = 'solar_prediction'

convert_csv_to_sqlite(extract_to, csv_filename, sqlite_filename, table_name)

os.remove("C:/Users/hatef/OneDrive/Desktop/Made-fau/archive.zip")
os.remove("C:/Users/hatef/OneDrive/Desktop/Made-fau/data/SolarPrediction.csv")
