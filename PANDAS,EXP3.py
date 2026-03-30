import pandas as pd
import numpy as np

# Create two DataFrames [cite: 82, 86]
df1 = pd.DataFrame({
    'Name': ['Arun', 'Divya'],
    'Age': [22, 21]
})

df2 = pd.DataFrame({
    'Name': ['Kumar', 'Meena'],
    'Age': [23, 20]
})

print("DataFrame 1:")
print(df1)

# Reindexing to change row labels and expand the range [cite: 77, 92]
# Using np.nan instead of "NA" to keep data types consistent
df1_reindexed = df1.reindex(range(3)) 

print("\nReindexed DataFrame (with empty row):")
print(df1_reindexed)

# Combine DataFrames using concatenation [cite: 78, 95]
# ignore_index=True ensures the final list is numbered 0, 1, 2, 3, 4
combined = pd.concat([df1_reindexed, df2], ignore_index=True)

print("\nFinal Aligned and Combined Data:")
print(combined)