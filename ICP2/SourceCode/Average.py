#Program to find the Average of given Plants
n=int(input("enter the number of plants"))
sum=0
x=input()
num=x.split()
for i in num:
    sum=sum+int(i)
print(round(sum/n,3))