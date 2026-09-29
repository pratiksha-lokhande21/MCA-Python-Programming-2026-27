correct_pin = 1234
balance = 10000

pin = int(input("Enter PIN: "))
amount = float(input("Enter withdrawal amount: "))

if pin != correct_pin:
    print("Invalid PIN")
elif amount <= 0:
    print("Invalid withdrawal amount")
elif amount > balance:
    print("Insufficient balance")
elif amount % 100 != 0:
    print("Amount must be in multiples of 100")
else:
    balance = balance - amount
    print("Withdrawal successful")
    print("Remaining balance:", balance)