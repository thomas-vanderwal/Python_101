#The Python language has a couple of methods for creating lists and dictionaries that are known as comprehensions.

#A list comprehension is basically a one line for loop that produces a Python list data structure.
x = [i for i in range(5)]
print(x)

#Can be used to apply functions to each item in a list. IE case multiple string to integers
x = ['1', '2', '3', '4', '5']
y = [int(i) for i in x]
print (y)

#Flatten nested lists
#Python documentation has other examples for nested list comprehensions. Take a look at them later
vec = [[1,2,3], [4,5,6], [7,8,9]]
newvec = [c for i in vec for c in i]
print(newvec)

#Dictonary comprehensions
print( {i: str(i) for i in range(5)} )
#Using this technique to swap dictionary keys and values
my_dict = {1:"dog", 2:"cat", 3:"hamster"}
print( {value:key for key, value in my_dict.items()} )

#Set comprehensions
#Sets are like mathematical sets where they don't have any repeated values
my_list = [1, 2, 2, 3, 4, 5, 5, 7, 8]
my_set = set(my_list)
print(my_set)

#Same code written as a comprehension
my_set = {x for x in my_list}
print(my_set)