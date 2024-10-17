
#-----------------------------------------------------------------------------------------------------
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