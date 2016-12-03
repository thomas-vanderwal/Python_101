#Error Handling in python is normally wrapped with try/except/(finally)
#Python documentation for built in exceptions https://docs.python.org/2/library/exceptions.html

#Most common types:
# • Exception (this is what almost all the others are built off of)
# • AttributeError - Raised when an attribute reference or assignment fails.
# • IOError - Raised when an I/O operation (such as a print statement, the built-in
# open() function or a method of a file object) fails for an I/O-related reason, e.g.,
# “file not found” or “disk full”.
# • ImportError - Raised when an import statement fails to find the module definition
# or when a from … import fails to find a name that is to be imported.
# • IndexError - Raised when a sequence subscript is out of range.
# • KeyError - Raised when a mapping (dictionary) key is not found in the set of
# existing keys.
# • KeyboardInterrupt - Raised when the user hits the interrupt key (normally
# Control-C or Delete).
# • NameError - Raised when a local or global name is not found.
# • OSError - Raised when a function returns a system-related error.
# • SyntaxError - Raised when the parser encounters a syntax error.
# • TypeError - Raised when an operation or function is applied to an object of
# inappropriate type. The associated value is a string giving details about the type
# mismatch.
# • ValueError - Raised when a built-in operation or function receives an argument
# that has the right type but an inappropriate value, and the situation is not described
# by a more precise exception such as IndexError.
# • ZeroDivisionError -Raised when the second argument of a division or modulo
# operation is zero.

try:
    1/0
except ZeroDivisionError:
    print("You cannot divide by 0!")

#Catching multiple errors
#Method 1
my_dict={'a':1, 'b':2, 'c':3}
try:
    value=my_dict['d']
except IndexError:
    print("This index does not exist!")
except KeyError:
    print("This key is not in the dictionary")
except:
    print("This is a bare exception and is generally bad programming")

#Method 2
try:
    value=my_dict['d']
except (IndexError, KeyError):
    print('An IndexError or KeyError has occurred!')

#The finally statement
try:
    value=my_dict['d']
except KeyError:
    print('Still doesnt exist man')
finally:
    print('The finally statement executed!')

#Try also has an else clause. It will run only if no error is raised
try:
    value = my_dict["a"]
except KeyError:
    print("A KeyError occurred!")
else:
    print("No error occurred!")

#Can be used with finally as well
try:
    value = my_dict["a"]
except KeyError:
    print("A KeyError occurred!")
else:
    print("No error occurred!")
finally:
    print('The finally statement executed!')