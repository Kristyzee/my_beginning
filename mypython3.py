# def add(a, b):
# #     print(a + b)

#.......................................................CSV ASSIGNMNENT...................................................
import csv
import os


filename = input("Enter filename: ")
check = os.path.exists(filename)
fields = ["Name", "Age", "Gender"]
if check == True:
    print(f"{filename} exists \n Proceeding...")
    Name = input("Please Enter your Name: ")
    Age = int(input("Please enter your Age in digits: "))
    Gender = input("Please enter your Gender: ")
    
    rows = [Name, Age, Gender]
    with open(filename, "a") as myfile:
        # Create the CSV writer object
        mywriter = csv.writer(myfile)
        #Write Header and Rows
        # mywriter.writerow(fields)
        mywriter.writerow(rows)
    print(f"Your Biodata have been succesfully appended to {filename}")
        
elif check == False:
    print(f"{filename} is being created")
    
    mydict = {"Name": "", "Age":"", "Gender":""}
    Name = input("Please Enter your Name: ")
    Age = int(input("Please enter your Age in digits: "))
    Gender = input("Please enter your Gender: ")

    mydict["Name"] = Name
    mydict["Age"] = Age
    mydict["Gender"] = Gender

    with open(filename, "w+") as file:
        #Create the CSV dict writer Object
        csvwriter = csv.DictWriter(file, fieldnames= fields)
        # Write Headers
        csvwriter.writeheader()
        # Write Rows
        csvwriter.writerow(mydict)
    print(f"{filename} has been created and biodata have been succesfully uploaded")
     











    


