#program to do airthmetic operations
#input of two numbers
q='y'
def add(x,y):
    print("Adding two numbers: "+ str(x+y))
def minus(x,y):
    print("Subraction of two numbers: "+ str(abs(x-y)))
def multiplication(x,y):
    print("Multiplication  of two numbers: "+ str((x*y)))
def division(x,y):
    print("Division of two numbers: "+ str(round(x/y,3)))
while q!='n':
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter Second number: "))
    operation = int(input("Enter 1 for addition\n"
                           "Enter 2 for Subtraction\n"
                            "Enter 3 for multiplication\n"
                             "Enter 4 for division\n"))
    if operation==1:
        add(num1,num2)
    elif operation==2:
        minus(num1,num2)
    elif operation==3:
        multiplication(num1,num2)
    elif operation==4:
        division(num1,num2)
    q=input("Enter y : continue or n : quit ")




