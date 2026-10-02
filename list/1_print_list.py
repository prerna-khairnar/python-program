list = [10, 2.3, True, "riyoo", 'H', '1234']
print(list)
print(list[4])
print(list[:])
print(list[1:4])
print(list[::2])
print(list[::-1])   #reverse

multi_list = [12, [12.3, 55, 0], 90, 7 , ['riyo', [200,300,400], "prerana"], [1,2,3,4,5,6,7,8]]
print(multi_list[1][1])
print(multi_list[1][0])
print(multi_list[4][1])
print(multi_list[3])
print(multi_list[5][7])
print(multi_list[5][2])
print(multi_list[1][2])
print(multi_list[4][1][2])

#concatnation
l1 = [1,2,3,4,5]
l2 = ["riya", "sanu", "vedu"]
print(l1+l2)

#update list
l1[2] = 200
print(l1)

