from atexit import register
from threading import Thread
from re import compile
from time import ctime
from urllib.request import urlopen as uopen

REGEX = compile('#([\d,]+) in Books')
AMZN = 'http://www.amazon.com/dp/'
ISBNs = {
    '0132269937': 'Core Python Programming',
    '0132356139': 'Python Web Development with Django',
    '0137143419': 'Python Fundamentals'
}


def getRanking(isbn):
    page = uopen('{0}{1}'.format(AMZN, isbn))
    data = page.read()
    page.close()
    return REGEX.findall(data)[0]


def _showRanking(isbn):
    print(('- %r ranked %s' % (ISBNs[isbn], getRanking(isbn))))


def _main():
    print(('At', ctime(), 'on Amazon....'))
    for isbn in ISBNs:
        t = Thread(target=_showRanking, args=(isbn, ))
        t.start()
    print('OMG NOW WHERE')


@register
def _atext():
    print(('all DONE at:', ctime()))

if __name__ == '__main__':
    _main()
