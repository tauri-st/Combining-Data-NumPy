import csv
import numpy as np

with open("titanic1.csv", "r") as file:
  # ADD CODE: Convert titanic1.csv
  data1 = csv.reader(file,delimiter=",")
  headers = next(data1)
  data_list = list(data1)

# ADD CODE: Convert titanic2.csv 


# ADD CODE: Merge two datasets


# ADD CODE: Print out shape and number of dimensions of merged dataset