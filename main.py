import csv
import numpy as np

with open("titanic1.csv", "r") as file:
  # ADD CODE: Convert titanic1.csv
  data = csv.reader(file,delimiter=",")
  headers = next(data)
  data_list = list(data)
  titanic_data1 = np.array(data_list)

# ADD CODE: Convert titanic2.csv 
  with open("titanic2.csv", "r") as file:
    # ADD CODE: Convert titanic2.csv
    data = csv.reader(file,delimiter=",")
    headers = next(data)
    data_list = list(data)
    titanic_data2 = np.array(data_list)

# ADD CODE: Merge two datasets
combined_data = np.concatenate((titanic_data1, titanic_data2), axis=0)

# ADD CODE: Print out shape and number of dimensions of merged dataset
print(combined_data.shape)
print(combined_data.ndim)

#Transform the Numpy array back into a regular list
listify = combined_data.tolist()

#Empty list to store the data once it's made into a string
titanic_lists_to_string = []

#Loop through the list of lists
for titanic_lists in listify:
  #Specify the delimeter between the data and use join to    convert the data into a string
  titanic_string = (",").join(titanic_lists)
  titanic_lists_to_string.append(titanic_string)

#transform the NumPy array, which is now stored in titanic_lists_to_string, into a string
complete_titanic = ("\n").join(titanic_lists_to_string)