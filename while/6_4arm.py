# A 4-digit Armstrong number is a number that is equal to the sum of the 4th powers of its digits.

num = int(input("Enter a number: "))

temp = num
rem = 0
sum = 0

cnt = len(str(num))

while(num > 0):
    rem = num % 10
    sum += rem ** cnt
    num //= 10

if temp == sum:
    print("this is armstrong number ")
else:
     print("this is not armstrong number ")