import pandas as pd

df = pd.read_csv( \
    https://opendata.rhein-kreis-neuss.de/api/v2/catalog/datasets/stadt-neuss-herbstpflanzung-2023/exports/csv, \
    sep= ';'   )

print (df.to_string())