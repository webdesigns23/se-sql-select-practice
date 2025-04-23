import sqlite3
import pandas as pd

conn = sqlite3.connect('data.sqlite')

product_data = pd.read_sql("""
SELECT *
  FROM products;
""", conn)

print(product_data)