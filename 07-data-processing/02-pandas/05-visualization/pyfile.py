import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May"],
    "Sales": [100, 120, 150, 130, 140],
    "Expenses": [80, 90, 100, 110, 95],
}

# Creating a DataFrame
df = pd.DataFrame(data)

# Displaying the DataFrame
print("DataFrame:")
print(df)
print()

