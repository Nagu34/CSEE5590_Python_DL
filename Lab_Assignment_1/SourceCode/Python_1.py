#Write a program that computes the net amount of a bank account based a transaction log from console input.
Q='y'
#Enter the input transaction wether deposit or withdraw.
#here it takes input transaction and add it to netamount
def Transaction(Transactions,net_amount):
    if Transactions[0][0].lower()=='d':
        #print("Deposit")
        #adding amount
        net_amount+=int(Transactions[1])
        return net_amount
    elif Transactions[0][0].lower()=='w':
        #print("withdraw")
        #deleting amount
        net_amount-=int(Transactions[1])
        return net_amount
    else:
        pass
net_amount=0
#here run the loop untill you enter quit
while(Q!='n'):
    Transactions=input("ENter the Transactions")
    Transactions=Transactions.split(" ")
    #print(Transactions)
    #pass tghe function
    net_amount=Transaction(Transactions,net_amount)
    Q=input("TO continue transactions Enter y or else type n \n ")
print("Total amount:$",net_amount)
