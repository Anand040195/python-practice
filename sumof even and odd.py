n=int(input("Enter n value"))
esum=0
osum=0
for i in range (1,n+1):
    if i%2==0:
        esum=esum+1
    else:
        osum=osum+1
print("sum of even number:",esum)
print("sum of odd number:",osum)