n1=int(input("Enter n1 value"))
n2=int(input("Enter n2 value"))
n3=int(input("Enter n3 value"))

if n1>n2 and n1>n3:
    print("n1 is max:",n1)
elif n2>n1 and n2>n3:
    print("n2 is max:",n2)
else:
    print("n3 is max:",n3)