import pytest
from etl.extract import fetch_data

@pytest.fixture
def mock_response(mocker):
    """Mock the response of pd.read_csv to simulate different scenarios."""
    mocker.patch('pandas.read_csv')

def test_fetch_data_valid_url(mock_response, mocker):
    """
    Test fetch_data function with a valid URL to ensure it returns a non-empty DataFrame.
    """
    # Setup the mock to return a DataFrame
    import pandas as pd
    mocker.patch('pandas.read_csv', return_value=pd.DataFrame({'data': [1, 2, 3]}))
    
    test_url = 'https://validurl.com/data.csv'
    result = fetch_data(test_url)
    assert not result.empty, "DataFrame should not be empty for a valid URL"

def test_fetch_data_invalid_url(mock_response, mocker):
    """
    Test fetch_data function with an invalid URL to ensure it handles errors gracefully and returns an empty DataFrame.
    """
    # Setup the mock to raise an HTTPError
    from pandas.errors import EmptyDataError
    mocker.patch('pandas.read_csv', side_effect=EmptyDataError("No columns to parse from file"))
    
    test_url = 'https://example.com/invalid_url.csv'
    result = fetch_data(test_url)
    assert result.empty, "DataFrame should be empty for an invalid URL"

def test_fetch_data_empty_data(mock_response, mocker):
    """
    Test fetch_data function with a URL pointing to an empty CSV to ensure it returns an empty DataFrame.
    """
    # Setup the mock to return an empty DataFrame
    import pandas as pd
    mocker.patch('pandas.read_csv', return_value=pd.DataFrame())
    
    test_url = 'https://example.com/empty.csv'
    result = fetch_data(test_url)
    assert result.empty, "DataFrame should be empty for an empty CSV file"