import yfinance as yf
import pandas as pd
from pathlib import Path


def download_market_data(ticker, start_date, end_date, save_dir='data/raw'):
    
    # Step 1: Download Data
    df= yf.download(ticker, start=start_date, end=end_date) #downloads the ticker data from start to end.
    
    # Step 2: Validate Data
    if df.empty:    #If dataframe empty = True, raise an error
        raise ValueError(f"No data found for ticker: '{ticker}'. Check if ticker is valid.")

    # Step 3: Create/Ensure directory path
    dir_path = Path(save_dir) # Saves path as save_dir
    dir_path.mkdir(parents=True, exist_ok=True) # Creates the FOLDER 'data/raw'

    # Step 3b: Create file path
    file_path = dir_path / f"{ticker}.csv" # Path('data/raw/AAPL.csv')

    #Step 4: Save to CSV
    df.to_csv(file_path, index=True)
    return str(file_path) # Returns the path as a string 'data/raw/AAPL.csv'


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
