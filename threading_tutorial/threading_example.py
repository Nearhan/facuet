import threading
import urllib2

''' A tutorail to see how threading really works in PYTHON
'''


class FetchUrls(threading.Thread):

    def __init__(self, urls, output, lock):
        super(FetchUrls, self).__init__()
        self.urls = urls
        self.output = output
        self.lock = lock

    def run(self):
        while self.urls:
            url = self.urls.pop()
            req = urllib2.Request(url)
            try:
                d = urllib2.urlopen(req)
            except urllib2.URLError, e:
                print 'URL %s failed: %s' % (url, e.reason)
            self.lock.acquire()
            print 'lock acquired by %s' % self.name
            self.output.write(d.read())
            print 'write done by %s' % (self.name)
            print 'URL %s fetched by %s' % (url, self.name)
            print 'lock released by %s' % self.name
            self.lock.release()


class WriteToFile(threading.Thread):

    def __init__(self, sents, output):
        super(WriteToFile, self).__init__()
        self.sents = sents
        self.output = output

    def run(self):
        while self.sents:
            sent = self.sents.pop()
            self.output.write(sent)


# Lets define a main function
def main():
    lock = threading.Lock()
    urls1 = ['http://www.google.com', 'http://www.facebook.com']
    urls2 = ['http://www.yahoo.com', 'http://www.youtube.com']
    with open('output3.txt', 'w') as f:
        t1 = FetchUrls(urls1, f, lock)
        t2 = FetchUrls(urls2, f, lock)
        t1.start()
        t2.start()
        t1.join()
        t2.join()


def main2():
    sents1 = 'This is awesome. This is great. This is terrible!'.split('.')
    sents2 = 'You are awesome. You are terrible. You are great!'.split('.')
    with open('output2.txt', 'w') as f:
        t1 = WriteToFile(sents1, f)
        t2 = WriteToFile(sents2, f)
        t1.start()
        t2.start()
        t1.join()
        t2.join()

if __name__ == '__main__':
    main()
