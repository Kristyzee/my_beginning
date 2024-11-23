# def prime_numbers():
#     n = int(input("enter the number you desire to derive it's prime numbers: "))

#     prime_list = [x for x in range(2, n+1) if all(x % i != 0 for i in range(2, int(x**0.5) + 1))]

#     if prime_list:
#         print(prime_list)
#     else:
#         print("Error! No prime numbers associated with input")

# prime_numbers()
      


n=int(input("enter the number you desire to derive it's prime numbers: "))
for num in range(n + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:

            print(num, end= '  ')
            