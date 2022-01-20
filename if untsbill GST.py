units=int(input("Enter unit"))
bill=0
if units<=50:
    bill=0.75*units
    print("bill value", bill)
    gst=(bill*10)/100
    bill=bill+gst
    print ("GST:",gst)
    print("final bill:",bill)
elif units<=150:
    bill=(50*0.75)+(units-50)*2.10
    print("bill value", bill)
    gst=(bill*10)/100
    bill=bill+gst
    print ("GST:",gst)
    print("final bill:",bill)
elif units<=250:
    bill=(50*0.75)+(100*2.10)+(units-150)*2.50
    print("bill value", bill)
    gst=(bill*10)/100
    bill=bill+gst
    print ("GST:",gst)
    print("final bill:",bill)
else:
    bill=(50*0.75)+(100*2.10)+(150*2.50)+(units-250)*2.80
    print("bill value", bill)
    gst=(bill*10)/100
    bill=bill+gst
    print ("GST:",gst)
    print("final bill:",bill)