#program to do Stack operations using lists
MyStack = []
StackSize = int(input("Enter the stackSize"))
Q = "y"


def DisplayStack():
    print("Printing the entire stack")
    for item in MyStack:
        print(item)


def Push(Value):
    if len(MyStack) < StackSize:
        MyStack.append(Value)
    else:
        print("Stack is Full")


def Pop():
    if len(MyStack) > 0:
        MyStack.pop()
    else:
        print("Stack is full")


def Top():
    if len(MyStack) > 0:
        print(MyStack[-1])
    else:
        print("Stack is empty")


while (Q != 'n'):
    x = int(input("Enter the following numbers to do stack Opereations:\n 1:Push \n 2:Pop \n 3:Top \n 4:Display Stack"))
    if x == 1:
        print("Push Operation-----")
        Push(int(input("Enter the value to push")))
    elif x == 2:
        print("Pop Operation-----")
        Pop()
    elif x == 3:
        print("Printing Top of the Stack---")
        Top()
    elif x == 4:
        print("Display operation----")
        DisplayStack()
    else:
        print("Entered invalid input")
    Q = input("Enter the y/n to continue the opeations y: To Continue \n n:To quit\n")
MyStack.clear()
