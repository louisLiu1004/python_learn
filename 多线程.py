__author__ = '財'


import threading
from threading import current_thread
# def myThread(arg1, arg2):
#      print(current_thread().getName(),'start')
#      print('%s %s'%(arg1, arg2))
#
# for i in range(1,10000,1):
#     # t1 = myThread(i, i+1)
#      t1 = threading.Thread(target=myThread,args=(i, i+1))
#      t1.start()

# class Mythreads(threading.Thread):
#     def run(self):
#         print(current_thread().getName(),'start')
#         print('run')
#         print(current_thread().getName(),'stop')
#
# t1 = Mythreads()
# t1.start()
# # t1.join()
#
# print(current_thread().getName(),'end')

from threading import Thread,current_thread
import time
import random
from queue import Queue

queue  = Queue(5)
class Producer(Thread):
    def run(self):
        name = current_thread().getName()
        nums = range(100)
        global queue
        while True:
            num = random.choice(nums)
            queue.put(num)
            print('生产者 %s 生产了数据 %s' %(name,num))
            t = random.randint(1,3)
            time.sleep(t)
            print('生产者 %s 睡眠了 %s 秒' %(name,t))
class Custmer(Thread):
    def run(self):
        name = current_thread().getName()
        global queue
        while True :
            num = queue.get()
            queue.task_done()
            print('消费者 %s 消耗了数据 %s' %(name,num))
            t = random.randint(1,5)
            time.sleep(t)
            print('消费者 %s 睡眠了 %s' %(name, t))


p1 = Producer(name= 'p1')
p1.start()
p2 = Producer(name= 'p2')
p2.start()
p3 = Producer(name= 'p3')
p3.start()
p4 = Producer(name= 'p4')
p4.start()
c1 = Custmer(name= 'c1')
c1.start()
c2 = Custmer(name= 'c2')
c2.start()