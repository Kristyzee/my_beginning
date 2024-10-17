import csv
import os

fields=["Name", "Age","Gender"]

filename=input("enter name  of csv file you wish to create or append to: ")
fileexists= os.path.isfile(filename)
if not filename.endswith('.csv'):
    print("filename does not apply")
    
    # filename+=".csv"
fieldnames=fields
Name= input("enter your name and surname respectively: ")
Age=int(input('enter your age: '))
Gender=input("enter your Gender; Male(M) or Female(F): ")
print(Name, Age, Gender)

with open(filename, "a" , newline='') as csvfile:
    csvwriter=csv.writer(csvfile,fieldnames==fields)
# if not fileexists:csvwriter.writeheader()
    csvwriter.writerows({"Name":Name, "Age":Age, "Gender":Gender})
