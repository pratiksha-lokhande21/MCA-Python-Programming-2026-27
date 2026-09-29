while True:
    print("\n----- Mathematical Application -----")
    print("1. Check Prime")
    print("2. Check Palindrome")
    print("3. Check Armstrong")
    print("4. Factorial")
    print("5. Fibonacci Series")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        num = int(input("Enter a number: "))

        if num <= 1:
            print("Not a Prime number")
        else:
            for i in range(2, num):
                if num % i == 0:
                    print("Not a Prime number")
                    break
            else:
                print("Prime number")

    elif choice == 2:
        num = int(input("Enter a number: "))

        original = num
        reverse = 0

        while num > 0:
            digit = num % 10
            reverse = reverse * 10 + digit
            num = num // 10

        if original == reverse:
            print("Palindrome")
        else:
            print("Not Palindrome")

    elif choice == 3:
        num = int(input("Enter a number: "))

        original = num
        digits = 0
        total = 0

        while num > 0:
            digits = digits + 1
            num = num // 10

        num = original

        while num > 0:
            digit = num % 10
            total = total + digit ** digits
            num = num // 10

        if total == original:
            print("Armstrong number")
        else:
            print("Not an Armstrong number")

    elif choice == 4:
        num = int(input("Enter a number: "))

        factorial = 1

        for i in range(1, num + 1):
            factorial = factorial * i

        print("Factorial:", factorial)

    elif choice == 5:
        n = int(input("Enter number of terms: "))

        a = 0
        b = 1

        print("Fibonacci Series:")

        for i in range(n):
            print(a, end=" ")

            c = a + b
            a = b
            b = c

        print()

    elif choice == 6:
        print("Exiting the application...")
        break

    else:
        print("Invalid choice. Please try again.")