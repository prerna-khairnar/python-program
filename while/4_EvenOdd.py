lst = list(map(int, input("Enter list elements: ").split()))

i = 0

while i < len(lst):
    if lst[i] % 2 == 0:
        print(lst[i], "is Even")
    else:
        print(lst[i], "is Odd")

    i += 1