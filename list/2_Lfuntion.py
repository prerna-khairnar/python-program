# 1.append --> add new element

l1 = [1, 2, 3, 4, 5, 6]
#l1[6] = 7
print(l1)
l1.append(7)
print(l1)

# 2.pop --> remove the element using index

l1.pop()   #remove last element
print(l1)
l1.pop(3)  #remove index no. 3
print(l1)

# 3.sort --> sort the element 

list = [7, 4, 8, 2, 9, 3, 12 ,10, 1]
print("before operation :", list)
print("\n")

list.sort()    #sort in ascending order
print("after operation :", list)

print("descending order :",list[::-1])   #reverse list

list.sort(reverse=True)
print("after operation descending order :",list)     ##sort in descending order

# 4.reverse --> print list in reverse form

list1 = [1,2,3,4,5,6,7,8,9,10]
print(list1[::-1])
list1.reverse()
print(list1)
