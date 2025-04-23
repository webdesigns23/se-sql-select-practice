# Practice: Selecting Data with SQL

## Introduction

Understanding how to select data with SQL is a crucial skill when working with databases.
<br /><br />
Imagine you're working with a large e-commerce database containing millions of customer transactions. Your task is to analyze customer purchasing behavior to inform marketing strategies. Using SQL's SELECT statement, you can efficiently extract specific information from this vast dataset. For instance, you might want to retrieve the total amount spent by each customer in the last quarter, focusing only on those who made purchases exceeding $500. SQL allows you to precisely define these criteria, filtering and aggregating data from various tables to obtain the exact insights you need.
<br /><br />
This ability to select, filter, and summarize data is fundamental to deriving meaningful insights and forms the foundation for more complex tasks.

## Tools & Resources

- [GitHub Repo](https://github.com/learn-co-curriculum/se-sql-select-practice)

## Instructions

Run `pipenv install`, `pipenv shell`, and `python3 practice.py` to run the file and get started.

```python
# practice.py

import sqlite3
import pandas as pd

conn = sqlite3.connect('data.sqlite')

product_data = pd.read_sql("""
SELECT *
  FROM products;
""", conn)

print(product_data)
```

### Step 1

* Select the product name and product code for the products.
* Show the last five products.

### Step 2

* Switch the order of the columns, i.e. show the product code first and then the product name.
* Show the last five products.

### Step 3

* Select the product name and product line.
    * When the product line is "Planes" keep it as "Planes", otherwise have it as "Not Planes."
    * Call this new column "Planes.”

### Step 4

* Find the length of the product description for each product.
    * Call this new column "description_length."
    * Show the first five rows of data.

### Step 5

* Change the product vendor to all caps.
    * Call this new column "caps_vendor."
    * Show the first five rows.

### Step 6

* Change the product name to all lowercase.
    * Use lower() as you did upper().
* Call this new column "lower_name."
* Show the first five rows.

### Step 7

* Since all of the product scales are 1:xxx, we can take a substring of just the number following the colon.
* The first character following the colon is the third character.
* None of the scales are more than 1 to a three digit number.

### Step 8

* Create a new column "fullName" that has product vendor followed by the product name with a space between.
    * For example, Min Lin Diecast 1969 Harley Davidson Ultimate Chopper.

### Step 9

* Find the difference in price between the MSRP and the buy price.
* Round the difference to the nearest whole number, i.e. as an integer, not floating point.
* Call this new column "round_diff."

***Hint: These should all be positive values.*** 

### Step 10

Close the connection when finished.

## Solution

When you're done, check the lesson in Canvas for the solution.