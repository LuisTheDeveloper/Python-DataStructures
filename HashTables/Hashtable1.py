fruits = [
    {'name' : 'apple', 'price' : 20},
    {'name' : 'avocado', 'price' : 25},
    {'name' : 'banana', 'price' : 22}
]

fruit_names = []

#for fruit in fruits:
#    fruit_names.append(fruit['name'])
#print(fruit_names)

#for price in fruits:
#    fruit_names.append(price['price'])
#print(fruit_names)

for fruit in fruits:
    fruit_names.append(fruit['name'])
    fruit_names.append(fruit['price'])
print(fruit_names)

meats = [
    {'name' : 'cow', 'price' : 20},
    {'name' : 'pork', 'price' : 25},
    {'name' : 'chicken', 'price' : 22}
]

# printing the list with only print
print(
    [meat['name'] for meat in meats]
)

# conditional printing
print(
    [meat['name'] for meat in meats if meat['name'][1] == 'o']
)

fishes = [
    {'name' : 'codfish', 'price' : 25},
    {'name' : 'Salmon', 'price' : 35},
    {'name' : 'haddock', 'price' : 15}    
]

# alternative way using dictionary
print(
    {fish['name']: fish['price'] for fish in fishes}
)