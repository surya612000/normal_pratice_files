import threading
import os
from time import sleep
 
def print_cube(num):
    sleep(1)
    print("Cube: {}" .format(num * num * num))
    print(threading.current_thread().name)
    print(os.getpid())
    
 
 
def print_square(num):
    print("Square: {}" .format(num * num))
    print(os.getpid())


def kkk(num):
    print("extra_function:{}".format(num**num))
    print(os.getpid())

def kk(num):
    print("extra_function222222222222222:{}".format(num*1000))
    print(os.getpid())


 
<<<<<<< Updated upstream

t1 = threading.Thread(target=print_square, args=(10,))
t2 = threading.Thread(target=print_cube, args=(10,))
t3=threading.Thread(target=kkk,args=(10,))
t4=threading.Thread(target=kk,args=(10,))
t1.start()
t2.start()
t4.start()
sleep(1)
t3.start()
print(os.getpid())
=======
if __name__ =="__main__":
    t1 =threading.Thread(target=print_square, args=(10,))
    t2 =threading.Thread(target=print_cube, args=(10,))
    t3=threading.Thread(target=kkk,args=(10,))
    t4=threading.Thread(target=kk,args=(10,))



    t1.start()
    t2.start()
    t4.start()
    sleep(1)
    t3.start()
>>>>>>> Stashed changes

    
t2.join()
t1.join()
t4.join()
    
print("srua")
    
 
print("Done!")