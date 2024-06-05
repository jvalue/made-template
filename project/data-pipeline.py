import pandas as pd
import sqlalchemy as sql

destination_dir = 'data'


def drop_rows(df, mask):
    df.drop(df[mask].index, axis=0, inplace=True)


def create_emissions_data(name, url, sql_engine):
    print('downloading emissions data')
    emissions_sheet = pd.read_csv(url, sep=',')

    print('processing emissions data')

    # filter rows
    # 1. Source sectors for greenhouse gas emissions:
    #    TOTXMEMONIA - Total (excluding memo items, including international aviation)
    src_crf_mask = emissions_sheet['src_crf'] != 'TOTXMEMONIA'
    drop_rows(emissions_sheet, src_crf_mask)

    # 2. Unit of measure
    #    T_HAB - Tonnes per capita
    unit_mask = emissions_sheet['unit'] != 'T_HAB'
    drop_rows(emissions_sheet, unit_mask)

    # filter columns
    emissions_sheet.drop(labels=['DATAFLOW', 'LAST UPDATE', 'freq', 'airpol', 'src_crf', 'unit', 'OBS_FLAG'], axis=1, inplace=True)

    print('writing emissions data')
    emissions_sheet.to_sql(name, sql_engine, if_exists='replace', index=False)


def create_energy_consumption_data(name, url, sql_engine):
    print('downloading energy consumption data')
    energy_consumption_sheet = pd.read_csv(url, sep=',')

    print('processing energy consumption data')

    # filter rows
    # 1. Unit of measure
    #    TOE_HAB - Tonnes of oil equivalent (TOE) per capita
    unit_mask = energy_consumption_sheet['unit'] != 'TOE_HAB'
    drop_rows(energy_consumption_sheet, unit_mask)

    # filter columns
    energy_consumption_sheet.drop(labels=['DATAFLOW', 'LAST UPDATE', 'freq', 'unit', 'OBS_FLAG'], axis=1, inplace=True)

    print('writing energy consumption data')
    energy_consumption_sheet.to_sql(name, sql_engine, if_exists='replace', index=False)


def create_energy_share_data(name, url, sql_engine):
    print('downloading energy share data')
    energy_share_sheet = pd.read_csv(url, sep=',')

    print('processing energy share data')

    # filter rows
    # 1. Energy balance
    #    REN - Renewable energy sources
    nrg_bal_mask = energy_share_sheet['nrg_bal'] != 'REN'
    drop_rows(energy_share_sheet, nrg_bal_mask)

    # filter columns
    energy_share_sheet.drop(labels=['DATAFLOW', 'LAST UPDATE', 'freq', 'nrg_bal', 'unit', 'OBS_FLAG'], axis=1, inplace=True)

    print('writing energy share data')
    energy_share_sheet.to_sql(name, sql_engine, if_exists='replace', index=False)


if __name__ == '__main__':
    sql_engine = sql.create_engine(f'sqlite:///{destination_dir}/data.sqlite')

    print('running: data pipeline')

    # Datasource1: Net greenhouse gas emissions
    emissions_url = 'https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data/sdg_13_10/?format=SDMX-CSV&i'
    create_emissions_data('emissions', emissions_url, sql_engine)

    # Datasource2: Primary energy consumption
    energy_consumption_url = 'https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data/sdg_07_10/?format=SDMX-CSV&i'
    create_energy_consumption_data('energy_consumption', energy_consumption_url, sql_engine)

    # Datasource3: Share of energy from renewable sources
    energy_share_url = 'https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data/nrg_ind_ren/?format=SDMX-CSV&i'
    create_energy_share_data('energy_share', energy_share_url, sql_engine)

    print('success: data pipeline')
