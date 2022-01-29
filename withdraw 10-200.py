withdraw=int(input("Enter Amount"))
a=0
b=0
c=0
d=0
e=0
if withdraw%10==0:
    if withdraw>=200:
        a=withdraw//200
        withdraw=withdraw-(200*a)
        print("200 rupees notes are :",a)
    if withdraw>=100:
        b=withdraw//100
        withdraw=withdraw-(100*b)
        print("100 rupees notes are :",b)
    if withdraw>=50:
        c=withdraw//50
        withdraw=withdraw-(50*c)
        print("50 rupees notes are :",c)
    if withdraw>=20:
        d=withdraw//20
        withdraw=withdraw-(20*d)
        print("20 rupees notes are :",d)
    if withdraw>=10:
        e=withdraw//10
        print("10 rupees notes are :",e)
else:
    print("invalid")