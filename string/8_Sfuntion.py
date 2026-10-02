#string built-in funtion
#1. Strip --> remove space

name = "   tech   "
print(name)
print("remove space")
print(name.strip())

print("\n")

name = "*****tech*****"
print(name)
print("remove star")
print(name.strip('*'))

print("\n")

#2. split --> split the string , make list

name = "techno script fc_road pune"
print(name.split())
new_var = name.split()
print(type(new_var ))
print("\n")

#3. replace --> replace specific word or character

name = "techno script fc_road pune"
print(name.replace("fc_road","jm_road"))
print(name)
name = name.replace("fc_road","jm_road") #for constant to store again in same variable
print(name)

#reclace character

print(name.replace('n','$'))

#4. count --> count word or character in sentence ,, case sensetive

name = "techno script fc_road pune "
print(name.count('n'))

name = "techno script fc_road pune ,techno,Techno"
print(name.count("techno"))

#also count space
name = "techno script fc_road pune , techno , Techno"
print(name.count(' '))




