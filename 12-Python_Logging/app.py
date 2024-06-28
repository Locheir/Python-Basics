# Import Library
import logging 

## Configure logging settings 
logging.basicConfig(
    level = logging.DEBUG,
    format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler('app1.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger('ArithmeticApp')

def addition(a, b) :
    result = a + b
    logger.debug(f"Adding {a} + {b} = {result}")
    return result

def subtraction(a, b) :
    result = a - b
    logger.debug(f"Subtracting {a} - {b} = {result}")
    return result

def multiply(a, b) :
    result = a * b
    logger.debug(f"Multiplying {a} * {b} = {result}")
    return result

def division(a, b) :
    try :
        result = a / b
        logger.debug(f"Dividing {a} / {b} = {result}")
        return result
    except ZeroDivisionError:
        logger.error("Division By Zero Error")
        return None
    
addition(10,151)
subtraction(25,20)
multiply(9,2)
division(10,0)