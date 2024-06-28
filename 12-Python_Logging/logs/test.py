from logger import logging

def add(a, b):
    logging.debug('Addtion Operation is taking place.')
    return a + b

logging.debug('Addition Function is called !')
add(10,15)
