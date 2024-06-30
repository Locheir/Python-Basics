'''
    Real-World Example : Multiprocessing for CPU-bound Tasks
    Senario : Factorial Calculation
    Factorical Calculation , especially for large numbers,
    involve significant computational work. Multiprocessing
    can be used to distribute the workload accross multiple
    CPU cores, improving performance.
'''

import multiprocessing 
import math 
import sys
import time

## Increase the maximum number of digits for Integer Conversion
sys.set_int_max_str_digits(100000)

## Function to Compute Factorial of a given number.
def compute_factorial(number):
    print(f"Computing the Factorial of {number}")
    result = math.factorial(number)
    print(f"FactoriaL of {number} is {result}")
    return result

if __name__ == "__main__" :

    numbers = [5000,6000,7000,8000]
    start_time = time.time()

    ## Create a Pool of Worker Processes
    with multiprocessing.Pool() as pool : 
        results = pool.map(compute_factorial,numbers)

    end_time = time.time()

    print(f"Results : {results}")
    print(f"Time taken : {end_time - start_time} seconds")