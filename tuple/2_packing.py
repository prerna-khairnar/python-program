#packing --> store miltiple value into single tuple

data = ()

riya = 87.9
munnu   = 91.9
vedu = 99
sanu = 39.99

data = (riya, munnu, vedu, sanu)
print(data)

#unpacking --> assigning the element of tuple to separate variables , extracting value from tuple

dta = (55, 66, 86, 39, 99)

math, english, science, marathi, hindi = dta
print("math :", math)
print("english :", english)
print("science :", science)
print("marathi :", marathi)
print("hindi :", hindi)