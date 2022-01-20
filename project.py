#Wap to accept project marks, internal marks and external marks and find total marks
# total marks= 70% from projet+20% from external+10% from intenal



project=int(input("project markes"))
internal=int(input("internal markes"))
external=int(input("external markes"))

Total_marks=(70*project+20*external+10*internal)/100

print("total marks:",Total_marks) 