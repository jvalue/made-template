# %%
import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

URL_EU_TRANSACTION_LOG = "https://climate.ec.europa.eu/document/download/ebb2c20e-8737-4a73-b6ba-a4b7e78ecc01_en?filename=verified_emissions_2023_en_1.xlsx"
URL_EU_ETS_OPERATORS = "https://climate.ec.europa.eu/document/download/ab2c1214-decb-40bc-bb0d-d37f080bdebd_en?filename=policy_ets_registry_operators_ets_en.xlsx"
URL_CO2E_PRICE_DEVELOPMENT = "https://www.umweltbundesamt.de/sites/default/files/medien/384/bilder/dateien/2_abb_preisentwick-emissionsber-eua_2023-11-23.xlsx"
URL_GLOBAL_GHG_EMSISSIONS = "https://edgar.jrc.ec.europa.eu/booklet/EDGARv8.0_FT2022_GHG_booklet_2023.xlsx"

# for local development
# URL_EU_TRANSACTION_LOG = "./data/verified_emissions_2023_en_1.xlsx"
# URL_EU_ETS_OPERATORS = "./data/policy_ets_registry_operators_ets_en.xlsx"
# URL_CO2E_PRICE_DEVELOPMENT = "./data/2_abb_preisentwick-emissionsber-eua_2023-11-23.xlsx"
# URL_GLOBAL_GHG_EMSISSIONS = "./data/EDGARv8.0_FT2022_GHG_booklet_2023.xlsx"

# %%
# classes that'll contain the cleaned datasets
class EuropeanUnionTransactionLog:
    raw: pd.DataFrame
    cleaned: pd.DataFrame

class EUETSOperators:
    file: pd.ExcelFile
    raw: pd.DataFrame
    cleaned: pd.DataFrame

class CO2ePriceDevelopment:
    file: pd.ExcelFile
    raw: pd.DataFrame
    cleaned: pd.DataFrame

class GlobalGHGEmissions:
    file: pd.ExcelFile
    raw: pd.DataFrame
    cleaned: pd.DataFrame

eu_transaction_log = EuropeanUnionTransactionLog()
eu_ets_operators = EUETSOperators()
co2e_price_development = CO2ePriceDevelopment()
global_ghg_emissions = GlobalGHGEmissions()

# %%
# parse all separate datasets
eu_transaction_log.file = pd.ExcelFile(URL_EU_TRANSACTION_LOG)
eu_ets_operators.file= pd.ExcelFile(URL_EU_ETS_OPERATORS)
co2e_price_development.file = pd.ExcelFile(URL_CO2E_PRICE_DEVELOPMENT)
global_ghg_emissions.file = pd.ExcelFile(URL_GLOBAL_GHG_EMSISSIONS)

# %%
# clean eu transaction log dataset
eu_transaction_log_data = pd.read_excel(eu_transaction_log.file, header=21, sheet_name="data")
eu_transaction_log_activity_codes = pd.read_excel(eu_transaction_log.file, sheet_name="activity codes")

# merge with activity code description table
eu_transaction_log.raw = pd.merge(
    left=eu_transaction_log_data,
    right=eu_transaction_log_activity_codes,
    left_on="MAIN_ACTIVITY_TYPE_CODE",
    right_on="code",
)

eu_transaction_log.raw = eu_transaction_log.raw.drop(columns=["code"])
eu_transaction_log.raw = eu_transaction_log.raw.rename(
    columns={
        "value": "MAIN_ACTIVITY",
        "ALLOCATION2008": "ALLOCATION_2008",
    }
)

eu_transaction_log.cleaned = pd.DataFrame(
    columns=[
        "REGISTRY_CODE",
        "IDENTIFIER_IN_REG",
        "INSTALLATION_NAME",
        "INSTALLATION_IDENTIFIER",
        "ALLOCATION",
        "VERIFIED_EMISSIONS",
        "MAIN_ACTIVITY_TYPE_CODE",
        "MAIN_ACTIVITY",
        "YEAR",
    ]
)

for i in range(2008, 2024):
    df_i = eu_transaction_log.raw[
        [
            "REGISTRY_CODE",
            "IDENTIFIER_IN_REG",
            "INSTALLATION_NAME",
            "INSTALLATION_IDENTIFIER",
            f"ALLOCATION_{i}",
            f"VERIFIED_EMISSIONS_{i}",
            "MAIN_ACTIVITY_TYPE_CODE",
            "MAIN_ACTIVITY",
        ]
    ]

    df_i = df_i.rename(columns=lambda x: x.removesuffix(f"_{i}"))
    df_i = df_i.assign(YEAR=i)
    df_i["EXCLUDED"] = df_i["VERIFIED_EMISSIONS"].apply(lambda x: True if x == "Excluded" else False)
    df_i["VERIFIED_EMISSIONS"] = df_i["VERIFIED_EMISSIONS"].apply(lambda x: -1 if x == "Excluded" else x)

    # sum up verified emissions / allocation and ch verified emissions / allocation
    if f"CH_VERIFIED_EMISSIONS_{i}" in eu_transaction_log.raw.columns:
        eu_transaction_log.raw[f"CH_VERIFIED_EMISSIONS_{i}"] = eu_transaction_log.raw[f"CH_VERIFIED_EMISSIONS_{i}"].apply(lambda x: 0 if x == -1 or x == "Excluded" else x)
        df_i["VERIFIED_EMISSIONS"] = df_i["VERIFIED_EMISSIONS"] + eu_transaction_log.raw[f"CH_VERIFIED_EMISSIONS_{i}"]

    if f"CH_ALLOCATION_{i}" in eu_transaction_log.raw.columns:
        eu_transaction_log.raw[f"CH_ALLOCATION_{i}"] = eu_transaction_log.raw[f"CH_ALLOCATION_{i}"].apply(lambda x: 0 if x == -1 or x == "Excluded" else x)
        df_i["ALLOCATION"] = df_i["ALLOCATION"] + eu_transaction_log.raw[f"CH_ALLOCATION_{i}"]

    eu_transaction_log.cleaned = pd.concat([eu_transaction_log.cleaned, df_i])


eu_transaction_log.cleaned.head(n=100)

# %%
# clean eu ets operators dataset
eu_ets_operators.raw = pd.read_excel(eu_ets_operators.file)
eu_ets_operators.cleaned = eu_ets_operators.raw
eu_ets_operators.cleaned.head()

# %%
# clean co2e price development dataset
co2e_price_development.raw = pd.read_excel(
    co2e_price_development.file, 
    sheet_name="Daten", 
    header=9, 
    usecols="B,C", 
    names=["date", "price"]
)

co2e_price_development.cleaned = co2e_price_development.raw.dropna()
co2e_price_development.cleaned.head()

# %%
# clean global ghg emissions dataset
global_ghg_emissions.raw = pd.read_excel(global_ghg_emissions.file, sheet_name="GHG_totals_by_country")
global_ghg_emissions.cleaned = global_ghg_emissions.raw.dropna()
global_ghg_emissions.cleaned.tail()

# %%
# save all cleaned datasets to sqlite
conn = sqlite3.connect(r"./data/data.sqlite")

eu_transaction_log.cleaned.to_sql("eu_transaction_log", conn, if_exists="replace", index=True)
eu_ets_operators.cleaned.to_sql("eu_ets_operators", conn, if_exists="replace", index=True)
co2e_price_development.cleaned.to_sql("co2e_price_development", conn, if_exists="replace", index=True)
global_ghg_emissions.cleaned.to_sql("global_ghg_emissions", conn, if_exists="replace", index=True)


