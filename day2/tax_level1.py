#taxation problem
print("Employee Details")
employee_name = input("Enter a Employee Name:  ")
employee_id = int(input("Enter the Employee ID:  "))
employee_salary = int(input("Enter the Employe Monthly Basic Salary:  "))
special_allowances = int(input("Enter the Monthly Special allowances:  "))
bonus_percentage = int(input("Enter the Yearly bonus percentage: "))
gross_monthly_salary = employee_salary + special_allowances
gross_annual_salary = ( gross_monthly_salary * 12 ) + bonus_percentage
print("Employee Name :", employee_name)
print("Employee ID:", employee_id)
print("Employee Basic Salary:" , employee_salary)
print("Employee Monthly Special Allowances:" , special_allowances)
print("Employee Bonus Percentage:" , bonus_percentage)
print("Employee Gross Monthly Salary:" , gross_monthly_salary)
print("Employee  Gross Annual Salary:",gross_annual_salary)
