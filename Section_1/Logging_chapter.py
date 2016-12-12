#Loging is a built in library meant to help debug code
#  Use thin instead of regular print statements to debug. With this library you
#  don't have to go back and remove those statements

import logging

#add filemode='w' to overwrite
logging.basicConfig(filename='sample.log', level=logging.INFO)

logging.debug("This is a debug message")
logging.info('This is an informational message')
logging.error('An error has happened')