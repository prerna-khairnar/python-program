n1 = int(input("Enter 1st number: "))
n2 = int(input("Enter 2nd number: "))

if n1 > n2:
    print(f"{n1} is greater than {n2}")

elif n1 < n2:
    print(f"{n2} is greater than {n1}")

else:
    print("Both numbers are equal.")

a = 10
b = 20

print("a =", a)
print("b =", b)

print("a == b :", a == b)   # Equal to
print("a != b :", a != b)   # Not equal to
print("a > b  :", a > b)    # Greater than
print("a < b  :", a < b)    # Less than
print("a >= b :", a >= b)   # Greater than or equal to
print("a <= b :", a <= b)   # Less than or equal to