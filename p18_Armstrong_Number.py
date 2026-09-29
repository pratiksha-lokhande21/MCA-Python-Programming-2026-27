num = int(input("Enter an integer: "))

original = num
digits = 0
sum = 0

while num > 0:
    digits = digits + 1
    num = num // 10

num = original

while num > 0:
    digit = num % 10
    sum = sum + digit ** digits
    num = num // 10

if sum == original:
    print("Armstrong number")
else:
    print("Not an Armstrong number")