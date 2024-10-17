# name = input("Enter your name: ")  
# print(f"Hello {name}, welcome!\n")
# print("What shape would you like to print?")

# shapes = [
#     "1. Hour Glass",
#     "2. Pyramid",
#     "3. Right triangle",
#     "4. Left triangle",
#     "5. Inverted Pyramid",
#     "6. Double Pyramid",
#     "7. Inverted double Pyramid",
#     "8. Diamond"
# ]

# # Print the shapes list
# for shape in shapes:
#     print(shape)

# response = input("Enter correct shape name or index number: ").capitalize()

# if "Hour-Glass" in response or "1" in response:
#     n = 8
#     # Printing the Hour-Glass shape
#     for i in range(1, n):
#         print(' ' * i + '* ' * (n - i))
#     for i in range(n - 1, 0, -1):
#         print(' ' * i + '* ' * (n - i))

# elif "Pyramid" in response or "2" in response:
#     n = int(input(f"What size should your Pyramid be: "))
#     # Printing the Pyramid shape
#     for i in range(1, n + 1):
#         print(' ' * (n - i) + '*' * (2 * i - 1))

# elif "Left Triangle" in response or "4" in response:
#     n = int(input(f"What size should your Left Triangle be: "))
#     # Printing the Left Triangle shape
#     for i in range(1, n + 1):
#         print('* ' * i)

# elif "Right Triangle" in response or "3" in response:
#     n = int(input(f"What size should your Right Triangle be: "))
#     # Printing the Right Triangle shape
#     for i in range(1, n + 1):
#         print(' ' * (n - i) + '* ' * i)

# elif "Inverted Pyramid" in response or "5" in response:
#     n = int(input(f"What size should your Inverted Pyramid be: "))
#     # Printing the Inverted Pyramid shape
#     for i in range(n, 0, -1):
#         print(' ' * (n - i) + '*' * (2 * i - 1))

# elif "Double Pyramid" in response or "6" in response:
#     n = int(input(f"What size should your Double Pyramid be: "))
#     # Printing the Double Pyramid shape
#     for i in range(1, n + 1):
#         print(' ' * (n - i) + '*' * (2 * i - 1) + ' ' * (2 * (n - i)) + '*' * (2 * i - 1))

# elif "Inverted Double Pyramid" in response or "7" in response:
#     n = int(input(f"What size should your Inverted Double Pyramid be: "))
#     # Printing the Inverted Double Pyramid shape
#     for i in range(n, 0, -1):
#         print(' ' * (n - i) + '*' * (2 * i - 1) + ' ' * (2 * (n - i)) + '*' * (2 * i - 1))

# elif "Diamond" in response or "8" in response:
#     n = int(input(f"What size should your Diamond be: "))
#     # Printing the Diamond shape
#     for i in range(1, n + 1):
#         print(' ' * (n - i) + '*' * (2 * i - 1))
#     for i in range(n - 1, 0, -1):
#         print(' ' * (n - i) + '*' * (2 * i - 1))

# else:
#     print("Invalid shape selection.")

######IMPORTING FILES
from file import add

i=3
l=4
add(i,l)