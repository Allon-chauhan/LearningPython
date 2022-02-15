list = {"allon", "ashish", "andrelina", "Dolly"}

list.discard("allon") #discard will not raise a error if the item doesnot exist in the list
list.discard("hello")

list.remove("ashish") #remove will raise the problem if the item doesnot exixt in the list

print(list)
