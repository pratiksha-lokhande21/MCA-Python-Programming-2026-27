num = int(input("Enter an integer: "))

count = 0

print("Factors of", num, "are:")

for i in range(1, num + 1):
    if num % i == 0:
        print(i)
        count = count + 1

print("Total number of factors:", count)