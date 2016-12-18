#The subprocess module allows us to start processes or programs in Python
# In other words we can start applications and pass parameters to them

import subprocess

#subprocess.call('notepad.exe')
#Running the above line will open a notepad sessions.
#   Notice that the terminal will wait till the application closes to send a return code

#The code below returns the return code into a variable that we can then analyze to make sure we got the
# expected results
code = subprocess.call('notepad.exe')
if code == 0:
    print('Success!')
else:
    print('Error!')

#The call method also accepts arguments to be passed to the program we're executing
code = subprocess.call(['ping', 'www.yahoo.com'])
print(code)