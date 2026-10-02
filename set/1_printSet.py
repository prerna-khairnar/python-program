set = {12, "riyoo", '$', 89.90, False}
print(set)     #print unordered sequence # cannot support indexing

# 1. remove --> remove specific value
set.remove(12)
print(set)

# 2. union --> add new element
#set = set.union({True, 100, "python"})  # need to store again
print(set.union({True, 100, "python"}))

# 3. pop --> remove the last element
set.pop()            # remove last elment
print(set)

# 4. discard --> remove specific element
value = {24, 66, 33, 98, 609, '*'}
print(value)
value.discard(66)
print(value)