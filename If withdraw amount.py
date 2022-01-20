withdraw=int(input("Enter Amount"))
a=0
b=0
c=0

if withdraw%100==0:
    if withdraw>=500:
        a=withdraw//500
        withdraw=withdraw-(500*a)
        print("500 rupees notes are :",a)
    if withdraw>=200:
        b=withdraw//200
        withdraw=withdraw-(200*b)
        print("200 rupees notes are :",b)
    if withdraw>=100:
        c=withdraw//100
        print("100 rupees notes are :",c)
else:
    print("invalid")