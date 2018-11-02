import threading
import time
from random import randint

class Boss(threading.Thread):
    def run(self):
        print('Boss:今晚加班到22:00')
        event.set()
        time.sleep(randint(1,5))
        print('Boss:22:00到了，可以下班了')
        event.set()
class Woker(threading.Thread):
    def run(self):
        event.wait()
        print('Woker:好惨啊加班中...................')
        event.clear()
        event.wait()
        print('Woker:太棒了')

if __name__=='__main__':
    event = threading.Event()
    threads = []
    for i in  range(5):
        threads.append(Woker())
    threads.append(Boss())
    for t in threads:
        t.start()
    for t in threads:
        t.join()