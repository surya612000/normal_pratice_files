from threading import *
from time import sleep


# class hello(Thread):
#     def run(self):
#         for _ in range(5):
#             print("Hello")
#             sleep(1)

# class hi(Thread):
#     def run(self):
#         for _ in range(5):
#             print("Hi")
#             sleep(1)

def hello():
    for _ in range(15):
        print("Hello")
        sleep(1)

def hi():
    for _ in range(15):
        print("hi")
        sleep(1)

t1=Thread(target=hello)
t2=Thread(target=hi)

t1.start()
sleep(0.2)
t2.start()


t1.join()
t2.join()


print("BYE")