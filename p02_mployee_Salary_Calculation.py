Basic_Salary=float(input("Enter Your Salary:"))
DA=Basic_Salary*10/100
HRA=Basic_Salary*20/100
Gross_Salary=Basic_Salary+DA+HRA
Tax=Basic_Salary*5/100
Net_Salary=Gross_Salary-Tax

print("DA:",DA)
print("HRA:",HRA)
print("Gross Salary:",Gross_Salary)
print("Tax:",Tax)
print("Net salary:",Net_Salary)