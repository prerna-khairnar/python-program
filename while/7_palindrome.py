num = int(input("Enter a number: "))

temp = num

s = str(num)   #convert into string

rev = s[::-1]  #reverse string

rev = int(rev)   #convert into int

if temp == rev:
    print("This is a Palindrome number")
else:
    print("This is not a Palindrome number")


""""num = int(input("Enter a number: "))

temp = num
rev = 0

while num > 0:
    rem = num % 10
    rev = rev * 10 + rem
    num //= 10

if temp == rev:
    print("This is a Palindrome number")
else:
    print("This is not a Palindrome number")"""