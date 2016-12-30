#lambda is a is an anonymous and unbound function. It's very limited. Mostly sees use with tkinker

import math

def sqroot(x):
    return math.sqrt(x)

square_rt = lambda x: math.sqrt(x)

if __name__ == '__main__':
    print(sqroot(49))
    print(square_rt(64))
