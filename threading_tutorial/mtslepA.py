from time import sleep, ctime
import thread


def loop0():
    print 'start loop 0 at:', ctime()
    sleep(4)
    print 'stop loop 0 at:', ctime()


def loop1():
    print 'start loop 1 at:', ctime()
    sleep(2)
    print 'stop loop1 at:', ctime()


def main():
    print 'starting at:', ctime()
    thread.start_new_thread(loop0, ())
    thread.start_new_thread(loop1, ())
    sleep(6)
    print 'all DONE at:', ctime()

if __name__ == '__main__':
    main()
