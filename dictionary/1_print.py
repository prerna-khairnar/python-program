start = {"class" : "techno_script", "Batch" : 100, "count" : 18}
print(start["class"])    #display specific value using key
print(start["count"])

start["count"] = 20   #change the data (mutable)
print(start)

# 1.update() --> update add new value & add new key : value pair 
start.update({"Batch" : "111"})     #update new value
print(start)

start.update({"year" : "2026"})     #add new key : value at the end of dictionary
print(start)

# 2.keys() --> display only keys
# 3.values() --> display only values list

print(start.keys())       #print keys
print(start.values())     #print values

# 4.item() --> display key:value pair in separate group
 
print(start.items())    #dict_items([('class', 'techno_script'), ('Batch', '111'), ('count', 20), ('year', '2026')])

# 5.get() --> access specific key data

print(start.get("class"))   #if key are not in dic then output is (none)

# nested dictionary

location = {"India" : {"Maharashtra" : ["pune", "pcmc"]}}
print(location["India"]["Maharashtra"][1])
