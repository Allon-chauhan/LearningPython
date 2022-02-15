x = 'awesome'

def myFun():
    global x
    x = 'Fantastic'
    print('Python is ' + x)

myFun()

print(x)
