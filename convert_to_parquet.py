import pandas as pd

# 1. Load the CSV into a DataFrame
df = pd.read_csv("NYC.csv")

# 2. (Optional) Do your data cleaning here...

# 3. Save directly to Parquet
df.to_parquet("NYC.parquet", engine="pyarrow")

print("Conversion complete!")
