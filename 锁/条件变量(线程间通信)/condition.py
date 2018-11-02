

import threading
import time
from random import randint

class Producer(threading.Thread):
    def run(self):
        global L
        while 1:
            val = randint(0,100)
            print('生产者',self.name,':Append: '+str(val),L)
            if lock_con.acquire():
                L.append(val)
                lock_con.notify() #通知wait方法，重新激活锁运行线程
                lock_con.release()
            time.sleep(3)

class Custmer(threading.Thread):
    def run(self):
        global L
        while 1:
            lock_con.acquire()
            if len(L)==0:
                lock_con.wait() #释放锁，并阻塞线程
            print('消费者',self.name,':Delete'+str(L[0]),L)
            del L[0]
            lock_con.release()
            time.sleep(0.2)


if __name__=='__main__':
    L = []
    lock_con = threading.Condition()
    thres =[]

    for i in range(5):
        thres.append(Producer())
    thres.append(Custmer())
    for t in thres:
        t.start()
    for t in thres:
        t.join()

