cars = ["BMW", "Audi", "Mercedes", "Bugatti"]

print(cars)

print(len(cars))

cars.append("Lincoln")
cars.insert(0, "Ferrari")

print(cars[4])
print(cars[0])
print(len(cars)) #print length of list

cars.remove("Audi") #remove audi from list
print(len(cars))

anotherlist = cars.copy() #copy cars to anotherlist
print(anotherlist)

add = anotherlist + cars #adding two list to one list

add.reverse()#reverse a list

print(add)

add.sort()

print(add)
