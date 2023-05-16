from datetime import datetime


class DataProcessor:
    def __init__(self) -> None:
        pass

    def process_date_format(self, date):
        """Convert string date format (YYMMDDHHMM) to (YYYY-MM-DD-HH-MM).

        Args:
            date (str): date in (YYMMDDHHMM) format.

        Returns:
            str: date in (YYYY-MM-DD-HH-MM) format.
        """
        if date:
            date = datetime.strptime(date, "%Y-%M-%D-%H-%M")
        return date
