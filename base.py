import twitter
import redis




class Facet(object):
    pass

    
r = redis.StrictRedis(host='localhost', port=6379, db=0)