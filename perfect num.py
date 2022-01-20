n=int=(input("Enter number:"))
sum=0
for i in range (1,n,1):
    if (n%i==0):
        sum=sum+i
if (sum==n):
    print(" number is perfect number")
else:
    print(" number is not perfect number")
