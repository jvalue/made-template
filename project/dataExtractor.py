from urllib.request import urlretrieve

url = 'https://opendata.rhein-kreis-neuss.de/api/v2/catalog/datasets/stadt-neuss-herbstpflanzung-2023/exports/csv'

filename = "../data/myfile.csv"
localFileName, headers = urlretrieve(url,filename)