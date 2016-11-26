#Chapter 3 using more of python's built in data types
#lists function as arrays do in other languages, but are not data type specific

my_list=['a', 1, 5, 'Python']
print(my_list)

my_list2 = [1, 2, 3]
nested_list = (my_list, my_list2)
print(nested_list)

combo_list = my_list + my_list2
print(combo_list)

#slice them like you do a string
print(combo_list[1:4])

#tuples are like lists but you create them with () instead of []
# The main difference between the two is that tuples are immutable while lists are mutable
my_tuple = (1,2,3,4,5)
print(my_tuple)
print(my_tuple[0:3])

#Dictionaires are pretty much hash tables or a hash mapping
#  They are created with {} and the keys must be unique
my_dict={'one':1, 'two':2, 'three':3}
print(my_dict)
print(my_dict['one'])

print('one' in my_dict)
print('four' in my_dict)
print(my_dict.keys())