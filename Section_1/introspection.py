import sys

#This chapter is on the introspection package. It allows us to get python to tell us more about itself
x = "test"
y = 7
z = None

#Standard Python function type() can tell you the type of variable
print(type(x))
print(type(y))
print(type(z))

#Dir will tell us what methods an object has. It can also be used on modules
print(dir('test'))
print(dir(sys))

#Help() brings up the python documentation. It's interactive and isntead of getting >>> in the prompt you get help>
#Note it is case sensitive
help()