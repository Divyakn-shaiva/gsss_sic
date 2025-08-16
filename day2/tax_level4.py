import tax_level1 as t1 
import tax_level3 as t3
net_annual_salary=t1.gross_annual_salary - t3.total_tax_amount
print("Employee Annual Salary " , t1.gross_annual_salary)
print("Net Annual Salary " , net_annual_salary)