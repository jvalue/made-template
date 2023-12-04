# import necessary libraries and file
from sqlalchemy import create_engine, inspect
from pipeline import extract_data, transform_data, load_data 

# Declaring variables for Total Tests, Passed Tests and Failed Tests
total_tests = 0
passed_tests = 0
failed_tests = 0
# Function definition for testing the extraction process
def perform_extraction_test(url):
    global total_tests, passed_tests, failed_tests
    total_tests += 1
    try:
        extracted_data = extract_data(url)
        if extracted_data.empty:
            failed_tests += 1
            raise AssertionError("Extraction failed - Dataframe is empty")
        print("perform_extraction_test: Test Passed")
        passed_tests += 1
        return extracted_data
    except Exception as e:
        failed_tests += 1
        raise AssertionError(f"Extraction failed with error: {e}")
   

# Function definition for testing the transformation process
def perform_transformation_test(data, column_map, col_to_drop):
    global total_tests, passed_tests, failed_tests
    total_tests += 1
    try:
        transformed_df = transform_data(data, column_map, col_to_drop)
        if transformed_df.isna().any().any():
            failed_tests += 1
            raise AssertionError("Transformation failed - NAN Found in Data")
        print("perform_transformation_test: Test Passed")
        passed_tests += 1
        return transformed_df
    except Exception as e:
        failed_tests += 1
        raise AssertionError(f"Transformation failed with error: {e}")

# Function definition for testing the loading process
def perform_data_loading_test(df, table_name):
    global total_tests, passed_tests, failed_tests
    total_tests += 1
    try:
        load_data(df, table_name)
        engine = create_engine("sqlite:///../data/unemployed.sqlite")
        inspector = inspect(engine)
        if not inspector.has_table(table_name):
            failed_tests += 1
            raise AssertionError(f"The table '{table_name}' does not exist in the database.")
        passed_tests += 1
        print(f"perform_data_loading_test: Table '{table_name}' exists, Test Passed")
    except Exception as e:
        failed_tests += 1
        raise AssertionError(f"Data loading failed with error: {e}")

# Define main function
def main():
    # URLs and parameters
    west_unemployed = "https://www.destatis.de/EN/Themes/Economy/Short-Term-Indicators/Labour-Market/arb120.html#241586"
    east_unemployed = "https://www.destatis.de/EN/Themes/Economy/Short-Term-Indicators/Labour-Market/arb130.html#241598"
    column_map = {'Year, month': 'year', 'Year, month.1': 'month',
                  'Total': 'total', 'Male': 'male', 'Female': 'female',
                  'Juveniles of under 20 years of age': 'under_20_year_age',
                  'Long-term unemployed': 'long_term'}
    col_to_drop = ["total", "under_20_year_age", "long_term"]

    print(f"\n=======>Test cases for West_Unemployed dataset<=======")
    # Execution block for West Unemployed dataset
    df_west = perform_extraction_test(west_unemployed)
    df_west_transformed = perform_transformation_test(df_west, column_map, col_to_drop)
    perform_data_loading_test(df_west_transformed, "unemployed_west")
    
    print(f"\n=======>Test cases for East_Unemployed dataset<=======")
    # Execution block for East Unemployed dataset
    df_east = perform_extraction_test(east_unemployed)
    df_east_transformed = perform_transformation_test(df_east, column_map, col_to_drop)
    perform_data_loading_test(df_east_transformed, "unemployed_east")
    print(f"\n=======>Test Summary<=======")
    print(f"Total Tests: {total_tests}")
    print(f"Passed Tests: {passed_tests}")
    print(f"Failed Tests: {failed_tests}")
    
# Execute the main function
if __name__ == "__main__":
    main()
