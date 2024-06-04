import pandas as pd
from etl.transform import rename_year_columns, simplify_indicator, apply_transformations

def test_rename_year_columns():
    # Create a sample DataFrame
    data = {
        'F2013': [1, 2],
        'F2014': [3, 4],
        'Name': ['A', 'B']
    }
    df = pd.DataFrame(data)

    # Apply the rename function
    transformed_df = rename_year_columns(df)

    # Check if columns are renamed correctly
    assert '2013' in transformed_df.columns
    assert 'F2013' not in transformed_df.columns
    assert 'Name' in transformed_df.columns

def test_simplify_indicator():
    # Create a sample DataFrame
    data = {
        'Indicator': [
            'Climate related disasters frequency, Number of Disasters: Drought',
            'Climate related disasters frequency, Number of Disasters: Flood'
        ]
    }
    df = pd.DataFrame(data)

    # Apply the simplify function
    transformed_df = simplify_indicator(df)

    # Check if indicators are simplified correctly
    assert transformed_df['Indicator'].iloc[0] == 'Drought'
    assert transformed_df['Indicator'].iloc[1] == 'Flood'

def test_apply_transformations():
    # Create a sample DataFrame
    data = {
        'ObjectId': [1, 2],
        'Country': ['Country1', 'Country2'],
        'Indicator': ['Climate related disasters frequency, Number of Disasters: Drought', 'Climate related disasters frequency, Number of Disasters: Flood'],
        'Unit': ['Unit1', 'Unit2'],
        'F2013': [100, 200],
        'F2014': [300, 400]
    }
    df = pd.DataFrame(data)

    # Apply transformations for a specific table
    transformed_df = apply_transformations(df, 'climate_disaster_freq')

    # Check if transformation was applied correctly
    assert '2013' in transformed_df.columns
    assert 'F2013' not in transformed_df.columns
    assert transformed_df['Indicator'].iloc[0] == 'Drought'