import pandas as pd
from colorama import init, Fore

# Initialize colorama
init(autoreset=True)


def transform_temperature_data(df: pd.DataFrame):
    """
    Transforms and cleans the FAO temperature data.

    Args:
    - df (pd.DataFrame): DataFrame containing the raw temperature data.

    Returns:
    - pd.DataFrame: Cleaned and transformed DataFrame.
    """
    try:

        # keep only the rows that contains temperature change
        df = df[df['Element'] == 'Temperature change']

        # drop irrelevant columns
        df = df.drop(['Area Code', 'Area Code (M49)', 'Element Code', 'Months Code',
                      'Unit', 'Element'], axis=1)

        # Rename columns for consistency

        desired_months = ['January', 'February', 'March', 'April', 'May', 'June',
                          'July', 'August', 'September', 'October', 'November', 'December']
        df = df[df['Months'].isin(desired_months)]

        yrs = range(1961, 2023)
        for yr in yrs:
            df = df[df[f'Y{yr}F'] == 'E']
            df = df.drop(f'Y{yr}F', axis=1)

        value_vars = [f'Y{yr}' for yr in yrs]

        df = pd.melt(df, id_vars=['Area', 'Months'], value_vars=value_vars,
                     var_name='Year', value_name='Change')

        # remove Y from each year and convert datatype to int
        df['Year'] = df['Year'].str[1:].astype(int)

        # Aggregate to yearly data by taking the mean temperature change for each

        df = df.groupby(['Area', 'Year'], as_index=False)[
            'Change'].mean()

        print(Fore.GREEN + "Successfully transformed FAO temperature data.")
        return df
    except Exception as e:
        print(Fore.RED + f"Error transforming FAO temperature data: {e}")
        return None


def transform_co2_data(df: pd.DataFrame):
    """
    Transforms and cleans the World Bank CO2 emissions data.

    Args:
    - df (pd.DataFrame): DataFrame containing the raw CO2 emissions data.

    Returns:
    - pd.DataFrame: Cleaned and transformed DataFrame.
    """
    try:
        # Rename columns for consistency
        df = df.rename(columns={'Country Name': 'Area',
                       'Country Code': 'country_code'})

        # Drop unnecessary columns
        df = df.drop(columns=['Indicator Name', 'Indicator Code'])

        # Reshape the data from wide to long format
        df = df.melt(id_vars=['Area', 'country_code'],
                     var_name='year', value_name='co2_emissions')

        # Drop rows with missing CO2 emission values
        df = df.dropna(subset=['co2_emissions'])

        # Convert data types
        df['year'] = df['year'].astype(int)

        df = df.rename(columns={'year': 'Year'})

        df['co2_emissions'] = df['co2_emissions'].astype(float)

        print(Fore.GREEN + "Successfully transformed World Bank CO2 data.")
        return df
    except Exception as e:
        print(Fore.RED + f"Error transforming World Bank CO2 data: {e}")
        return None
