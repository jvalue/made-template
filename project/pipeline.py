 
from sqlalchemy import create_engine
import pandas as pd
import sqlite3
import requests
import os
from pathlib import Path

class DataPipeline:
    def __init__(self, file1_path, file2_path, output_directory):
        self.file1_path = file1_path
        self.file2_path = file2_path
        self.output_directory = output_directory
       # self.table_name = table_name

    def read_csv_files(self):
        df1 = pd.read_csv(self.file1_path)
        df2 = pd.read_csv(self.file2_path)
        return df1, df2
    
       
    def normal_to_binary(self, df1):
        # Iterate over columns
        for column in df1.columns:
            unique_values = df1[column].dropna().unique()
            if set(unique_values) == {'normal', 'abnormal'}:
                # Replace "normal" with 0, "abnormal" with 1, and missing values with the majority value
                df1[column] = df1[column].map({'normal': 0, 'abnormal': 1})
                majority_value = df1[column].mode().iloc[0]
                df1[column] = df1[column].fillna(majority_value)            
        return df1
     
    def present_to_binary(self, df1):
        # Iterate over columns
        for column in df1.columns:
            unique_values = df1[column].dropna().unique()
            if set(unique_values) == {'notpresent', 'present'}:
                # Replace "notpresent" with 0, "present" with 1, and missing values with the majority value
                df1[column] = df1[column].map({'notpresent': 0, 'present': 1})
                majority_value = df1[column].mode().iloc[0]
                df1[column] = df1[column].fillna(majority_value)            
        return df1     
    def good_to_binary(self, df1):

            # Iterate over columns
        for column in df1.columns:
            unique_values = df1[column].dropna().unique()
            if set(unique_values) == {'good', 'poor'}:
                # Replace "good" with 0, "poor" with 1, and missing values with the majority value
                df1[column] = df1[column].map({'good': 0, 'poor': 1})
                majority_value = df1[column].mode().iloc[0]
                df1[column] = df1[column].fillna(majority_value)
        return df1
    def outcome_to_binary(self, df1):

            # Iterate over columns
        for column in df1.columns:
            unique_values = df1[column].dropna().unique()
            if set(unique_values) == {'notckd', 'ckd'}:
                # Replace "notckd" with 0, "ckd" with 1, and missing values with the majority value
                df1[column] = df1[column].map({'notckd': 0, 'ckd': 1})

        return df1
    
    def yesno_to_binary(self, df1):
        for column in df1.columns:
            # Replace "yes" with 1 and "no" with 0
            df1[column] = df1[column].replace({'yes': 1, 'no': 0})
        return df1    

    def missing_with_majority(self, df1):
        for column in df1.columns:
            unique_values = df1[column].dropna().unique()
            if set(unique_values) == {0, 1}:
                # Replace missing values with the majority value
                majority_value = df1[column].mode().iloc[0]
                df1[column] = df1[column].fillna(majority_value)
        return df1


    def missing_with_mean(self, df1):
    # Convert all numeric columns to real (float)
        df1 = df1.apply(pd.to_numeric, errors='coerce')

        # Replace missing values with the mean for each column
        for column in df1.columns:
            mean_value = df1[column].mean()
            df1[column] = df1[column].fillna(mean_value)   
        return df1
    def roundnumbers(self, df1):
        # Iterate over columns
        for column in df1.columns:
            # Check if the column is numeric
            if pd.api.types.is_numeric_dtype(df1[column]):
                # Convert values based on the specified conditions
                df1[column] = df1[column].apply(lambda x: 0 if x < 0.5 else (1 if x < 1 else x))
        return df1

    def zero_with_mean_onecolumn(self, df2):
        columnlist= [ "BloodPressure" ,  "SkinThickness", "Insulin"]
        for column in columnlist:
            mean_value = df2[column].mean()
            df2[column] = df2[column].apply(lambda x: mean_value if x ==0  else x)
        return df2

 

    def merge_dataframes(self, df1, df2):
        merged_df = pd.concat([df1, df2], axis=0, ignore_index=True)
        return merged_df

    def save_to_sqlite(self, df1, df2, table_name1, table_name2):
        output_database_path = os.path.join(self.output_directory, 'madedb.sqlite')
        engine = create_engine(f'sqlite:///{output_database_path}')
        df1.to_sql(table_name1, engine, index=False, if_exists='replace')
        df2.to_sql(table_name2, engine, index=False, if_exists='replace')
        engine.dispose()
        print(f"SQLite database saved to: {output_database_path}")

if __name__ == "__main__":
    # Specify input and output paths  data
    file1_path = 'https://raw.githubusercontent.com/aiplanethub/Datasets/master/Chronic%20Kidney%20Disease%20(CKD)%20Dataset/ChronicKidneyDisease.csv'
    file2_path = 'https://raw.githubusercontent.com/npradaschnor/Pima-Indians-Diabetes-Dataset/master/diabetes.csv'
    table_name1 = Path(file1_path).stem
    table_name2 = Path(file2_path).stem
    output_directory = 'C:/Users/z004j5vt/made-template-ws2324/data/'

    # Create a DataPipeline instance
    data_pipeline = DataPipeline(file1_path, file2_path, output_directory)

    # Execute the pipeline
    df1, df2 = data_pipeline.read_csv_files()
    df1 = data_pipeline.normal_to_binary(df1)
    df1 = data_pipeline.present_to_binary(df1)
    df1 = data_pipeline.good_to_binary(df1)
    df1 = data_pipeline.outcome_to_binary(df1)
    df1 = data_pipeline.yesno_to_binary(df1)
    df1 = data_pipeline.missing_with_majority(df1)
    df1 = data_pipeline.missing_with_mean(df1)
    df1 = data_pipeline.roundnumbers(df1)
    df2 =data_pipeline.zero_with_mean_onecolumn( df2)
    df1.to_csv('output_file1.csv', index=False)
    df2.to_csv('output_file2.csv', index=False)
    #merged_df = data_pipeline.merge_dataframes(df1, df2)
    data_pipeline.save_to_sqlite(df1, df2, table_name1, table_name2)
 
