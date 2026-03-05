from src.data_loader import load_market_data

# Test the function
df = load_market_data('data/raw/APPL_1Y.csv', date_column = 'Date', price_column = 'Close/Last')

# Inspect the result
print("First 5 rows:")

print(df.head())
print(f"/nDataFrame shape: {df.shape}")
print(f"/nIndex type: {type(df.index)}")
print(f"/nColumns: {df.columns.tolist}")

