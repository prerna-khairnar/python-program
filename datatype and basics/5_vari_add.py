n1 = int(input("enter 1st number :"))
n2 = int(input("enter 2nd number :"))

print("num1 : ",n1,"\tnum2 : ",n2)

# same num = same adress / different value = different add
print("address of num1 : ",id(n1))
print("address of num2 : ",id(n2))

