import matplotlib.pyplot as plt
import pandas as pd
import geopandas as gpd

def plot_overall_average_temperature_change(df: pd.DataFrame) -> None:
    """
    Plot the overall average temperature change over the years.

    :param df: pd.DataFrame
        DataFrame containing the annual surface temperature change data.
    """
    year_columns = df.columns[2:]
    avg_temp_change = df[year_columns].mean()
    
    plt.figure(figsize=(14, 7))
    avg_temp_change.plot()
    plt.title('Average Worldwide Surface Temperature Change Over Years')
    plt.xlabel('Year')
    plt.ylabel('Average Temperature Change in Degree Celsius')
    plt.grid(True)
    plt.show()


def plot_compare_countries_temperature_trend(df: pd.DataFrame, country1: str, country2: str) -> None:
    """
    Compare the temperature change trends of two countries over the years.

    :param df: pd.DataFrame
        DataFrame containing the annual surface temperature change data.
    :param country1: str
        The name of the first country.
    :param country2: str
        The name of the second country.
    """
    country1_data = df[df['Country'] == country1]
    country2_data = df[df['Country'] == country2]
    
    if country1_data.empty:
        print(f"Country '{country1}' is not found in the data.")
        return
    if country2_data.empty:
        print(f"Country '{country2}' is not found in the data.")
        return
    
    # Extract year columns
    year_columns = df.columns[2:]
    
    # Plotting
    plt.figure(figsize=(14, 7))
    plt.plot(year_columns, country1_data[year_columns].values.flatten(), label=country1)
    plt.plot(year_columns, country2_data[year_columns].values.flatten(), label=country2)
    plt.title(f'Comparison of Surface Temperature Change Trends\n{country1} vs {country2}')
    plt.xlabel('Year')
    plt.ylabel('Temperature Change in Degree Celsius')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.legend()
    plt.show()

def plot_average_temperature_change_map(merged: gpd.GeoDataFrame) -> None:
    """
    Create a map visualization of all countries with the average change in temperature.

    :param merged: gpd.GeoDataFrame
        GeoDataFrame containing the merged world map and temperature change data.
    """
    fig, ax = plt.subplots(1, 1, figsize=(15, 10))
    merged.plot(column='Average_Temperature_Change', ax=ax, legend=True,
                legend_kwds={'label': "Average Temperature Change (°C)",
                             'orientation': "horizontal"},
                cmap='viridis', missing_kwds={'color': 'lightgrey'})
    plt.title('Average Surface Temperature Change by Country')
    plt.show()
