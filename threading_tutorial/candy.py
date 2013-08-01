from atexit import register
from random import randrange
from threading import BoundedSemaphore, Lock, Thread
from time import ctime, sleep

#define a lock
lock = Lock()
MAX = 5
candytray = BoundedSemaphore(MAX)


def refill():
    lock.acquire()
    print 'Refilling candy'
    try:
        candytray.release()
    except ValueError:
        print 'Full, skipping'
    else:
        print 'OK'
    lock.release()


def buy():
    lock.acquire()
    print 'Buying Candy'
    if candytray.acquire(False):
        print 'OK'
    else:
        print 'empty, skipping'
    lock.release()


def producer(loops):
    for i in xrange(loops):
        refill()
        sleep(randrange(3))


def consumer(loops):
    for i in xrange(loops):
        buy()
        sleep(randrange(3))


def _main():
    print 'starting time at: ', ctime()
    nloops = randrange(2, 6)
    print 'Candy Machine full with %d bars' % MAX
    Thread(target=consumer, args=(
        randrange(nloops, nloops + MAX + 2),)).start()
    Thread(target=producer, args=(nloops,)).start()


@register
def _atexit():
    print 'ALL DONE at:', ctime()

if __name__ == '__main__':
    _main()
