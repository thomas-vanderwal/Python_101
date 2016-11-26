#Chapter 4: Conditional statements
# Like most languages, python supports an if/elif/else type statement
# However, it doesn't support CASE/SWITCH :(

if 2 > 1:
    print('This is a true statement')

#Note the indented spaces. This is what tells python to run code within a statement (like {})
#  4 spaces is recommended as a python standard but any number will work as long as
#  the programmer is consistent

var1=1
var2=3
if var1 > var2:
    print('This is also True')
else:
    print('That was False!')

#python's conditional operators have the following order of operations
#   1)or 2)and 3)not
x = 10
y = 20

if x < 10 or y > 15:
    print("This statement was True!")


x = 10
y = 10

if x == 10 and y == 15:
    print("This statement was True")
else:
    print("This statement was False")


my_list = [1, 2, 3, 4]
x = 10

if x not in my_list:
    print(''''x' is not in the list, so this is True!''')

if x != 11:
    print('x is not equal to 11')

z = 11
if x not in my_list and z != 10:
    print('This is True')

#checking for nothing (null in most languages)
empty_list = []
empty_tuple = ()
empty_string = ""
nothing = None

if empty_list == []:
   print("It's an empty list!")

if empty_tuple:
   print("It's not an empty tuple!")

if not empty_string:
   print("This is an empty string!")

if not nothing:
    print("Then it's nothing!")

#Special characters
print('I have a \n new line in this sentence')
print('This sentence is \ttabbed')
print('Escape \\ with itself')

