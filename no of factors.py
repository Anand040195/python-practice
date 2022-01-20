n=0
x=int(input("Enter first value is:")) 
for i in range(1, x + 1):
    if x % i == 0:
        n += 1
print("no of factors :",n)