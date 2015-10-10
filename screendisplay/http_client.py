import urllib2


class http_client:
    def __init__(self, hostname, port):
        self.hostname = hostname
        self.port = port

    def __request(self, req_url):
        url = "http://%s:%d/%s" % (self.hostname, self.port, req_url)

        req = urllib2.urlopen(url)
        data = req.read()
        print data