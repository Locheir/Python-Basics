### Multi-Threading
## When to use Multi-Threading

# 1. I/O Bound Tasks : Task that spends more time waiting for I/O Operations.
# 2. Concurrent Execution : When you want to improve the throughput of your application

import threading
import time

def print_numbers() :
    for i in range(5) :
        time.sleep(2)
        print(f"Number : {i}")

def print_letters() :
    for letter in "abcde" :
        time.sleep(2)
        print(f"Letter : {letter}") 

# Create 2 Threads : 
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

t = time.time()

# Start the Thread()
t1.start()
t2.start()

# Wait for Threads to Complete :
t1.join()
t2.join()

finished_time = time.time() - t
print(finished_time)