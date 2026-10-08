import pandas as pd

existing = pd.read_parquet("NYC.parquet", engine="pyarrow")
new_rows = pd.read_csv("NYC_new.csv")  # or build a DataFrame however you like

combined = pd.concat([new_rows, existing], ignore_index=True)

combined.to_parquet(
    "NYC.parquet",
    engine="pyarrow",
    use_content_defined_chunking=True,
)
