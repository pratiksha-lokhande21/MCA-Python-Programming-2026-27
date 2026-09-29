Units=float(input("Enter Your electricity unit:"))

if Units<=100:
    bill=Units*5
elif Units<=200:
    bill = (100*5)+((Units-100)*7)

else:
    bill = (100*5)+(100*7)+((Units-200)*10)

print("Electricity Bill:",bill)
