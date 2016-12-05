#Working with files. This chapter will focus on reading and writing files to your disk drive

#It's important to treat file paths as wrong strings, which is done with a leading r. Note below the importance
print('C:\\Users\mike\py101book\data\test.txt')
print(r"C:\Users\mike\py101book\data\test.txt")

#opens our text file and reads the whole thing into a variable
#To open a binary file such as a PDF change the file mode from r to br
handle = open("test.txt", "r")
data = handle.read()
print(data)
handle.close()

#Writing to a file (wb for writing a binary)
handle = open('output.txt', 'w')
handle.write('This is a test')
handle.close()

#The with operator simplifies the writing and reading of files. It's known as a context manager and will automatically
#close the file when it's done
with open("test.txt") as file_handler:
    for line in file_handler:
        print(line)

#catching errors
try:
    file_handler = open('test.txt')
    for line in file_handler:
        print(line)
except IOError:
    print("An IOError has occurred")
finally:
    file_handler.close()

#Example above but using with
try:
    with open('test.txt') as file_handler:
        for line in file_handler:
            print(line)
except IOError:
    print('An IOError has occurred')

