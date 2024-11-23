
#calender range

import calendar


def print_calendar_range():
try:
    year = int(input("Enter the year: "))
    start_month_input = input("Enter the starting month (name or number): ")
    end_month_input = input("Enter the ending month (name or number): ")

    # Convert start month input to integer if it's a number
    if start_month_input.isdigit():
        start_month = int(start_month_input)
    else:
        start_month = list(calendar.month_name).index(start_month_input.capitalize())

    # Convert end month input to integer if it's a number
    if end_month_input.isdigit():
        end_month = int(end_month_input)
    else:
        end_month = list(calendar.month_name).index(end_month_input.capitalize())

    # Print the calendar for each month in the range
    print(
        f"\nThe calender from {calendar.month_name[start_month]} to {calendar.month_name[end_month]} for the year {year} is:  "
    )
    for month in range(start_month, end_month + 1):
        # print("\n", calendar.month_name[month], year)
        # print(calendar.monthcalendar(year, month))
        print("\n", calendar.month(year, month))


print_calendar_range()

except:
# SHAPES ASSIGNMWENT
name = input("Enter your name: ")  
print(f"Hello {name}, welcome!\n")
print("What shape would you like to print?")

shapes = [
    "1. Hour Glass",
    "2. Pyramid",
    "3. Right triangle",
    "4. Left triangle",
    "5. Inverted Pyramid",
    "6. Double Pyramid",
    "7. Inverted double Pyramid",
    "8. Diamond"
]

# Print the shapes list
for shape in shapes:
    print(shape)

response = input("Enter correct shape name or index number: ").capitalize()

if "Hour-Glass" in response or "1" in response:
    n = 8
    # Printing the Hour-Glass shape
    for i in range(1, n):
        print(' ' * i + '* ' * (n - i))
    for i in range(n - 1, 0, -1):
        print(' ' * i + '* ' * (n - i))

elif "Pyramid" in response or "2" in response:
    n = int(input(f"What size should your Pyramid be: "))
    # Printing the Pyramid shape
    for i in range(1, n + 1):
        print(' ' * (n - i) + '*' * (2 * i - 1))

elif "Left Triangle" in response or "4" in response:
    n = int(input(f"What size should your Left Triangle be: "))
    # Printing the Left Triangle shape
    for i in range(1, n + 1):
        print('* ' * i)

elif "Right Triangle" in response or "3" in response:
    n = int(input(f"What size should your Right Triangle be: "))
    # Printing the Right Triangle shape
    for i in range(1, n + 1):
        print(' ' * (n - i) + '* ' * i)

elif "Inverted Pyramid" in response or "5" in response:
    n = int(input(f"What size should your Inverted Pyramid be: "))
    # Printing the Inverted Pyramid shape
    for i in range(n, 0, -1):
        print(' ' * (n - i) + '*' * (2 * i - 1))

elif "Double Pyramid" in response or "6" in response:
    n = int(input(f"What size should your Double Pyramid be: "))
    # Printing the Double Pyramid shape
    for i in range(1, n + 1):
        print(' ' * (n - i) + '*' * (2 * i - 1) + ' ' * (2 * (n - i)) + '*' * (2 * i - 1))

elif "Inverted Double Pyramid" in response or "7" in response:
    n = int(input(f"What size should your Inverted Double Pyramid be: "))
    # Printing the Inverted Double Pyramid shape
    for i in range(n, 0, -1):
        print(' ' * (n - i) + '*' * (2 * i - 1) + ' ' * (2 * (n - i)) + '*' * (2 * i - 1))

elif "Diamond" in response or "8" in response:
    n = int(input(f"What size should your Diamond be: "))
    # Printing the Diamond shape
    for i in range(1, n + 1):
        print(' ' * (n - i) + '*' * (2 * i - 1))
    for i in range(n - 1, 0, -1):
        print(' ' * (n - i) + '*' * (2 * i - 1))

else:
    print("Invalid shape selection.")
    
    
except:    
    #PRIME NUMBERS
    
n=int(input("enter the number you desire to derive it's prime numbers: "))
for num in range(n + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:

            print(num, end= '  ')
       
       
except:            
# PASSWORD GENERATOR
import string
import random
import array

length=int(input("enter password length: "))

DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']   
LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',  
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 
                     'z'] 
  
UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',  
                     'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q', 
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 
                     'Z'] 
  
SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',  
           '*', '(', ')', '<'] 
   
COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS 
  
# randomly select at least one character from each character set above 
rand_digit = random.choice(DIGITS) 
rand_upper = random.choice(UPCASE_CHARACTERS) 
rand_lower = random.choice(LOCASE_CHARACTERS) 
rand_symbol = random.choice(SYMBOLS) 
  
# helps to select only 4 passwords, one from each rand
temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol 
  
  
# selelcts the rest of the password 
for x in range(length - 4): 
    temp_pass = temp_pass + random.choice(COMBINED_LIST) 
  
    # convert temporary password into array and shuffle to  prevent it from having a consistent pattern 
    temp_pass_list = array.array('u', temp_pass) 
    random.shuffle(temp_pass_list) 
  
password = "" 
for x in temp_pass_list: 
        password = password + x 
print(password)
for word in range(password):
    random_word=".join(random.shuffle(temp_pass_list) for_in range(password)))"
    
print(random_word)

except:
#BULK RENAMER
import os

def renamer():
    
    path= input("Enter the file path you wish to rename: ")
    path=path.replace('\\', "/")
    path= path + "/"
    i=0
    for filename in os.listdir(path):
            my_source=path + filename
            my_dest= "PIC" + str(i) + ".png"
            my_dest=path + my_dest
        
            os.rename(my_source, my_dest)
            i += 1
    print("Success! you can now check your folder")
                      
                      
renamer()

except:
# CSV FILES

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
    
    
except:    
    #FABONACCI
def fibonacci():
   x,y=0,1
   while True:
      yield x
      x , y = y, x+y
n=int(input("how many fibonacci terms do you wish to run?: "))
print(f"number of first" , n , "fibonacci numbers is : ")
fib=fibonacci()
for _ in range(n):
   print(next(fib), end="  ")
fibonacci()

finally:
     # FACTORIAL
import math
n=int(input("enter a number:"))
if n<0:
    print("sorry wrong parameters entered")
    print("program terminated")
elif n==0:
    print("the factorial of 0 is 1") 
else:
    print("the factorial of", n,  "is")
    print(math.factorial (n))

