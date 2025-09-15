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
```

## Problem 2: `Surname_Pandas-P2.py`

This script performs **data extraction and filtering** from the `cars.csv` dataset using **Pandas subsetting, slicing, and indexing**.

---

### Full Code

```python
import pandas as pd

# Load dataset
cars = pd.read_csv('cars.csv')

# a) Display the first five rows with odd-numbered columns (1, 3, 5, 7...)
print("a) First 5 rows with odd-numbered columns:\n")
print(cars.iloc[:5, ::2])

# b) Display the row that contains the 'Model' of 'Mazda RX4'
print("\nb) Row with Model 'Mazda RX4':\n")
print(cars.loc[cars['Model'] == 'Mazda RX4'])

# c) How many cylinders ('cyl') does the car model 'Camaro Z28' have?
print("\nc) Cylinders of Camaro Z28:\n")
print(cars.loc[cars['Model'] == 'Camaro Z28', ['cyl']])

# d) Determine how many cylinders ('cyl') and what gear type ('gear')
# do the car models 'Mazda RX4 Wag', 'Ford Pantera L', and 'Honda Civic' have
print("\nd) Cylinders and gear type of Mazda RX4 Wag, Ford Pantera L, Honda Civic:\n")
cars_model = ['Mazda RX4 Wag', 'Ford Pantera L', 'Honda Civic']
print(cars.loc[cars['Model'].isin(cars_model), ['cyl', 'gear']])
