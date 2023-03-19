# from multiprocessing import Process
import time
# from threading import Thread
import threading

x = 0
locker = threading.Lock( )

def process1():
    global x
    i = 0

    while i < 100:
        locker.acquire()
        time.sleep(15)
        x -= 10
        print("Now decrement:", threading.current_thread().name,x)
        locker.release()
        i += 1


def process2():
    global x
    i = 0
    while i < 100:
        time.sleep(1)
        x += 1
        print(i, end = " ")
        print("__", threading.current_thread().name ,x)
        i +=1


if __name__ == '__main__':
    
    thread1 = threading.Thread(target=process1, args=(),daemon =True,  name="thr-1")
    thread2 = threading.Thread(target=process2, args=(),daemon =True, name="thr-2")

  

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join() 