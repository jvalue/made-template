import pandas as pd

destination_dir = '../data'

print('running: data pipeline')

# Datasource1: Net greenhouse gas emissions
print('processing emissions csv')
emissions_url = 'https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data/sdg_13_10/?format=SDMX-CSV&i'
emissions_sheet = pd.read_csv(emissions_url, sep=',')

emissions_sheet.to_sql('emissions', f'sqlite:///{destination_dir}/emissions.sqlite', if_exists='replace', index=False)

# Datasource2: Primary energy consumption
print('processing energy consumption csv')
energy_consumption_url = 'https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data/sdg_07_10/?format=SDMX-CSV&i'
energy_consumption_sheet = pd.read_csv(energy_consumption_url, sep=',')
energy_consumption_sheet.to_sql('energy_consumption', f'sqlite:///{destination_dir}/energy_consumption.sqlite', if_exists='replace', index=False)

# Datasource3: Share of energy from renewable sources
print('processing energy share csv')
energy_share_url = 'https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data/nrg_ind_ren/?format=SDMX-CSV&i'
energy_share_sheet = pd.read_csv(energy_share_url, sep=',')
energy_share_sheet.to_sql('energy_share', f'sqlite:///{destination_dir}/energy_share.sqlite', if_exists='replace', index=False)

print('success: data pipeline')
