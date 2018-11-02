import threading
import time


class myThread(threading.Thread):
    def run(self):
        if semaphore.acquire():
            print(self.name)
            time.sleep(1)
            semaphore.release()



if __name__ == '__main__':
    semaphore =threading.BoundedSemaphore(5) #规定通行的线程数
    thrs=[]
    for i in range(100):
        thrs.append(myThread())
    for t in thrs:
        t.start()
