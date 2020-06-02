import pandas
import os

#csv_filepath = "data/products.csv"
csv_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "products.csv")

df = pandas.read_csv(csv_filepath)
print(df.head())

products = df.to_dict("records")

