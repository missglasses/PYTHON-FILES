#Python List 

#List with the same types
garden = ["tulip", "lily", "orchid"]
print(garden)

#List with different types
store = [2, "tulip", 70.00]
print("Receipt: Item: %s Amount: %d Price: %.2f" %(store[1], store[0], store[2]))

#Nested 
numeros = [[1,2], [3,4], [5,6]]
print(numeros)

#Subsetting List - accessing list
print(store[1])

#Slice element (Range)
print(garden[0:2])
print(garden[-1]) #prints last element

#Manipulating List
garden[2]="rose"
print(garden[2])

#Extend List
garden.append("orchid") #if one item ra
print(garden)

garden.extend(["lily of the valley", "poppy"]) #if multiple items
print(garden)

#Delete Element(s)
del garden[2] #delete one element
print(garden) 

garden.remove("poppy") #specific kaayo
print(garden)