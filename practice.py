import sqlite3
import pandas as pd

conn = sqlite3.connect('data.sqlite')

# product_data = pd.read_sql("""
# SELECT *
#   FROM products;
# """, conn)

# print(product_data)

# #1: Select the product name and product code for the last 5 products.
# product_name_and_code = pd.read_sql("""
# SELECT productName, productCode
#   FROM products;
# """, conn).tail()

# print(product_name_and_code)

# #2: Switch the order of the columns, i.e., show the product code first and then the product name for last  5 products
# product_code_and_name = pd.read_sql("""
# SELECT productCode, productName
#   FROM products;
# """, conn).tail()

# print(product_code_and_name)

# #3: Select the product name and product line. When the product line is "Planes", keep it as "Planes"; otherwise, have it as "Not Planes".Call this new column "Planes”.

# products_by_line = pd.read_sql(""" 
# SELECT productName, productLine,
# 		CASE
#     WHEN productLine = "Planes" THEN "Planes"
# 	  ELSE "Not Planes"
# 		END AS planes
# 	FROM products;
# """, conn)

# print(products_by_line)

# #4:Find the length of the product description for each product.Call this new column description_length.Show the first five rows of data. 
# product_description_lengths = pd.read_sql(""" 
# SELECT length(productDescription) AS description_length
#   FROM products;
# """, conn).head()

# print(product_description_lengths)

# #5:Change the product vendor to all caps.Call this new column caps_vendor.Show the first five rows.

# product_all_caps_vendors = pd.read_sql(""" 
# SELECT upper(productVendor) AS caps_vendor
#   FROM products;
# """, conn).head()

# print(product_all_caps_vendors)

# #6:Change the product name to all lowercase.Use lower() as you did upper().Call this new column lower_name.Show the first five rows.

# product_all_names_lower = pd.read_sql(""" 
# SELECT lower(productName) AS lower_name
#   FROM products;
# """, conn).head()

# print(product_all_names_lower)

# #7: Since all of the product scales are 1:xxx, we can take a substring of just the number following the colon.The first character following the colon is the third character.None of the scales are more than 1 to a three-digit number.
# product_scales = pd.read_sql(""" 
# SELECT substr(productScale, 3, 3) AS non 
# FROM products;
# """, conn)

# print(product_scales)

# #8:Create a new column fullName that has the product vendor followed by the product name, with a space between.For example, Min Lin Diecast 1969 Harley Davidson Ultimate Chopper.

# product_with_vendors = pd.read_sql(""" 
# SELECT productVendor || " " || productName AS fullName							
# From products;
# """, conn)

# print(product_with_vendors)

# #9: Find the difference in price between the MSRP and the buy price.Round the difference to the nearest whole number, i.e., as an integer, not floating point.Call this new column round_diff.
# rounded_price_diffs = pd.read_sql("""
# SELECT CAST(round(MSRP - buyPrice) AS INTEGER) AS round_diff
#   FROM products;
# """, conn)

# print(rounded_price_diffs)


#10: Close the connection when finished.
conn.close()