


#--------------------------------------------------------RGHT ANGLE TRIANGLE--------------------------------------------------------------
# def print_triangle(n):
#     for i in range(n):
#         print('' * (n-i-1) + "*"  * (1* i +1))
# print_triangle(5)
#-----------------------------------------NORMAL TRIANGLE-----------------------------------------------------------------

# def print_triangle(n):
#     for i in range(n):
#         print(' ' * (n - i - 1) + ' * ' * (2 * i + 1))

# print_triangle(5)


#-----------------------------------------INVERTED TRIANGLE---------------------------------------------------------------------------


# def print_inverted_triangle(n):
#     for i in range(n):
#         print(' ' * i + '*' * (2 * (n - i - 1) + 1))

# print_inverted_triangle(5)


#------------------------------------------------DOUBLE UP $ DOWN TRIANGLE------------------------------------------------------------------


# def print_double_triangle(n):
#     # Upper triangle
#     for i in range(n):
#         print(' ' * (n - i - 1) + '*' * (2 * i + 1))
    
#     # Lower triangle
#     for i in range(n-2, -1, -1):
#         print(' ' * (n - i - 1) + '*' * (2 * i + 1))

# print_double_triangle(5)


#------------------------------INVERTED $ NORMAL TRIANGLE TOGETHER---------------------------------------------------------------------------------

# def print_inverted_triangle(n):
#     for i in range(n):
#         print(' ' * i + '*' * (2 * (n - i - 1) + 1))

# print_inverted_triangle(5)

# def print_triangle(n):
#     for i in range(n):
#         print(' ' * (n - i - 1) + '*' * (2 * i + 1))

# print_triangle(5)


#-----------------------------------------INVERTED RIGHT ANGLE TRIANGLE-----------------------------------------------------------

# def print_inverted_right_triangle(n):
#     for i in range(n, 0, -1):
#         print('*' * i)

# print_inverted_right_triangle(5)

#-----------------------------------DOUBLE NORMAL TRIANGLE---------------------------------------------

# def print_double_triangle(n):
#     for i in range(n):
#         print(' ' * (n - i - 1) + '*' * (2 * i + 1) +  '  ' * (n - i - 1) + '*' * (2 * i + 1))

# print_double_triangle(5)

#---------------------------------------right side triangle--------------------------------------------


# def print_triangle(n):
#     for i in range(n):
#         print('' * (n-i-2) + " * "  * (1* i +2))
# print_triangle(5)

# def print_inverted_right_triangle(n):
#     for i in range(n, 0, -1):
#         print(' * ' * i)

# print_inverted_right_triangle(5)


#---------------------------------------LEFT SIDE TRIANGLE----------------------------------

# def print_triangle(n):
#     for i in range(n):
#         print(' ' * (n-i-1+1) + "*"  * (1* i +1))
# print_triangle(5)

# def print_triangle(n):
#     for i in range(n,0,-1):
#         print(' ' * (n-i-1+1) + "*"  * (1 * i +1))
# print_triangle(5)


#------------------------------------SQUARE---------------------------------
#for i in range (5), it starts counting from 0 to 4 and it gives you 5 iteration
#but i in range(5),(15); it starts from 5 and ends in 14.

# for i in range(5):
#     for j in range(3):
#         print('* ', end= '')
#     print()


#################### RIGHT ANGLE TRIANGLE##############################

# for i in range(5):
#     for j in range(i + 1):
#         print('* ', end= " ")
#     print()
#################INVERTED RIGHT ANGLE TRIANGLE###########################
#i is rows, j is column
# def inv_right_angle(n):
#     for i in range(n):
#         for j in range(n-i):
#             print("* ", end= " ")
#         print()
# my_num=int(input("enter the number of rows: "))
    
# inv_right_angle(my_num)


######################### RIGHT INVERTED TRIANGLE###################

# def right_aligned_triangle(n):
#     for i in range(1, n + 1): #ROWS
#         for j in range(n - i):  #EMPTY SPACES
#             print("    ", end='')
#         for k in range(i):  #COLUMNS
#             print('*   ', end="")
#         print()
# my_num=int(input("enter the number of rows: "))
# right_aligned_triangle(my_num)


#################################### INVERTED RIGHT ALIGNED TRIANGLE############


# def inverted_right_aligned_triangle(n):
#     for i in range(n,0,- 1): #ROWS
#         for j in range(n - i):  #EMPTY SPACES
#             print("    ", end='')
#         for k in range(i):  #COLUMNS
#             print('*   ', end="")
#         print()
# my_num=int(input("enter the number of rows: "))
# inverted_right_aligned_triangle(my_num)

# def right_triangle(n):
#     for i in range(n):
#         for j in range(i + 1):
#             print('* ', end= " ")
#     print()
# my_num=int(input("enter the number of rows: "))
# right_triangle(my_num)








#ASSIGNMENT
# def hour_glass(n):
#     for i in range(0, n + 1):
#         for j in range(n + i):
#             print("  ",end="")
#         for k in  range(n-i):
#             print("  *  ", end="")
#         print()
            
#     for i in range(2, n + 1):
#         for j in range(n - i):
#             print("  ", end="")
#         for k in range(i):
#             print("  *  ", end="")
#         print()
# my_num=int(input("enter the number of rows: "))
# hour_glass(my_num)

# n = int(input("Enter the number of rows: "))
# for i in range(n, 0+1, -1):
#     for j in range(0, n-i):
#         print(end="  ")
#     for j in range(0, i):
#         print(" * ", end=" ")
#     print()
    
# for i in range(0, n):
#     for j in range(0, n-i-1):
#         print(end="  ")
#     for j in range(0, i+1):
#         print(" * ", end=" ")
# print()



# def hour_glass(n):
#     for i in range(n):
#         print(' ' * i + '*' * (1 * (n - i - 1) + 1))

#     for i in range(n):
#         print(' ' * (n - i - 1) + '*' * (1 * i + 1))

# my_num=int(input("enter the number of rows: "))
# hour_glass(my_num)



# ############## PYRAMID ##############
def pyramid(n):
   for i in range(1,n+1):
      for j in range(n - i):
         print(' ', end="")
      for k in range(i):
         print(' *', end=" ")
   print()
my_num=int(input("enter the number of rows: "))
pyramid(my_num)

# #################### RIGHT ANGLE TRIANGLE##############################

# def right_triangle(n):
#     for i in range(n):
#         for j in range(i + 1):
#             print('* ', end= " ")
#         print()
# my_num=int(input("enter the number of rows: "))
# right_triangle(my_num)


# ######################### LEFT TRIANGLE###################

# def left_triangle(n):
#     for i in range(1, n + 1): #ROWS
#         for j in range(n - i):  #EMPTY SPACES
#             print("    ", end='')
#         for k in range(i):  #COLUMNS
#             print('*   ', end="")
#         print()
# my_num=int(input("enter the number of rows: "))
# left_triangle(my_num)


# ############# INVERTED PYRAMID ##########
# def inverted_pyramid(n):
#     for i in range(0, n+1):
#         for j in range(n+i):
#             print("  ",end=" ")
#         for k in  range(n-i):
#             print("  *  ", end= " ")
#         print()
# my_num=int(input("enter the number of rows: "))
# inverted_pyramid(my_num)


# ##################### DOUBLE PYRAMID ##########
# def double_pyramid(n):

#     for i in range(n):
#         print(' ' * (n - i - 1) + '*' * (2 * i + 1) +  '  ' * (n - i - 1) + '*' * (2 * i + 1))
# my_num=int(input("enter the number of rows: "))
# double_pyramid(my_num)


##################### INVERTED DOUBLE PYRAMID ##########
# def inverteddouble_pyramid(n):
#    for i in range(n):
#       print(' ' * i + '*' * (2 * (n - i - 1) + 1 + ' ' * i + '*' * (2 * (n - i - 1) + 1)))

# my_num=int(input("enter the number of rows: "))

# inverteddouble_pyramid(my_num)



# ############ DIAMOND #################################

# def diamond(n):
#     # pyramid
#     for i in range(n):
#        print(' ' * (n - i - 1) + '*' * (2 * i + 1))
    
#     # inverted pyramid
#     for i in range(n-2, -1, -1):
#         print(' ' * (n - i - 1) + '*' * (2 * i + 1)