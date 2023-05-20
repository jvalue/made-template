from datetime import datetime


class DataProcessor:
    def __init__(self) -> None:
        pass

    @staticmethod
    def process_date_format(date):
        """Convert string date format (YYMMDDHHMM) to (YYYY-MM-DD-HH-MM).

        Args:
            date (str): date in (YYMMDDHHMM) format.

        Returns:
            str: date in (YYYY-MM-DD-HH-MM) format.
        """
        if date and not (date == "N/A"):
            date = datetime.strptime(
                date, "%y%m%d%H%M").strftime('%Y-%m-%d %H:%M')
        return date


if __name__ == "__main__":
    dp = DataProcessor()
    out = dp.process_date_format("2305160945")
    print(out)
