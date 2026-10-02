num = int(input("enter the number : "))

if num % 2 == 0 :
    print("this number is even number")
else :
    print("this number is odd number")

#without arithmatic operator

num1 = int(input("Enter a number: "))

if num & 1 == 0 :
    print("even")      #If the last bit is 0, the number is even.
else:
    print("odd")       #If the last bit is 1, the number is odd