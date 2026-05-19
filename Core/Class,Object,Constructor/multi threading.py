# from threading import Thread
# import time
# class MyThread(Thread):
#     def run(self):
#         for i in range(10):
#             time.sleep(1)
#             print("Starting Thread", i)
#
# t1=MyThread()
# t2=MyThread()
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print("Main thread")
#
# import threading
# import time
#
# def worker(delay):
#     for i in range(3):
#         time.sleep(delay)
#         print(f"[{threading.current_thread().name}] Iteration {i}")
#
#
# t1 = threading.Thread(target=worker, name="Thread-A", args=(1,), daemon=True)
# t2 = threading.Thread(target=worker, name="Thread-B", args=(1.5,), daemon=True)
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print("Done")
#
# import threading
# import time
#
# def say(msg):
#     print(f"[{threading.current_thread().name}] {msg}")
#
# t = threading.Thread(target=say, args=("Hello from thread!",), name="GreetThread")
# print(f"[Main] Starting {t.name}")
# t.start()
# t.join()
# print("[Main] Thread has finished. Alive?", t.is_alive())
#
#
# import threading
# counter = 0
# def unsafe_increment(n):
#     global counter
#     for _ in range(n):
#         counter += 1
# t1 = threading.Thread(target=unsafe_increment, args=(1000000,))
# t2 = threading.Thread(target=unsafe_increment, args=(1000000,))
# t1.start()
# t2.start()
# print("Expected counter = 2000000; Actual counter =", counter)
#
#
# import threading
#
# counter = 0
# lock = threading.Lock()
#
# def safe_increment(n):
#     global counter
#     for _ in range(n):
#         with lock:
#             counter += 1
#
# t1 = threading.Thread(target=safe_increment, args=(1000000,))
# t2 = threading.Thread(target=safe_increment, args=(1000000,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
#
# print("Expected counter = 2000000; Actual counter =", counter)
#
#
#
# import threading
# #
# cv = threading.Condition()
# items = []
#
# # Consumer thread
# def consumer():
#     with cv:
#         print("Consumer")
#         while not items:
#             cv.wait()        # wait for an item
#         item = items.pop()
#     print("Consumed", item)
#
# # Producer thread
# def producer(x):
#     with cv:
#         print("Producing", x)
#         items.append(x)
#         print("Produced", x)
#         cv.notify()         # signal that a new item is available
#
# t1 = threading.Thread(target=consumer)
# t2 = threading.Thread(target=producer, args=(5,))
# t1.start(); t2.start()
# t1.join(); t2.join()
#
#
# import threading, time
# start_event = threading.Event()
# def worker(id):
#     print(f"Worker {id} waiting to start")
#     start_event.wait()
#     print(f"Worker {id} started")
# threads = [threading.Thread(target=worker, args=(i,)) for i in range(3)]
# for t in threads: t.start()
# time.sleep(5)
# print("Main: Ready, set workers free!")
# start_event.set()
#
#
# from threading import Timer
#
# def delayed_action():
#     print("Action executed after delay")
#
# t = Timer(2.0, delayed_action)
# t.start()
#
# import threading, time
#
# def loop_print(name):
#     for i in range(3):
#         time.sleep(0.1)
#         print(f"{name}: {i}")
#
# t1 = threading.Thread(target=loop_print, args=("Thread-1",),daemon=True)
# t2 = threading.Thread(target=loop_print, args=("Thread-2",),daemon=True)
# t1.start(); t2.start()
#
#
# import threading
# from concurrent.futures import ThreadPoolExecutor
#
# def process(x):
#     print(f"Processing {x} in {threading.current_thread().name}")
#     return x * x
# inputs = [1, 2, 3, 4, 5]
# with ThreadPoolExecutor(max_workers=3) as executor:
#     futures = [executor.submit(process, x) for x in inputs]
#     for f in futures:
#         result = f.result()
#         print("Result:", result)
# #
#
# import threading
# #
# def task():
#     raise ValueError("An error occurred")
#
# t = threading.Thread(target=task)
# t.start()
# print("Main thread still running.")
#
# lock1 = threading.Lock()
# lock2 = threading.Lock()
# def t1():
#     with lock1:
#         print("t1")
#         with lock2:
#             print("inside t1")
# def t2():
#     with lock2:
#         print("t2")
#         with lock1:
#             t1()
#             print("inside t2")
# th1=threading.Thread(target=t1)
# th2=threading.Thread(target=t2)
# th1.start(); th2.start()
# th1.join(); th2.join()
#
# sem = threading.Semaphore(3)
# def task():
#     with sem:
#         print("Using resource")
# event = threading.Event()
# def waiter():
#     event.wait()
#     print("Proceeding")
# def signaler():
#     event.set()
#
#
# import asyncio
# import time
# #
# async def task(name, delay):
#     print(f"{name} starts at {time.time():.2f}")
#     await asyncio.sleep(delay)
#     print(f"{name} finishes at {time.time():.2f}")
#
# async def main():
#     a=task(name="A", delay=0.5)
#     print(a)
#     await a
#
#     tasks = [asyncio.create_task(task(f"Task-{i}", 1)) for i in range(3)]
#     print(*tasks, sep="\n")
#     await asyncio.gather(*tasks)
#
# asyncio.run(main())
#
# import multiprocessing
# p1=multiprocessing.Process(target=loop_print, name="p1",args=("Process-1",))
# p2=multiprocessing.Process(target=loop_print, name="p2",args=("Process-2",))
# if __name__=="__main__":
#     p1.start(); p2.start(); p1.join(); p2.join()



# 1. Write a Python program that creates a worker thread which prints “Hello
# from worker thread” while the main thread prints “Hello from main thread”, and
# ensure that the main thread waits for the worker thread to finish execution
# before the program exits.
# import threading
#
# def worker():
#     print("Hello from worker thread")
#
# t = threading.Thread(target=worker)
# t.start()
# print("Hello from main thread")
# t.join()



# 2. Write a Python program that creates three separate threads where each
# thread prints numbers from 1 to 5, and every printed number must be prefixed
# with the name of the thread that printed it, such as “Thread-1: 3”

# import threading
#
# def print_numbers():
#     thread_name = threading.current_thread().name
#     for i in range(1, 6):
#         print(f"{thread_name}: {i}")
#
# threads = []
#
# for i in range(1, 4):
#     t = threading.Thread(target=print_numbers, name=f"Thread-{i}")
#     threads.append(t)
#     t.start()
#
# for t in threads:
#     t.join()



# 3. Write a Python program in which a thread accepts two integer arguments,
# computes their sum, prints the result from inside the thread, and ensures that
# the main thread waits until the worker thread completes execution.
# import threading
#
# def add_numbers(a, b):
#     result = a + b
#     print(f"Sum inside thread: {result}")
# t = threading.Thread(target=add_numbers, args=(10, 20))
# t.start()
# t.join()
# print("Main thread finished after worker thread.")



