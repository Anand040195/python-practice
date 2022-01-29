bs=float(input("enter basic salary:"))

if bs<10000:
    DA=(70*bs)/100
    HRA=(65*bs)/100
    gs=bs+DA+HRA
    print("gross salary:",gs)
if bs>=10000 and bs<=20000:
    DA=(75*bs)/100
    HRA=(73*bs)/100
    gs=bs+DA+HRA
    print("gross salary:",gs)
else:
    DA=(80*bs)/100
    HRA=(76*bs)/100
    gs=bs+DA+HRA
    print("gross salary:",gs)