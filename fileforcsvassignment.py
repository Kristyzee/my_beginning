import csv
import os

# fields=["Name", "Age","Gender"]

# filename=input("enter name  of csv file you wish to create or append to: ")
# fileexists= os.path.isfile(filename)
# if not filename.endswith('.csv'):
#     print("filename does not apply")
    
#     # filename+=".csv"
# fieldnames=fields
# def user_data():
#     Name= input("enter your name and surname respectively: ")
#     Age=int(input('enter your age: '))
#     Gender=input("enter your Gender; Male(M) or Female(F): ")
#     # return{f'Name: {Name} Age:  {Age} Gender: {Gender}'}
  

# with open(filename, "a" , newline='') as csvfile:
#     csvwriter=csv.writer(csvfile)
#     # csvwriter.writerow(fields)
#     csvwriter.writerow(user_data())
# print("userdetails has been successfully added")




# TUTORS WAY

import os
import csv

# Define column names
column_names = ["name", "age", "sex"]

# Get filename from user
filename = input("Enter the name of the CSV file: ") + ".csv"

# Check if file exists
if os.path.exists(filename):
    mode = "a"  # Append mode
    print("File already exists. Appending data.")
else:
    mode = "w"  # Write mode
    print("File created successfully.")

# Open file in specified mode
with open(filename, mode, newline="") as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=column_names)