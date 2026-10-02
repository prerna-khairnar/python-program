# 5.Insert --> add specific new element

lst = ["riyoo", "100", 50, True, 12.2, '#']
lst.insert(2,20)  #you cannot add multiple data because only 2 arguement are present
print(lst)

# 6.extend --> add multiple element at the end of list

lst.extend(["sanu", 500, '@'])
print(lst)

# 7.remove --> remove value from list

lst.remove("100")
print(lst)

# 8.clear --> clear the list

lst.clear()    #clear the list ([]) not remove , if remove then display (none)
print(lst)

# 9.count --> count the element

lst1 = [1, 2, 2, 2, 3, 4, 2, 2]
c = lst1.count(2)
print(c)

# 10.copy --> copy one list into another

lst2 = []
print("before operation :")
print("list 1 :",lst1)
print("list 2 :",lst2)

lst2 = lst1.copy()
print("after operation :")
print("list 1 :",lst1)
print("list 2 :",lst2)

