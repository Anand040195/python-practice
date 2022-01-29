list=[23,45,65,90,45,23]
for i in range(6):
    for j in range(i+1,6):
        if list[i]==list[j]:
            print(list[i],end=" ")
            