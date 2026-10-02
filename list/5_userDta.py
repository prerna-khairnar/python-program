import ast   #file import for accepting user lidt

lst = []
lst = input("enter one list in string format :")
lst = ast.literal_eval(lst)     #fun convert string into list(dictionary,tuple)
print(lst)

print(type(lst))
