x = "       Allon, Chauhan"

print(x.strip()) #Removes white spaces from beginning and ending

y = "HELLO, WORLD, Allon, Chauhan"

z = x.strip()

print(z.upper())
print(y.lower())

print(y.replace("H", "A"))
print(y.split(","))

txt = "lo" in x
txt_not = "hn" not in x

print(txt)
print(txt_not)

age = str(18)
name = "Allon Chauhan is "

print(name + age)#use integer as string in sentence

print("Using quotes in sentence is by blackslash \"This is the way of writing it.\"")

print(name.title())
