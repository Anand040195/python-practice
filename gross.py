#WAP to accept basic and find gross
#gross= basic+da+hra
#da is 80% on basicsalary
#hra is 76% on basicsalary




basicsalary=float(input("Basic salary "))

DA=(basicsalary*80/100)
HRA=(basicsalary*76/100)

Gross_salary=basicsalary+DA+HRA

print("Gross salary:",Gross_salary)