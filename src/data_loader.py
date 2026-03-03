# Handles reading CSVs, basic validation."""'data_loader.py
"""
Purpose: Load historical market data from CSV files.

Responsibilities:
- Read CSV from filepath
- Validate structure (required columns exist)
- Handle missing data
Return clean DataFrame with Datetimeindex
"""

def load_market_data(filepath, date_column = 'Date', price_column = 'Adj Close'):

    """
    Load historical market data from CSV.

    Parameters:
    -----------
    filepath : str
        path to the CSV file
    Date_column : str, default = 'Date'
        Name of the column containing dates
    price_column : str, default = 'Adj Close'
        Name of the column containing prices.

    Returns:
    --------
    pandas.DataFrame
        - Index: DatetimeIndex (dates)
        - Columns: Asset Price(s)
        - Clean, ready for analysis.
    
    """
    pass