# Hash table example in Python

# create a hastable all at once
items1 = dict({"key1" : 1, "key2" : 2, "key3" : "three"})
print(items1)

# create a hashtable progressively
items2 = {}
items2["key1"] = 1
items2["key2"] = 2
items2["key3"] = 3
print(items2)

# replacing and printing an specific key
items2["key2"] = "Two"
print(items2)

# printing an unexisting key
#print(items2["key6"])

# looping through dictionary keys:
for key, value in items2.items():
    print("Key: ", key, "value: ", value)

