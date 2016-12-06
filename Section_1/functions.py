#A function is a structure that you define and are created using def
def a_function():
    print('My first function!')

a_function()

#Parameters are adding within the parens
def add(a,b):
    return a + b

print(add(1,2))

#Params can be named in the call as well
print(add(b=2, a=1))

#default values
def keyword_values(a=1,b=2):
    return a + b

print(keyword_values(4,5))
print(keyword_values())