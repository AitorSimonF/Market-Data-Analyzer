from src.data_loader import load_market_data

# Test the function
df = load_market_data('/Users/aitorfungairino/Desktop/MyProjects/APPL 1Y Data.csv')

# Inspect the result
print(df.head())
print(f"/nShape: {df.shape}")
print(f"/nIndex: {df.index}")
print(f"/nColumns: {df.columns.tolist}")

