#program to do Queue operations using lists
MyQueue = []
QueueSize = int(input("Enter the QueueSize"))
Q = "y"


def DisplayQueue():
    print("Printing the entire Queue")
    for item in MyQueue:
        print(item)


def Enqueue(Value):
    if len(MyQueue) < QueueSize:
        MyQueue.append(Value)
    else:
        print("Stack is Full")


def Dequeue():
    if len(MyQueue) > 0:
        MyQueue.pop(0)
    else:
        print("Queue is full")


def Top():
    if len(MyQueue) > 0:
        print(MyQueue[0])
    else:
        print("Queue is empty")


while (Q != 'n'):
    x = int(input(
        "Enter the following numbers to do Queue Opereations:\n 1:Enqueue \n 2:Dequeue \n 3:Top \n 4:Display Queue"))
    if x == 1:
        print("Enqueue Operation-----")
        Enqueue(int(input("Enter the value to push")))
    elif x == 2:
        print("Dequeue Operation-----")
        Dequeue()
    elif x == 3:
        print("Printing Top of the Queue---")
        Top()
    elif x == 4:
        print("Display operation----")
        DisplayQueue()
    else:
        print("Entered invalid input")
    Q = input("Enter the y/n to continue the opeations y: To Continue \n n:To quit\n")
MyQueue.clear()

