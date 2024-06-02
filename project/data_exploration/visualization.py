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

    plt.figure(figsize=(10, 6))
    avg_temp_change.plot()
    plt.title("Average Worldwide Surface Temperature Change Over Years")
    plt.xlabel("Year")
    plt.ylabel("Average Temperature Change in Degree Celsius")
    plt.grid(True)
    plt.show()


def plot_compare_countries_temperature_trend(
    df: pd.DataFrame, country1: str, country2: str
) -> None:
    """
    Compare the temperature change trends of two countries over the years.

    :param df: pd.DataFrame
        DataFrame containing the annual surface temperature change data.
    :param country1: str
        The name of the first country.
    :param country2: str
        The name of the second country.
    """
    country1_data = df[df["Country"] == country1]
    country2_data = df[df["Country"] == country2]

    if country1_data.empty:
        print(f"Country '{country1}' is not found in the data.")
        return
    if country2_data.empty:
        print(f"Country '{country2}' is not found in the data.")
        return

    # Extract year columns
    year_columns = df.columns[2:]

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(year_columns, country1_data[year_columns].values.flatten(), label=country1)
    plt.plot(year_columns, country2_data[year_columns].values.flatten(), label=country2)
    plt.title(
        f"Comparison of Surface Temperature Change Trends\n{country1} vs {country2}"
    )
    plt.xlabel("Year")
    plt.ylabel("Temperature Change in Degree Celsius")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.legend()
    plt.show()


def plot_average_value_map(
    merged: gpd.GeoDataFrame, label_and_unit: str, column: str = "Average_Value"
) -> None:
    """
    Create a map visualization of all countries
    with the average value of a specified column.

    :param merged: gpd.GeoDataFrame
        GeoDataFrame containing the merged world map and data.
    :param label_and_unit: str
        A string containing the label and unit for the legend and title.
    :param column: str, optional
        The name of the column to plot, default is "Average_Value".
    """
    label, unit = label_and_unit.split(" (")
    unit = unit.rstrip(")")

    fig, ax = plt.subplots(1, 1, figsize=(15, 10))
    merged.plot(
        column=column,
        ax=ax,
        legend=True,
        legend_kwds={
            "label": f"{label} ({unit})",
            "orientation": "horizontal",
        },
        cmap="viridis",
        missing_kwds={"color": "lightgrey"},
    )
    plt.title(f"{label} by Country")
    plt.show()


def plot_column_over_years(
    df: pd.DataFrame, date_col: str, value_col: str, label: str
) -> None:
    """
    Plot the specified column aggregated by year.

    :param df: pd.DataFrame
        DataFrame containing the data.
    :param date_col: str
        The name of the column containing date information.
    :param value_col: str
        The name of the column containing the values to be plotted.
    :param label: str
        The label for the data to be used in the plot title and ylabel.
    """

    # Convert date column to datetime
    df[date_col] = pd.to_datetime(df[date_col])

    # Set date column as index
    df.set_index(date_col, inplace=True)

    # Resample by year and calculate the mean
    yearly_data = df[value_col].resample("Y").mean()

    # Plotting
    plt.figure(figsize=(10, 6))
    yearly_data.plot()
    plt.title(f"{label} Over Years")
    plt.xlabel("Year")
    plt.ylabel(f"Average {label}")
    plt.grid(True)
    plt.show()


def plot_average_change(avg_change: pd.Series, label: str) -> None:
    """
    Plot the average change over the years.

    :param avg_change: pd.Series
        Series containing the average change for each year.
    :param label: str
        The label for the data to be used in the plot title and ylabel.
    """
    plt.figure(figsize=(10, 6))
    avg_change.plot()
    plt.title(f"Average Worldwide {label} Change Over Years")
    plt.xlabel("Year")
    plt.ylabel(f"Average {label} Change")
    plt.grid(True)
    plt.show()
