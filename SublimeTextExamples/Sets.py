#Sets are unordered colletion of items.

my_set = {2,3,4}
print(my_set)

my_set2 = {2,5,3,4,2,2,3}
print(my_set2) #prints only unique values(Will have no duplicates)

# Methods usd in sets

print(my_set.intersection(my_set2))
print(my_set2.difference(my_set))
print(my_set.union(my_set2))

#How to create an empty set

x = set()
x.add('Deepika')
print(x)
x.add('Vaasi')
print(x)
x.add('Vaasi')  #Duplicates will be ignored 
print(x)