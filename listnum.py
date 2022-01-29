count=0
list=[23,45,56,90,77]
num=int(input("enter number"))
for i in list:
    if num==i:
        count=count+1
if count!=0:
    print("yes")
else:
    print("no")