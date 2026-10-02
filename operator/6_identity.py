num = 5
num *= num

print(num)
print("address of num is", id(num))

x = 10
y = '10'

print("address is same :", x is y)        # == --> is
print("address is same :", x is not y)    # != --> is not

# is --> Compares the memory addresses (id) of two variables, used to compare value & its type
# == --> Compares the values of two variables., used to compare value

x = [7,8,4]
y = [7,8,4]

print("address is same :", x is y)        
print("address is same :", x == y)

