#The Python language has a couple of methods for creating lists and dictionaries that are known as comprehensions.

#A list comprehension is basically a one line for loop that produces a Python list data structure.
x = [i for i in range(5)]
print(x)

#Can be used to apply functions to each item in a list. IE case multiple string to integers
x = ['1', '2', '3', '4', '5']
y = [int(i) for i in x]
print (y)

#Flatten nested lists
vec = [[1,2,3], [4,5,6], [7,8,9]]
newvec = [i for i in vec for i in i]
print(newvec)