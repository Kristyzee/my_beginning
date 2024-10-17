#function to populate a list and make it a dictionary
import time
print("FIRST LIST")

a=[]
done = 'yes'

while True:
    userinput= input("enter a word ")
    print("are you done entering your input ")
    user=input("yes or no ")
    a.append(userinput)
    if user == done:
        break

print(a)
 
print("SECOND LIST")
b=[]
done = 'yes'

while True:
    userinput= input("enter a word ")
    print("are you done entering your input ")
    user=input("yes or no ")
    b.append(userinput)
    if user == done:
        break

print(b)
 
if len(a) != len(b):
        print("length of lists don't match")

else:
        print("lengths match. Proceeeding...")
        print(".")
        
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print("KEY:",a)
        print("Value:",b)
        my_dict= dict(zip(a,b))
        print("my dictionary:",my_dict)
        
        
  