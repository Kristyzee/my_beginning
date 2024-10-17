def add(b,c):
    return b+c
    
def substract(b,c):
    return b-c
    
def multiply(b,c):
    return b*c
    
def divide(b,c):
    if c !=0:
        return b/c
    else:
        return "Error! division by zero"
        
# my_dict=dict(zip(add,substract,multiplication,division))
# print("my dictionary:",my_dict)

operations={
"+'": add,
"-": substract,
"*": multiply,
"/": divide
}


def calculator():
    num1 = float(input("enter the float nummber: "))
    num2 = float(input("enter the second number: "))
    operation = input("enter an operation (+,-,*,/): ")
    
    if operation in operations:
        result= operations[operation](num1, num2)
        print(f"{num1} {operation} {num2} = {result}")
    else:
        print('invalid operator')
    
calculator()