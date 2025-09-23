# BELGICA-LAWRENCE-NATHAN-DC.--PA_3


#Pandas Exercises – Cars Dataset  

This repository contains solutions for two problems using **Python Pandas** to manipulate and analyze a dataset of cars (`cars.csv`).  

The purpose of this assignment is to practice data manipulation and extraction using Pandas, focusing on subsetting, slicing, and indexing operations with the Cars dataset (`cars.csv`).
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


#### 1. Import Pandas and Load Dataset
```python
import pandas as pd
```
→ Imports the Pandas library for handling tabular data.

```python
cars = pd.read_csv('cars.csv')
``` 
→ Loads the `cars.csv` file into a DataFrame named `cars`.

### 2. Row Containing "Mazda RX4"

**Goal:**  
Display the row of the DataFrame where the Model is `Mazda RX4`.

**Process:**  
Use `.loc[]` to filter rows where the column `Model` is `Mazda RX4`.

**Code Snippet:**
```python
print(cars.loc[cars['Model'] == 'Mazda RX4'])
```
→ `.loc[]` is used to select rows where the `Model` column equals `"Mazda RX4"`.
### 3. Cylinders of "Camaro Z28"

**Goal:**  
Find out how many cylinders (`cyl`) the car model `Camaro Z28` has.

**Process:**
- Use `.loc[]` to filter the row where the model is `Camaro Z28`.
- Select only the `'cyl'` column.

**Code Snippet:**
```python
print(cars.loc[cars['Model'] == 'Camaro Z28', ['cyl']])
```

### 4. Cylinders and Gears of Selected Models

**Goal:**  
Determine how many cylinders (`cyl`) and what gear type (`gear`) the following car models have:

- Mazda RX4  
- Ford Pantera L  
- Honda Civic  

**Process:**
- Create a list of selected models.  
- Use `.isin()` to filter rows where the model matches the list.  
- Display only `'cyl'` and `'gear'` columns.  

**Code Snippet:**
```python
cars_model = ['Mazda RX4', 'Ford Pantera L', 'Honda Civic']
print(cars.loc[cars['Model'].isin(cars_model), ['cyl', 'gear']])
```

## How to Run the Programs  

1. Ensure the dataset **`cars.csv`** is in the same folder as the Python files.  
2. Run each script using:  

```python
   python Surname_Pandas-P1.py
   python Surname_Pandas-P2.py
```
Check the terminal for outputs:

- Problem 1: Displays the first and last 5 rows of the dataset.
- Problem 2: Displays results for Mazda RX4, Camaro Z28, and selected models.


