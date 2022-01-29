count1=1
count=0
for i in range (5):
    for j in range(5):
        if i%2==0:
            print(count1,end=" ")
            count1=count1
        else:
            print(count,end=" ")
            count=count
    print()