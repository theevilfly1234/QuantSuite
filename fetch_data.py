import yfinance as yf
import pandas as pd
from strategies import add_strategy_signals


def fetch_and_clean_stock_data(ticker, start_date, end_date):
    """
    Fetch and clean historical stock data for a given ticker.
    :param ticker: Stock ticker (e.g., "AAPL" for Apple)
    :param start_date: Start date in "YYYY-MM-DD" format
    :param end_date: End date in "YYYY-MM-DD" format
    :return: A cleaned Pandas DataFrame
    """
    try:
        # Fetch data
        data = yf.download(ticker, start=start_date, end=end_date)

        # Check if data is empty
        if data.empty:
            print(f"No data found for {ticker}")
            return None

        # Keep only relevant columns
        data = data[['Open', 'High', 'Low', 'Close', 'Volume']]

        # Handle missing values (fill forward)
        data.fillna(method='ffill', inplace=True)
        data.dropna(inplace=True)

        # Save cleaned data
        filename = f"{ticker}_cleaned_data.csv"
        data.to_csv(filename)
        print(f"Cleaned data saved to {filename}")

        return data

    except Exception as e:
        print(f"Error fetching or cleaning data: {e}")
        return None


# Example usage
if __name__ == "__main__":
    fetch_and_clean_stock_data("AAPL", "2022-01-01", "2022-12-31")
