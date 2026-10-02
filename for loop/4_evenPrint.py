list = list(map(int, input("enter the numbers : ").split()))

count = 0

for i in list :
    if i % 2 == 0 :
       count = i
       print("even number : ", count)
    else :
        count = i
        print("odd numbers : ", count)
 