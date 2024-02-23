import threading
 
 
def print_cube(num):
    print("Cube: {}" .format(num * num * num))
 
 
def print_square(num):
    print("Square: {}" .format(num * num))


def kkk(num):
    print("extra_function:{}".format(num**num))

def kk(num):
    print("extra_function222222222222222:{}".format(num*1000))


 
if __name__ =="__main__":
    t1 = threading.Thread(target=print_square, args=(10,))
    t2 = threading.Thread(target=print_cube, args=(10,))
    t3=threading.Thread(target=kkk,args=(10,))
    t4=threading.Thread(target=kk,args=(10,))
    t1.start()
    t2.start()
    t3.start()
    t4.start()

    
    t1.join()
    t2.join()
    t4.join()
    
 
    print("Done!")