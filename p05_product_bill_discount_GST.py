price1 = float(input("Enter price of product 1: "))
quantity1 = int(input("Enter quantity of product 1: "))

price2 = float(input("Enter price of product 2: "))
quantity2 = int(input("Enter quantity of product 2: "))

price3 = float(input("Enter price of product 3: "))
quantity3 = int(input("Enter quantity of product 3: "))

subtotal = (price1 * quantity1) + (price2 * quantity2) + (price3 * quantity3)

discount = subtotal * 10 / 100

amount_after_discount = subtotal - discount

gst = amount_after_discount * 18 / 100

final_amount = amount_after_discount + gst

print("Subtotal =", subtotal)
print("Discount =", discount)
print("GST =", gst)
print("Final Payable Amount =", final_amount)