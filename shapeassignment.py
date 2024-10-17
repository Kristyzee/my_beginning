name = input("What is your name: ")
print(f"Hi, {name}! Welcome to our channel!")
print("""
List of shapes available here:
1. Hourglass
2. Pyramid
3. Left Triangle
4. Right Triangle
5. Inverted Pyramid
6. Double Pyramid
7. Inverted Double Pyramid
8. Diamond
""")

while True:
    choice = input("Enter the shape name or number: ")
    if choice.isdigit() and 1 <= int(choice) <= 8:
        choice = int(choice)
        break
    elif choice.lower() in ["hourglass", "pyramid", "left triangle", "right triangle", "inverted pyramid", "double pyramid", "inverted double pyramid", "diamond"]:
        choice = choice.lower()
        break
    print("Invalid choice. Please try again.")

rows = int(input("Enter the number of rows: "))

if choice == 1 or choice == "hourglass":
    for i in range(rows):
        print(' ' * i + '*' * (2 * (rows - i - 1) + 1))

    for i in range(rows):
        print(' ' * (rows - i - 1) + '*' * (2 * i + 1))

elif choice == 2 or choice == "pyramid":
    for i in range(1, rows + 1):
        print('  ' * (rows - i) + '*' * (2 * i - 1))

elif choice == 3 or choice == "left triangle":
    for i in range(1, rows + 1):
        print(' ' * (rows - i) + '*' * i)

elif choice == 4 or choice == "right triangle":
    for i in range(1, rows + 1):
        print('*' * i)

elif choice == 5 or choice == "inverted pyramid":
    for i in range(rows):
        print(' ' * i + '*' * (2 * (rows - i - 1) + 1))

elif choice == 6 or choice == "double pyramid":
    for i in range(rows):
        print(' ' * (rows - i - 1) + '*' * (2 * i + 1) +  '  ' * (rows - i - 1) + '*' * (2 * i + 1))

elif choice == 7 or choice == "inverted double pyramid":
    for i in range(rows):
        print(' ' * i + '*' * (2 * (rows - i - 1) + 1) +' ' * i + '*' * (2 * (rows - i - 1) + 1))
       

elif choice == 8 or choice == "diamond":
    for i in range(rows):
        print(' ' * (rows - i - 1) + '*' * (2 * i + 1))
    for i in range(rows-2, -1, -1):
        print(' ' * (rows - i - 1) + '*' *(2 * i + 1))
        
else:
    print("wrong parameters entered")
