#5. upper --> convert string into upper case
#6. lower --> convert string into lower case

name = "techno script fc_road pune , Techno , Techno"
print(name.upper())
print(name.lower())

#7. swapcase --> convert upper into lower, lower into upper

print(name.swapcase())

#8. capitalize --> conver 1st word 1st char into capital
#9. title --> convert all words 1st char into capital

name = "my name is prerana"
print(name.capitalize())
print(name.title())

#10. find --> find word or char , if present it return index(position) 1st char 
#if not return -1 = spacial value py used

name = "my name is prerana"
print(name.find("prerana"))   #index pos
print(name.find('z'))         #-1
print(name.find('a'))         #when multiple time present return 1st index of 1st find

#11. index --> work as find fun but if not present then generate error (valueerror)

print(name.index('a'))        #index pos
print(name.index("name"))     #valueerror
