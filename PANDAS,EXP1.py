import pandas as pd

data = {
    'Name': ['Arun', 'Divya', 'Kumar', 'Meena'],
    'Age': [22, 21, 23, 20],
    'Salary': [25000, 30000, 28000, 26000]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

print("\nSelected Column:")
print(df['Name'])

print("\nFiltered Data (Age > 21):")
print(df[df['Age'] > 21])

df['Bonus'] = df['Salary'] * 0.1
print("\nAfter Adding Bonus Column:")
print(df)