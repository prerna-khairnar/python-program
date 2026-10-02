n1 = int(input("Enter 1st number: "))
n2 = int(input("Enter 2nd number: "))
n3 = int(input("Enter 2nd number: "))

if n1 > n2  and n1 > n3 :
    print(f"{n1} is greatest number")

elif n2 > n1  and n2 > n3 :
    print(f"{n2} is greatest number")

else:
    print(f"{n3} is greatest number")

if n1 > n2  or n1 == n2 :
    print(f"{n1} is greater than or equal  to {n2}")

if not n1 == n2 :
    print("Numbers are not equal")

a = 10
b = 20

print("a =", a)
print("b =", b)

# Logical AND
print("a < b and a == 10 :", a < b and a == 10)

# Logical OR
print("a > b or a == 10 :", a > b or a == 10)

# Logical NOT
print("not(a > b) :", not(a > b))