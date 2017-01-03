#profiling is an attempt to find bottlenecks in our code. It will find out what parts are taking the longest so we can review
#   cProfile can also be ran in the command line
#   python -m cPython filename.py
#   python -m cPython -o output.txt filename.py     This will save the output but the output has to be parsed with pstats
import time
import cProfile

def fast():
    print('I run fast!')

def slow():
    time.sleep(3)
    print('I run slow!')

def medium():
    time.sleep(.5)
    print ('I run a little slowly...')

def main():
    fast()
    slow()
    medium()

if __name__ == '__main__':
    main()
    cProfile.run('main()')