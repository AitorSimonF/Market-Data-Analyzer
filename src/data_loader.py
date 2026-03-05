import pandas as pd

# Handles reading CSVs, basic validation."""'data_loader.py
"""
Purpose: Load historical market data from CSV files.

Responsibilities:
- Read CSV from filepath
- Validate structure (required columns exist)
- Handle missing data
Return clean DataFrame with Datetimeindex
"""

def load_market_data(filepath, date_column = 'Date', price_column = 'Close/Last'):

    '''
    Load historical market data from CSV.

    '''

    df = pd.read_csv(filepath)  # Reads CSV using filepath parameter.       

    if date_column not in df.columns:  # Checks if date_column is in the CSV.
        raise ValueError(f"Date column '{date_column}' not found in CSV.")

    if price_column not in df.columns:  # Checks if price_column is in the CSV.
        raise ValueError(f"Price column '{price_column}' not found in CSV.")

    df['Date'] = pd.to_datetime(df[date_column])  # Converts date_column to datetime.
    df = df.set_index('Date')  # Sets date_column as index.
    df = df[[price_column]]  # Selects price_column.

    return df
"""
    Returns:
    --------
    pandas.DataFrame
        - Index: DatetimeIndex (dates)
        - Columns: Asset Price(s)
        - Clean, ready for analysis.
    
"""   