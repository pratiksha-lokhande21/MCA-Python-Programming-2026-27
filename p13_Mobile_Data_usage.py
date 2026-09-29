data=float(input("Enter your  monthly data uses in GB:"))
if data <=2:
    bill = 199
elif data<=5:
    bill=199+(data-2)*20
elif data <=10:
    bill = 259+(data-5)*15
else:
    bill = 334+(data-10)*10

print("Data Usage:", data, "GB")
print("Total Bill: ₹", bill)