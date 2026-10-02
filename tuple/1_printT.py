laptop = ("hp", "dell", "mac", "asus")
print(laptop)

#indexing
print(laptop[3])

#slicing
print(laptop[1:])
print(laptop[1::2])
print(laptop[::-1])

#accept user data
new_lap = input("enter laptop name :")
laptop = list(laptop)          #laptop tuple convert into list because list is mutable
laptop.append(new_lap)         # add new element at the end of tuple


print("before coversion :",laptop)
laptop = tuple(laptop)         # list convert into tuple

print("after conversion :",laptop)

#replace new element
laptop = list(laptop)   #tuple convert into list

laptop[3] = "acer"    #replace elemnt
laptop = tuple(laptop)

print(laptop)
