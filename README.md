# BELGICA-LAWRENCE-NATHAN-DC.--PA_3


#Pandas Exercises – Cars Dataset  

This repository contains solutions for two problems using **Python Pandas** to manipulate and analyze a dataset of cars (`cars.csv`).  

---

## Problem 1: `Surname_Pandas-P1.py`  

### Task 
1. Load the `cars.csv` file into a Pandas DataFrame named `cars`.  
2. Display the **first five** and **last five** rows of the DataFrame.  

### Code  
```python
import pandas as pd

# Load dataset
cars = pd.read_csv('cars.csv')

# Display first 5 rows
print(cars.head())

# Display last 5 rows
print(cars.tail())
