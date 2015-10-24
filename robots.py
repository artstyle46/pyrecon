import urllib2
import io


def get_robots_txt(url):
    if url.endswith('/'):
        path = url
    else:
        path = url + '/'
    req = urllib2.Request(path + "robots.txt")
    req1 = urllib2.urlopen(req)
    #data = io.TextIOWrapper(req1, encoding= 'utf-8')
    return req1.read()


#print (get_robots_txt("http://www.google.com"))