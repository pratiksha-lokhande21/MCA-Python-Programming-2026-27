start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

count = 0

print("Prime numbers:")

for num in range(start, end + 1):
    if num < 2:
        continue

    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num)
        count = count + 1

print("Total prime numbers:", count)