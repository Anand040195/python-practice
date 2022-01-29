max=0
smax=0
for i in range(6):
    n=int(input("Enter your value"))  
    if max<n:          
        smax=max       
        max=n         
    elif smax<n:       
        smax=n          
print("Max value: ",max)
print("Second Max value: ",smax)
