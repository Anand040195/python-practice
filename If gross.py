basicsalary=int(input("Basic salary "))

if basicsalary<10000:
    DA=(basicsalary*70/100)
    HRA=(basicsalary*65/100)
    Gross_salary=basicsalary+DA+HRA
    print("gross sala:",Gross_salary)
elif basicsalary>10000 and basicsalary<20000:
    DA=(basicsalary*75/100)
    HRA=(basicsalary*73/100)
    Gross_salary=basicsalary+DA+HRA
    print("gross sala:",Gross_salary)
else:
    DA=(basicsalary*80/100)
    HRA=(basicsalary*76/100)
    Gross_salary=basicsalary+DA+HRA
    print("gross sala:",Gross_salary)
    

