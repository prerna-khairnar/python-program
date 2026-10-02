
lst = list(map(int, input("enter list : ").split()))   # split separate string whenever find space in user input
sum = 0

for i in lst :
    sum += i
print("sum of list is :", sum)