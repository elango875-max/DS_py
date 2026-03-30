import pandas as pd
import numpy as np # Standard practice to use numpy for NaN values

data = {
    'Name': ['Arun', 'Divya', np.nan, 'Meena'], # Use np.nan for clarity
    'Age': [22, np.nan, 23, 20],
    'Salary': [25000, 30000, np.nan, 26000]
}

df = pd.DataFrame(data)

# This line is correct for counting, but only if the data above uses np.nan or None
print("\nMissing Values Count:")
print(df.isnull().sum()) 

# FIX: In lines 59-61, avoid 'inplace=True' as it is being deprecated
df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Salary'] = df['Salary'].fillna(0)
df['Name'] = df['Name'].fillna("Unknown")