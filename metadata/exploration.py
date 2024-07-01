import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.dates as mdates
import seaborn as sns


class exploration:

    def __init__(self):
        pass

    def read_sqlite(self, dbfile):
        import sqlite3
        from pandas import read_sql_query, read_sql_table

        with sqlite3.connect(dbfile) as dbcon:
            tables = list(read_sql_query("SELECT name FROM sqlite_master WHERE type='table';", dbcon)['name'])
            output = {tbl: read_sql_query(f"SELECT * from {tbl}", dbcon) for tbl in tables}

        return output

    def visualize_Total_Production_Per_Year(self, years, itemProdInTonnes):
        plt.plot(years, itemProdInTonnes, label="Item production in Tonnes from 1970 to 2019", color="Red")
        plt.xlabel("Years")
        plt.ylabel("Item production in Tonnes")
        plt.legend()
        plt.show()

    def visualize_Yield_Per_Year(self, years, yieldHgHa):
        plt.plot(years, yieldHgHa, label="Yield in (hg/ha) from 1970 to 2019")
        plt.xlabel("Years")
        plt.ylabel("Yield")
        plt.legend()
        plt.show()

    def visualize_Production_Per_Year_Per_Staple_Food(self, years, total_production_per_item):
        plt.figure(figsize=(20, 20))
        for i in list(total_production_per_item.keys()):
            plt.plot(years, total_production_per_item[i])
            # plt.plot(years, total_production_per_item[i], label= str(i)+" production in Tonnes from 1970 to 2019", color="Red")
        plt.xlabel("Years")
        plt.ylabel("Item production in Tonnes")
        # plt.legend()
        plt.show()

    def visualize_staple_food_by_continent(self, years, staple_food_by_continents, total_production_per_item):
        # plt.figure(figsize=(10, 6))
        fig, axs = plt.subplots(3, 2, sharex=False, sharey=False, figsize=(30, 15))
        fig.tight_layout()
        # print(staple_food_by_continents['Africa'])

        for j in staple_food_by_continents["Africa"]:
            axs[0, 0].plot(years, total_production_per_item[j], label=j, linewidth=3.0)
            axs[0, 0].set_title("African Staples")
            axs[0, 0].legend(loc=2, prop={'size': 15})
            axs[0, 0].xaxis.label.set_size(20)
            axs[0, 0].tick_params(axis='both', which='major', labelsize=10)
        for j in staple_food_by_continents["America"]:
            axs[0, 1].plot(years, total_production_per_item[j], label=j, linewidth=3.0)
            axs[0, 1].set_title("American Staples")
            axs[0, 1].legend(loc=2, prop={'size': 15})
        for j in staple_food_by_continents["Asia"]:
            axs[1, 0].plot(years, total_production_per_item[j], label=j, linewidth=3.0)
            axs[1, 0].set_title("Asian Staples")
            axs[1, 0].legend(loc=2, prop={'size': 15})
        for j in staple_food_by_continents["Europe"]:
            axs[1, 1].plot(years, total_production_per_item[j], label=j, linewidth=3.0)
            axs[1, 1].set_title("Europen Staples")
            axs[1, 1].legend(loc=2, prop={'size': 15})
        for j in staple_food_by_continents["Oceania"]:
            axs[2, 0].plot(years, total_production_per_item[j], label=j, linewidth=3.0)
            axs[2, 0].set_title("Oceania Staples")
            axs[2, 0].legend(loc=2, prop={'size': 15})
        plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=None)
        plt.show()

    def visualize_average_world_inflation_Per_Year(self, years, cpi):
        plt.plot(years, cpi, label="Average Inflation from 1970 to 2019")
        plt.xlabel("Years")
        plt.ylabel("Avg Inflation")
        plt.legend()
        plt.show()

    def visualize_avg_temp_change_and_inflation_Per_Year_and_yield_per_year(self, new_df):
        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(15, 5))
        sns.lineplot(data=new_df, x='years', y='temp_change_avg_per_year', ax=ax1, marker='o', color='g',
                     label="Temperature Change")
        ax1.legend(loc='upper right')
        sns.lineplot(data=new_df, x='years', y='yield_per_hectare', ax=ax2, marker='o', color='r',
                     dashes=True, label="Yield")
        ax2.legend(loc='upper right')
        sns.lineplot(data=new_df, x='years', y='cpi_inflation', ax=ax3, marker='o', color='b', label="Inflation")
        ax3.legend(loc='upper right')
        plt.show()

    def get_continent(self, df, country_name):
        try:
            continent = df.loc[df['Country'] == country_name, 'Continent'].values[0]
            return continent
        except IndexError:
            return "Country not found"

    def visualize_correlation_between_yield_temp_cpi(self, new_df):
        fig, ax = plt.subplots(1, 1, figsize=(15, 10))
        # compute the correlation matrix
        corr = new_df.corr()
        # generate a mask for the upper triangle
        mask = np.triu(np.ones_like(corr, dtype=bool))

        sns.heatmap(new_df.corr(), annot=True, fmt='.2f', vmin=-1, vmax=1, cmap='coolwarm',
                    mask=mask, square=True, linewidths=.5, xticklabels=True, yticklabels=True)
        ax.set_xticklabels(corr.columns)
        plt.title('Correlation Matrix')
        plt.show()

    def visualize_all_visuals(self, db, years, itemProdInTonnes, staple_food_by_continents, total_production_per_item,
                              new_df):
        db.visualize_Total_Production_Per_Year(years, itemProdInTonnes)
        db.visualize_staple_food_by_continent(years, staple_food_by_continents, total_production_per_item)
        db.visualize_avg_temp_change_and_inflation_Per_Year_and_yield_per_year(new_df)
        db.visualize_correlation_between_yield_temp_cpi(new_df)

    def visualize_cpi_temp_per_continent_per_year(self, temp_country_continent_mapping_df,
                                                  cpi_country_continent_mapping_df):
        temp_continent_list = []
        for i in range(len(temp_data)):
            temp_continent_list.append(
                db.get_continent(temp_country_continent_mapping_df, temp_data.iloc[i]['country_name']))
        temp_data['continent'] = pd.Series(temp_continent_list)
        cpi_continent_list = []
        for i in range(len(cpi_data)):
            cpi_continent_list.append(
                db.get_continent(cpi_country_continent_mapping_df, cpi_data.iloc[i]['country_name']))
        cpi_data['continent'] = pd.Series(cpi_continent_list)
        avg_cpi_data_per_continent_per_year = cpi_data.groupby(['continent', 'year'])['cpi'].mean().reset_index()
        avg_temp_change_per_continent_per_year = temp_data.groupby(['continent', 'year'])[
            'Surface Temperature Change in °C'].mean().reset_index()
        continents = avg_cpi_data_per_continent_per_year['continent'].unique()
        num_continents = len(continents)
        fig, axs = plt.subplots(num_continents, 1, figsize=(10, 6 * num_continents), sharex=False)
        for i, continent in enumerate(continents):
            ax = axs[i] if num_continents > 1 else axs
            cpi_continent_data = avg_cpi_data_per_continent_per_year[
                avg_cpi_data_per_continent_per_year['continent'] == continent]
            temp_continent_data = avg_temp_change_per_continent_per_year[
                avg_temp_change_per_continent_per_year['continent'] == continent]
            ax2 = ax.twinx()
            ax.plot(cpi_continent_data['year'], cpi_continent_data['cpi'], marker='o', label='CPI', color='r')
            ax2.plot(temp_continent_data['year'], temp_continent_data['Surface Temperature Change in °C'], marker='^',
                     label='Surface Temp. Change')
            ax.set_title(f'CPI and Surface Temp Change by Year(1970-2019) for {continent}')
            ax.set_xlabel('Year')
            ax.set_ylabel('CPI')
            ax2.set_ylabel('Surface Temperature Change in °C')
            ax.legend(loc='upper left')
            ax2.legend(loc='upper right')
            ax.xaxis.set_major_locator(mdates.WeekdayLocator())
        plt.tight_layout()
        plt.show()


if __name__ == '__main__':
    db = exploration()
    dbfile = '../data/made_db.db'
    out = db.read_sqlite(dbfile)
    cpi_data = out.get("cpi_data")
    cpi_data.drop(cpi_data.index[:1860], inplace=True)
    cpi_data = cpi_data.truncate(before=1860, after=10973)
    cpi_data.index = np.arange(len(cpi_data))
    temp_data = out.get("temp_data")
    area_harvested_data = out.get("area_harvested_data")
    yield_data = out.get("yield_data")
    production_data = out.get("production_data")
    years = production_data['Year'].unique().tolist()
    itemProdInTonnes = production_data.groupby("Year").sum()['Item production in Tonnes']

    # print([int(year[1:]) for year in production_data["Year"]])
    production_data['Year'] = pd.Series([int(year[1:]) for year in production_data["Year"]])
    yield_data['Year'] = pd.Series([int(year[1:]) for year in yield_data["Year"]])
    area_harvested_data['Year'] = pd.Series([int(year[1:]) for year in area_harvested_data["Year"]])
    # print(production_data.head())
    # analysis 1
    db.visualize_Total_Production_Per_Year(years, itemProdInTonnes)

    staple_food_by_continents = {
        'Africa': ['Yams', 'Bananas', 'Sweet potatoes'],
        # 'America':['Maize', 'Dry beans','Green beans', 'Potatoes', 'Sweet potatoes', 'Tomatoes', 'Dry Onion', 'Green Onion'],
        'America': ['Dry beans', 'Green beans', 'Sweet potatoes', 'Tomatoes', 'Dry Onion',
                    'Green Onion'],
        'Asia': ['Rice', 'Wheat', 'Soybeans', 'Peanuts'],
        'Europe': ['Strawberries', 'Raspberries', 'Blueberries', 'Cranberries', 'Dates', 'Plums', 'Millet'],
        'Oceania': ['Yams', 'Potatoes', 'Sweet potatoes', 'Coconuts']
    }

    years = pd.Series(yield_data["Year"].unique())
    years = years.drop(index=40)

    res = production_data.groupby(['Item', 'Year'])
    groups = dict(list(res))
    items = production_data['Item'].unique().tolist()

    total_production_per_item = {}

    for i in items:
        itemProdInTonnes = []
        for j in years:
            itemProdInTonnes.append(groups[i, j]['Item production in Tonnes'].sum())
        total_production_per_item[i] = itemProdInTonnes

    db.visualize_Production_Per_Year_Per_Staple_Food(years, total_production_per_item)

    # analysis 4 - Production per staple food per continent
    db.visualize_staple_food_by_continent(years,staple_food_by_continents,total_production_per_item)
    yield_per_hectare = yield_data.groupby("Year")['Yield (hg/ha)'].sum()
    yield_per_hectare = yield_per_hectare.drop(yield_per_hectare.index[40])
    yield_per_hectare = pd.Series(yield_per_hectare.tolist(), name="yield_per_hectare")

    # analysis 2
    db.visualize_Yield_Per_Year(years, yield_per_hectare)
    cpi_inflation = cpi_data.groupby(["year"])["cpi"].mean()

    # years = pd.Series(yield_data["Year"].unique())
    # years = years.drop(index=40)

    # analysis 3
    db.visualize_average_world_inflation_Per_Year(years,cpi_inflation)

    count = temp_data.groupby(["year"])['country_name'].count()
    count = count.iloc[0]
    temp_change_per_year = temp_data.groupby(["year"]).sum()

    temp_change_avg_per_year = temp_change_per_year['Surface Temperature Change in °C'].div(count)
    temp_change_avg_per_year = temp_change_avg_per_year.drop(temp_change_avg_per_year.index[40])

    # analysis 5
    df_yield_per_hectare = pd.DataFrame({"yield_per_hectare": yield_per_hectare})
    df_temp_change_avg_per_year = pd.DataFrame({"temp_change_avg_per_year": temp_change_avg_per_year})
    df_cpi_inflation = pd.DataFrame({"cpi_inflation": cpi_inflation})
    df_years = pd.DataFrame({"years": years})
    df_temp_change_avg_per_year = df_temp_change_avg_per_year.set_index(df_cpi_inflation.index)
    df_yield_per_hectare = df_yield_per_hectare.set_index(df_cpi_inflation.index)
    df_years = df_years.set_index(df_cpi_inflation.index)
    new_df = pd.concat([df_temp_change_avg_per_year, df_cpi_inflation, df_yield_per_hectare, df_years], axis=1,
                       join="inner")
    db.visualize_avg_temp_change_and_inflation_Per_Year_and_yield_per_year(new_df)

    # analysis 6
    db.visualize_correlation_between_yield_temp_cpi(new_df)

    db.visualize_all_visuals(db, years, itemProdInTonnes, staple_food_by_continents, total_production_per_item,
                          new_df)

    # print(cpi_data.shape)
    # print(cpi_data)
    temp_country_continent_mapping_df = pd.read_csv(
        "../data/temp_country_continent_mapping.csv", encoding='latin-1')
    cpi_country_continent_mapping_df = pd.read_csv(
        "../data/cpi_country_continent_mapping.csv", encoding='latin-1')

    yield_country_continent_mapping_df = pd.read_csv(
        "../data/yield_country_continent_mapping.csv", encoding='latin-1')

    db.visualize_cpi_temp_per_continent_per_year(temp_country_continent_mapping_df,cpi_country_continent_mapping_df)

    # yield_continent_list = []
    # # yield_country_continent_mapping_df.index = np.arange(len(yield_country_continent_mapping_df))
    # # temp_data.index = np.arange(len(temp_data))
    #
    # temp_data, yield_country_continent_mapping_df = temp_data.align(yield_country_continent_mapping_df, join='outer', axis=0)
    #
    # for i in range(len(yield_data)):
    #     yield_continent_list.append(
    #         db.get_continent(yield_country_continent_mapping_df, temp_data.iloc[i]['country_name']))
    #
    # yield_data['continent'] = pd.Series(yield_continent_list)

    # print(yield_data)

    #
    # avg_cpi_data_per_continent_per_year = cpi_data.groupby(['continent', 'year'])['cpi'].mean().reset_index()
    # avg_temp_change_per_continent_per_year = temp_data.groupby(['continent', 'year'])['Surface Temperature Change in °C'].mean().reset_index()
    #
    # continents = avg_cpi_data_per_continent_per_year['continent'].unique()
    #
    # num_continents = len(continents)
    # fig, axs = plt.subplots(num_continents, 1, figsize=(10, 6 * num_continents), sharex=False)
    #
    # for i, continent in enumerate(continents):
    #     ax = axs[i] if num_continents > 1 else axs
    #     cpi_continent_data = avg_cpi_data_per_continent_per_year[avg_cpi_data_per_continent_per_year['continent'] == continent]
    #     temp_continent_data = avg_temp_change_per_continent_per_year[
    #         avg_temp_change_per_continent_per_year['continent'] == continent]
    #     ax2 = ax.twinx()
    #     ax.plot(cpi_continent_data['year'], cpi_continent_data['cpi'], marker='o', label='CPI',color = 'r')
    #     ax2.plot(temp_continent_data['year'], temp_continent_data['Surface Temperature Change in °C'], marker='^', label ='Surface Temp. Change')
    #     ax.set_title(f'CPI and Surface Temp Change by Year(1970-2019) for {continent}')
    #     ax.set_xlabel('Year')
    #     ax.set_ylabel('CPI')
    #     ax2.set_ylabel('Surface Temperature Change in °C')
    #     ax.legend(loc='upper left')
    #     ax2.legend(loc='upper right')
    #     ax.xaxis.set_major_locator(mdates.WeekdayLocator())
    # plt.tight_layout()
    # plt.show()


    # print(yield_data.head())