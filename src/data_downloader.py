import yfinance as yf
import pandas as pd
from pathlib import Path


def download_market_data(ticker, start_date, end_date, save_dir='data/raw'):
    """
    Download historical market data from Yahoo Finance and save to CSV.
    
    Parameters:
    -----------
    ticker : str
        Stock ticker symbol (e.g., 'AAPL', 'SPY', 'TSLA')
    start_date : str
        Start date in 'YYYY-MM-DD' format
    end_date : str
        End date in 'YYYY-MM-DD' format
    save_dir : str, default='data/raw'
        Directory to save the CSV file
    
    Returns:
    --------
    str
        Path to the saved CSV file
    
    What This Function Needs To Do:
    --------------------------------
    1. Use yfinance to download data for the ticker
    2. Validate that data was successfully downloaded
    3. Ensure column names are standardized:
       - 'Date' (as index)
       - 'Adj Close' (adjusted closing price)
       - 'Volume', 'Open', 'High', 'Low' (optional, but standardized)
    4. Create the save directory if it doesn't exist
    5. Save to CSV with filename format: {ticker}.csv
    6. Return the filepath so user knows where it was saved
    
    Research Tasks for Next Session:
    ---------------------------------
    Task 1: How to use yfinance.download()
    - Google: "yfinance download historical data"
    - Find: Basic syntax, required parameters
    
    Task 2: How yfinance returns data
    - What data structure does it return? (DataFrame? Series?)
    - What are the default column names?
    
    Task 3: How to create directories in Python
    - Google: "python pathlib create directory if not exists"
    - Find: How to ensure save_dir exists before saving
    
    Task 4: How to save DataFrame to CSV
    - You know pd.read_csv(), now find the reverse operation
    - Google: "pandas save dataframe to csv"
    """
    pass


# Optional: Function to download multiple tickers at once
def download_multiple_tickers(tickers, start_date, end_date, save_dir='data/raw'):
    """
    Download data for multiple tickers.
    
    Parameters:
    -----------
    tickers : list of str
        List of ticker symbols (e.g., ['AAPL', 'SPY', 'MSFT'])
    start_date : str
        Start date in 'YYYY-MM-DD' format
    end_date : str
        End date in 'YYYY-MM-DD' format
    save_dir : str, default='data/raw'
        Directory to save CSV files
    
    Returns:
    --------
    list of str
        List of filepaths for all saved CSV files
    
    Implementation Idea:
    --------------------
    - Loop through tickers list
    - Call download_market_data() for each ticker
    - Collect all filepaths and return them
    
    This can wait until after download_market_data() works.
    """
    pass
