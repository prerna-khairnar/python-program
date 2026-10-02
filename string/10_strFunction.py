#12. startswith --> check the start point of string
#13. endswith --> check the end point of string

name = "my name is prerana"
print(name.startswith("my"))     #true
print(name.startswith("name"))   #false
print(name.endswith("prerana"))     #true
print(name.endswith("name"))        #false

#14. isalpha --> check in string only present alphabet or not

name = "my name is prerana"
name1 = "my123nameisprerana"
print(name.isalpha())       #false
print(name1.isalpha())      #true

#15. isalnum --> check alphabet and number in string

print(name.isalnum())      #false
print(name1.isalnum())     #true

#16. isdigit --> check only digits in string

digit = "12345"
print(name.isdigit())      #false
print(digit.isdigit())     #true

#17. isupper --> check string is in upper or not
#18. islower --> check string is in lower or not

name = "my name is prerana"
print(name.isupper())       #false
name = name.upper()         #convert whole string into upper
print(name.isupper())       #true
name = name.lower()         #convert into lower
print(name.islower())       #true

#19. center --> shift string into center

name = "riyoo"
print(name)
print(name.center(25))

#20. ljust --> shift string into left side
#21. rjust --> shift string into right side
print(name.ljust(25))
print(name.rjust(25))