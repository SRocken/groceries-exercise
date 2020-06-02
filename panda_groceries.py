import operator

import pandas

import os

csv_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "products.csv")

df = pandas.read_csv(csv_filepath)
print(df.head())

products = df.to_dict("records")

#Approach A
#products = []
#for row in ______
#    products.append()

#Approach B
products = df.to_dict("records")

print("--------------")
print("THERE ARE", len(products), "PRODUCTS:")
print("--------------")

def sort_by_name(p):
    return p["name"]

def to_usd(my_price):
    return f"${my_price:,.2f}"

sorted_products = sorted(products, key=sort_by_name)

for p in sorted_products:
    price_usd = (" " + to_usd(p["price"]))
    print(" + " + p["name"] + price_usd)


departments = []

for p in products: #loop through the contents of an existing list to form a new list
    departments.append(p["department"])
unique_departments = list(set(departments))

print("--------------")
print("THERE ARE", len(departments), "DEPARTMENTS:")
print("--------------")

unique_departments.sort()

for d in unique_departments:
    matching_products_count = [p for p in products if p["department"] == d]
    matching_products_count = len(matching_products_count)
    if matching_products_count > 1:
        label = "products"
    else:
        label = "product"
    print(" + " + d.title() + " (" + str(matching_products_count) + " " + label +")")
