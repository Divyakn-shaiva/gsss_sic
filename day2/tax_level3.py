import tax_level2 as t2
employee_tax = int(input("Enter the Tax you are paying :  "))
section_87A_rebate=0
tax_percentage = 0
if employee_tax >= 0 and employee_tax <= 300000:
    tax_percentage = 0
elif  employee_tax <= 600000:
     tax_percentage = 5
elif employee_tax <= 900000:
    tax_percentage = 10
elif employee_tax <= 1200000:
    tax_percentage = 15
elif employee_tax <= 1500000:
     tax_percentage = 20
else:
    tax_percentage = 30
print("Will you come under the section 87A rebate? (1. yes, 2. No)")


    
