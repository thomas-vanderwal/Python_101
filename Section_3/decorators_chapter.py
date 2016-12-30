#A decorator is a function that accepts another function as an argument.


#logging decorator
import logging

def log(func):
    """
    log what function was called
    """
    def wrap_log(*args, **kwargs):
        name = func.__name__
        logger = logging.getLogger(name)
        logger.setLevel(logging.INFO)

        #Add file handler
        fh = logging.FileHandler('%s.log' % name)
        fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        formatter = logging.Formatter(fmt)
        fh.setFormatter(formatter)
        logger.addHandler(fh)

        logger.info("Running function: %s" % name)
        result = func(*args, **kwargs)
        logger.info("Result: %s" % result)
        return func
    return wrap_log

@log
def double_function(a):
    """
    double the input parameter
    :return:
    """
    return a*2

if __name__ == '__main__':
    value = double_function(2)