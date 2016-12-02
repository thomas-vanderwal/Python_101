#Chapter 5: Loops

#range will create a list that is n in length
print(range(5))
#Accepts begin and end params
print(range(5, 10))
#Accepts begin, end, and step params as well
print(list(range(1, 10, 2)))

for number in range(5):
    print(number)

a_dict = {'one':1,'two':2,'three':3}
for key in a_dict:
    print(key)

keys = a_dict.keys()
keys = sorted(keys)
for key in keys:
    print(key)

for number in range(10):
    if number % 2 == 0:
        print(number)

#while loop
#  Instead of executing over a range it will fire until a specific condition is met

i = 0
while i < 10:
    print(i)
    i += 1

#Python has a built in break function to get out of a loop early
i = 0
while i < 10:
    print(i)
    if i == 5:
        break
    i += 1