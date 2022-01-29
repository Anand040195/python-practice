temp=0
list=[23,45,65,90,45,23]
for i in range(len(list)):
    for j in range(i+1,len(list)):
        if list[i]>list[j] :
            temp=list[i]
            list[i]=list[j]
            list[j]=temp
        
print(list,end=" ") 