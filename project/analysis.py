import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine

####################################################
def extract_merged_dataset(path):
    engine = create_engine(f'sqlite:///{path}')
    query = "SELECT * FROM dataset_hly"
    return pd.read_sql_query(query, con=engine)

def plot_eu(df):
    df_eu = df[df['geo'] == 'European Union - 27 countries (from 2020)']
    fig, ax1 = plt.subplots(figsize=(12, 8))
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Healthy Life Years', color='tab:red')
    ax1.plot(df_eu['TIME_PERIOD'], df_eu['OBS_VALUE_hly'], color='tab:red', marker='o', label='HLY')
    ax1.tick_params(axis='y', labelcolor='tab:red')
    ax2 = ax1.twinx()
    ax2.set_ylabel('Net GHG emissions (tonnes per capita)', color='tab:blue')
    ax2.plot(df_eu['TIME_PERIOD'], df_eu['OBS_VALUE_gasem'], color='tab:blue', marker='o', label='Net GHG emissions')
    ax2.tick_params(axis='y', labelcolor='tab:blue')

    plt.title('Healthy Life Years and Net GHG emissions for EU over years')
    plt.grid(True)  
    lines, labels = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax2.legend(lines + lines2, labels + labels2, loc='upper left')
    plt.savefig('eu.png')
    plt.show()
    
    return df


def plot_gasem(df):
    plt.figure(figsize=(14, 8))
    sns.lineplot(data=df, x='TIME_PERIOD', y='OBS_VALUE_gasem', hue='geo', marker='o')
    plt.title('Net Greenhouse Gas emissions per capita across countries over years')
    plt.xlabel('Year')
    plt.ylabel('Net GHG emissions (tonnes per capita)')
    plt.legend(title='Country', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('gasem.png')
    plt.show()
    
    return df
    

def correlation_analysis(df):
    df_to_analyze = df[['OBS_VALUE_hly', 'OBS_VALUE_gasem']]
    correlation = df_to_analyze.corr()
    plt.figure(figsize=(8, 6))
    sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Correlation: Healthy Life Years and Net GHG emissions')
    plt.savefig('correlation.png')
    plt.show()


def analysis():
    df = extract_merged_dataset('../data/merged_dataset.sqlite')
    plot_eu(df)
    plot_gasem(df)
    correlation_analysis(df)
    
if __name__ == '__main__':
    analysis()
