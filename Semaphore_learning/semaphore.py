from threading import BoundedSemaphore, Semaphore, Timer, Thread
import time

class Limiter(object):
    def __init__(self, max_calls, interval):
        self.sema = Semaphore(max_calls)
        self.interval = interval
        self.count = 0

    def release(self):
        print ("Release timer started, releasing in", self.interval, "seconds.")
        time.sleep(self.interval)
        self.sema.release()
        print ("Released.")

    def call(self, function=None, *args, **kwargs):
        self.count += 1
        print ("Aquiring.")
        print ("number:", self.count)
        self._drain()
        self.sema.acquire()
        if (self.sema.acquire(block=True)):
            print ("blocked")
        print ("aquired")

    def _drain(self):
        print ("Drain thread launched.")
        t = Thread(target=self.release, args=())
        t.start()
        '''
        Releases semaphore so it will allow max_calls amount of calls again
        '''

    def lock(self):
        '''
        Used to check when semaphore will allow calls
        '''
        pass


class MultiLimiter(object):
    def __init__(self, *args):
        '''
        Initalizes a list of limtier objects
        '''
        pass

    def call(self, function=None, *args, **kwargs):
        '''
        Handles call, utilizes _lock() method to block until call can be made
        '''
        pass

    def _lock(self):
        '''
        Checks when semaphores of Limiter objects allow access to resource
        '''
        pass


s = Limiter(10, 5)
s.call()
s.call()
s.call()
s.call()
s.call()
s.call()
s.call()
s.call()
s.call()
s.call()
s.call()
s.call()
s.call()
s.call()
s.call()
s.call()
s.call()
s.call()
s.call()


'''

from threading import Semaphore

 s = Semaphore(1)
 # semaphore counter is 1

 s.acquire()
 # semaphore counter is 0
 print('[+] Acquired, counter decreased by 1')
 print('[!] Semaphore counter is 0, if you call .acquire() again we will be stuck')

 s.release()
 # semaphore counter is 1 again
 print('[+] Released, counter increased by 1')

 s.acquire()
 # semaphore counter is 0
 print('[+] Acquired, counter decreased by 1')
 print('[!] Semaphore counter is 0, if you call .acquire() again we will be stuck')

 #s.release()
 #print('[+] Released, counter increased by 1')

 s.acquire()

 print('You will see me only if you uncomment .release()')

 '''