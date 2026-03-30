import matplotlib.pyplot as plt
#Working with NumPy Arrays
import numpy as np
# Creating a 1D NumPy array
array_1d = np.array([1, 2, 3, 4, 5])
print("1D Array:", array_1d)
# Creating a 2D NumPy array
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array:\n", array_2d)
# Array operations
print("Array shape:", array_2d.shape) # Shape of the array
print("Sum of all elements:", np.sum(array_2d)) # Sum of all elements
print("Mean of the array:", np.mean(array_2d)) # Mean of the array
print("Transposed Array:\n", np.transpose(array_2d)) # Transposing the array
# Indexing and slicing
print("First row of 2D array:", array_2d[0]) # Accessing first row
print("Element at row 1, column 2:", array_2d[1, 2]) # Specific element
print("Slicing:\n", array_2d[:, 1:]) # Slicing columns
#Working with Pandas DataFrames
import pandas as pd
# Creating a DataFrame from a dictionary
data = {
'Name': ['Alice', 'Bob', 'Charlie'],
'Age': [25, 30, 35],
'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)
print("DataFrame:\n", df)
# Basic DataFrame operations
print("DataFrame shape:", df.shape) # Shape of the DataFrame
print("Summary Statistics:\n", df.describe()) # Summary statistics of numerical columns
print("DataFrame Info:")
print(df.info()) # Information about the DataFrame
# Adding a new column
df['Salary'] = [50000, 60000, 70000]
print("Updated DataFrame:\n", df)
# Indexing and selecting data
print("Selecting 'Age' column:\n", df['Age']) # Selecting a column
print("Selecting first row:\n", df.iloc[0]) # Selecting a row by index
print("Filtering by Age > 28:\n", df[df['Age'] > 28]) # Filtering rows
#Basic Plots Using Matplotlib
# Sample data
x = np.linspace(0, 10, 100)
y = np.sin(x)
# Line Plot
plt.figure(figsize=(10, 5))
plt.plot(x, y, label='sin(x)', color='blue')
plt.title('Line Plot of sin(x)')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.grid(True)
plt.show()
# Bar Plot
categories = ['A', 'B', 'C']
values = [10, 20, 15]
plt.figure(figsize=(8, 5))
plt.bar(categories, values, color=['red', 'green', 'blue'])
plt.title('Bar Plot Example')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.show()
# Scatter Plot
x = np.random.rand(50)
y = np.random.rand(50)
plt.figure(figsize=(8, 5))
plt.scatter(x, y, color='purple')
plt.title('Scatter Plot Example')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()
# Histogram
data = np.random.randn(1000)
plt.figure(figsize=(8, 5))
plt.hist(data, bins=30, color='orange', edgecolor='black')
plt.title('Histogram Example')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()