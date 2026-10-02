num = int(input("Enter a number: "))

temp = num
rem = 0
sum = 0

while(num > 0):
    rem = num % 10
    sum += rem * rem * rem
    num //= 10

if temp == sum:
    print("this is armstrong number ")
else:
     print("this is not armstrong number ")