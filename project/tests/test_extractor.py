import requests
import pytest
import pandas as pd
from io import StringIO
from etl_pipeline.extractor import extract_csv  

@pytest.fixture
def sample_csv_url() -> str:
    """
    Fixture for a sample CSV content.

    :return: URL of the sample CSV file.
    :rtype: str
    """
    return "https://people.sc.fsu.edu/~jburkardt/data/csv/airtravel.csv"

@pytest.fixture
def mock_response(mocker) -> callable:
    """
    Fixture for mocking requests.get.

    :param mocker: The mocker fixture from pytest-mock.
    :type mocker: pytest_mock.plugin.MockerFixture
    :return: A function that returns a mock response object.
    :rtype: callable
    """
    def _mock_response(content: str):
        response = mocker.Mock()
        response.status_code = 200
        response.text = content
        return response
    return _mock_response

def test_download_csv_success(mocker, sample_csv_url: str, mock_response: callable) -> None:
    """
    Test the download_csv function for successful CSV download.

    :param mocker: The mocker fixture from pytest-mock.
    :type mocker: pytest_mock.plugin.MockerFixture
    :param sample_csv_url: URL of the sample CSV file.
    :type sample_csv_url: str
    :param mock_response: Function that returns a mock response object.
    :type mock_response: callable
    :return: None
    """
    # Mock the requests.get to return a sample CSV content
    sample_csv_content = "Month,1958,1959,1960\nJAN,340,360,417\nFEB,318,342,391"
    mocker.patch('requests.get', return_value=mock_response(sample_csv_content))

    # Call the function
    df = extract_csv(sample_csv_url)

    # Check if the returned DataFrame matches the sample content
    expected_df = pd.read_csv(StringIO(sample_csv_content))
    pd.testing.assert_frame_equal(df, expected_df)

def test_download_csv_http_error(mocker, sample_csv_url: str) -> None:
    """
    Test the download_csv function for handling HTTP errors.

    :param mocker: The mocker fixture from pytest-mock.
    :type mocker: pytest_mock.plugin.MockerFixture
    :param sample_csv_url: URL of the sample CSV file.
    :type sample_csv_url: str
    :return: None
    """
    # Mock the requests.get to return an HTTP error
    mocker.patch('requests.get', side_effect=requests.exceptions.HTTPError("HTTP Error"))

    with pytest.raises(requests.exceptions.HTTPError, match="HTTP Error"):
        extract_csv(sample_csv_url)

if __name__ == "__main__":
    pytest.main()
