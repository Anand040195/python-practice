Salary=float(input("Employ salary: "))

bill1=float(input("Spent for bill1:"))
bill2=float(input("Spent for bill2:"))
bill3=float(input("Spent for bill3:"))

total=bill1+bill2+bill3

per= (total*100/Salary)

print("total shopping bill:", total)
print("% of shopping bill :", per)
