"""
multi threading: multithreading is a way of achieving multitasking
Multithreading is defined as the ability of a processor to execute multiple threads concurrently.
"""

"""
A thread is an entity within a process that can be scheduled for execution.
Also, it is the smallest unit of processing that can be performed in an OS
In simple words, a thread is a sequence of such instructions within a program
that can be executed independently of other code
A thread contains all this information in a Thread Control Block (TCB)
Thread Identifier: Unique id (TID) is assigned to every new thread
Stack pointer: Points to thread’s stack in the process. Stack contains the local variables under thread’s scope.
Program counter: a register which stores the address of the instruction currently being executed by thread.
Thread state: can be running, ready, waiting, start or done.
"""

"""
We use threading.main_thread() function to get the main thread object
in normal conditions, the main thread is the thread from which the Python interpreter was started. 
We use the threading.current_thread() function to get the current thread object.
"""

# without threading calculating the time to execute the two classes code

import time

"""

class Apple:
    def run(self):
        for x in range(10):
            time.sleep(1)
            print('apple')


class Orange:
    def run(self):
        for x in range(10):
            time.sleep(1)
            print('orange')


A = Apple()
O = Orange()

start_time = time.perf_counter()
A.run()
O.run()
end_time = time.perf_counter()
print(f'processed in {end_time - start_time} seconds')  # time taken to execute 20 sec
"""

# using threading to get the time taken to execute the two classes


from threading import Thread

"""
class Apple(Thread):
    def run(self):
        for x in range(10):
            time.sleep(1)
            print('apple')


class Orange(Thread):
    def run(self):
        for x in range(10):
            time.sleep(1)
            print('orange')


A = Apple()
O = Orange()

start_time = time.perf_counter()
A.start()  # start is a method that present in thread class
time.sleep(0.1)
O.start()

A.join()
O.join()
end_time = time.perf_counter()
print(f'processed in {end_time - start_time} seconds')  # time taken is 10sec
"""


# using threading to get the time taken to execute the two functions

def run():
    time.sleep(1)
    print('iam running')


def walk():
    time.sleep(1)
    print('iam walking')

