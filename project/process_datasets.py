
import pandas as pd
import os
from glob import glob

# Define the paths for the datasets
dataset1_path = 'dataset1/'  # Path for the Indian Cities Cancer Dataset
dataset2_path = 'dataset2/data.csv'  # Path for the Breast Cancer Prediction Dataset

# Function to read and combine Indian Cities Cancer Dataset
def read_and_combine_dataset1(path):
    all_files = glob(os.path.join(path, "*.csv"))
    df_list = []
    for filename in all_files:
        df = pd.read_csv(filename, index_col=None, header=0)
        df['City'] = os.path.basename(filename).split('_')[0]  # Extract city name from filename
        df_list.append(df)
    combined_df = pd.concat(df_list, axis=0, ignore_index=True)
    return combined_df

# Function to read Breast Cancer Prediction Dataset
def read_dataset2(path):
    return pd.read_csv(path)

# Function to clean and transform datasets
def clean_transform_datasets(df1, df2):
    # Basic cleaning and transformation can be added here
    # For example, handling missing values, renaming columns, etc.
    
    return df1, df2

# Main execution
def main():
    # Read and combine the datasets
    dataset1 = read_and_combine_dataset1(dataset1_path)
    dataset2 = read_dataset2(dataset2_path)

    # Clean and transform the datasets
    dataset1_clean, dataset2_clean = clean_transform_datasets(dataset1, dataset2)

    # Save the cleaned datasets
    dataset1_clean.to_csv('/data/combined_indian_cities_cancer_dataset.csv', index=False)
    dataset2_clean.to_csv('/data/breast_cancer_prediction_dataset.csv', index=False)

if __name__ == "__main__":
    main()
