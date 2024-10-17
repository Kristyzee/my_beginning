# def my_function(fname, lname):
#     print(fname + '' + lname)

# my_function("ADAMAWA ", 'YOLA')


#code to show that diferent prompts(words) can added to different function in a function
# def my_function(fname):
#     print("" +fname + " kayode")
    
# my_function("hello Ayo")
# my_function("hi Olamide")
# my_function("hey Fashola")

#  my_function()

# def my_function(fname):
#         print("hello " + fname + " Okoronkwo")
        
# my_function("favour")
# my_function("victory")
# my_function("david")
            

#code (1) to prompt the printing of a factorial
# import math

# n=int(input("enter a number:"))
## check if n is negative
# if n<0:
#     print("sorry wrong parameters entered")
#     print("program terminated")
# else:
#     print("the factorial of", n,  "is")
#     print(math.factorial (n))


#code (2) to prompt the printing of a factorial
# n=int(input("enter a number:"))
# if n<0:
#     print("sorry wrong parameters entered")
#     print("program terminated")
# elif n==0:
#     print("the factorial of 0 is 1") 
# else:
#     print("the factorial of", n,  "is")
#     print(math.factorial (n))



#code (3) to prompt the printing of a factorial


# def recur_factorial(n):
#     if n==1:
#         return n
#     else:
#         return n*recur_factorial(n-1)
# num =int(input("enter an integer:"))
# if num < 0: 
#     print("sorry, factorial does not existt for negative numbers") 
# elif num ==0:
#        print("the fcatorial of 0 is 1")
# else:
#     print("the factorial of", num, "is",recur_factorial (num))



# #code (4) to prompt the printing of a factorial
# n=int(input("enter an integer:"))
# factorial = 1
# if n<0:
#     print("sorry wrong parameters entered")
#     print("program terminated")
#     if n==0:
#         print('factorial of 0 is 1')
#     else:
#         for i in range (1,n+1):
#             factorial=factorial *i
#         print("factorial of the given number is:",factorial)




# ##code to print the calenders of a year-----------   1  --------------
import calendar

# x="year"
# x=int(input('enter the calendar year:'))
# print(calendar.calendar(x))

# ##----(ASS 2)-----------code to print the calendar of a particular month either in monthname or month number------------------
# x="year"
# y="month"

# x=int(input('enter the calendar year:'))

# print("1. January")
# print("2. February")
# print("3. March")
# print("4. April")
# print("5. May")
# print('6. June')
# print("7. July")
# print("8. August")
# print("9. September")
# print('10. October')
# print("11. November")
# print("12. December")

# y=int(input("enter the month(1-12):"))
# if y < 1 or y > 12:
#      print("inputed month number does not exist")
# else:
#      print(calendar.month(x,y))




# # #-------------------------------------------------------------  (2)    ------------------------------------------
# def print_calendar(year, month):
#     print(calendar.month(year, month))

# def main():
#     year = int(input("Enter a year: "))

#     while True:
#         month_input = input("Enter month name (e.g., January) or month number (e.g., 1): ")

#         try:
#             # Try to convert month name to month number
#             month = list(calendar.month_name).index(month_input.capitalize())
#         except ValueError:
#             try:
#                 # Try to convert month number to integer
#                 month = int(month_input)
#                 if month < 1 or month > 12:
#                     raise ValueError
#             except ValueError:
#                 print("Invalid month input. Please enter a valid month name or number.")
#                 continue

#         print_calendar(year, month)
#         break

# if __name__ == "__main__":
#     main()


#-----LEARNING TUTORIAL--------------------------------------2-------------------------------------

# num=int(input("enter the month(1-12):"))

# print("month number:" , num)
# print("month full name is: " , calendar.month_name [num])


##code to print calendar of a range of months-------------------  3   --------------

year=int(input('enter the calendar year:'))
print("1. January\n 2. February\n 3. March\n 4. April\n 5. May\n 6. June\n 7. July\n 8. August\n 9. September\n 10. October\n 11. November\n 12. December")
beginning_month= int(input("beginning month:" ))
stop_month=int(input("stop month:"))

for month in range(beginning_month, stop_month +1):
#      print(f"\n{calendar.month_name[month]}{year}\n")
#      print (calendar.month(year,month))
     print("\n", calendar.month(year,month))





#TRIALS



