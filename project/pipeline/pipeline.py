# main.py
from extract import extract_fao_temperature_data, extract_world_bank_co2_data
from trasform import transform_temperature_data, transform_co2_data
from load import merge_datasets, save_to_sqlite
from colorama import init, Fore


# Initialize colorama
init(autoreset=True)


def main():
    # URLs to the datasets
    fao_zip_url = 'https://bulks-faostat.fao.org/production/Environment_Temperature_change_E_All_Data.zip'
    world_bank_url = 'https://api.worldbank.org/v2/en/indicator/EN.ATM.CO2E.KT?downloadformat=csv'

    # Extract data
    temperature_data = extract_fao_temperature_data(fao_zip_url)
    co2_data = extract_world_bank_co2_data(world_bank_url)

    # Check if data extraction was successful
    if temperature_data is not None:
        print(Fore.GREEN + "Successfully extracted FAO temperature data.")

        temperature_data = transform_temperature_data(temperature_data)
        print(temperature_data.head())
    else:
        print(Fore.RED + "Failed to extract FAO temperature data.")

    if co2_data is not None:
        print(Fore.GREEN + "Successfully extracted World Bank CO2 data.")

        co2_data = transform_co2_data(co2_data)
        print(co2_data.head())
    else:
        print(Fore.RED + "Failed to extract World Bank CO2 data.")

    if temperature_data is not None and co2_data is not None:
        merged_data = merge_datasets(temperature_data, co2_data)
        if merged_data is not None:
            print(Fore.GREEN + "Merged Data:")
            print(merged_data.head())
            save_to_sqlite(merged_data, 'pipelineDB', 'tempCO2')

    else:
        print(Fore.YELLOW +
              "Skipping merge and save since one or both datasets are unavailable.")


if __name__ == "__main__":
    main()
