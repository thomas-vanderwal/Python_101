import time

#ctime function will convert a time  in seconds since the epoch is a string representing local time
print(time.ctime())
print(time.ctime(1384112639))

#sleep function allows us to suspend execution of scripts a given number of seconds
for x in range(5):
    time.sleep(2)
    print('Slept for 2 seconds')

print(time.time())
print(time.ctime(time.time()))

