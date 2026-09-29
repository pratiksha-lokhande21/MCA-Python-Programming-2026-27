num=int(input("Enter Your Number:"))
original=num
reverse =0
while num>0:
    digit=num%10
    reverse= reverse *10 +digit
    num=num//10
if original == reverse:
    print("Number is palindrome")
else:
    print("Number is not a palindrome number")
