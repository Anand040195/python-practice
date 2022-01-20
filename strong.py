n=int(input("Enter number:"))
tem=n
sum=0
while (n):
    i=1
    f=1
    r=n%10
    while(i<=r):
        f=f*i
        i=i+1
        sum=sum+f
        n= n//10
if (sum==tem):
    print(" number is strong")
else:
    print("number is not strong")