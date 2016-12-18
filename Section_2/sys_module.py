#The sys modules provides several system specific parameters and functions
import sys

#sys.argv is a list of command line arguments that were passed to the python script
#argv[0] is self. Depending on the OS this might be the full path or just the file name
print(sys.argv)

#Sys.executable is the absolute path to the Python interpreter. This is useful when
# using someone else's machine and need to Python is installed

print(sys.executable)

#sys.exit allows the programmer to exit from Python.
# This takes an optional parameter specifying the exit code
# When sys.exit is called it raises SystemExit exception

#sys.exit(0)

#sys.path is a list of strings that specify the search path for modules
print(sys.path)

#sys.platform identifies the OS.
print(sys.platform)

os = sys.platform
if os == 'win32':
    #use windows code here
    import csv
elif os.startswith('linux'):
    #do something linux specific
    import subprocess
    subprocess.popen(['ls, l'])

#sys.stdin/stdout/stderr allows us to map the standard input, output, and errors streams to a file