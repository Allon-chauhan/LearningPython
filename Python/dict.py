brand = {
    "name" : "Audi",

    "brand of" : "Cars",

    "numbers of cars" : 2500
}

print(brand["numbers of cars"])#printing value of number of cars item

for x in brand.values(): #loop of printing value of each item
    print(x)

if "numbers of cars" in brand:
    print("Yes")

else:
    print("No")
