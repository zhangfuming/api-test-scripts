__author__ = 'zhangfuming'

import pycurl
import StringIO
import urllib

class CurlService:

    def get(self,item,env):
        url = item['url_dev']
        if env == 'pro':
            url = item['url_pro']
        crl = pycurl.Curl()
        crl.setopt(pycurl.VERBOSE,1)
        crl.setopt(pycurl.FOLLOWLOCATION, 1)
        crl.setopt(pycurl.MAXREDIRS, 5)
        crl.setopt(pycurl.USERAGENT,"Tester")
        crl.setopt(pycurl.CONNECTTIMEOUT,60)
        crl.setopt(pycurl.TIMEOUT,600)
        crl.fp = StringIO.StringIO()
        crl.setopt(pycurl.URL, url)
        crl.setopt(crl.WRITEFUNCTION, crl.fp.write)
        crl.perform()
        return {
         "http_status" : crl.getinfo(crl.HTTP_CODE),
         "content_type" : crl.getinfo(crl.CONTENT_TYPE),
         "effective_url" : crl.getinfo(crl.EFFECTIVE_URL),
         "response" : crl.fp.getvalue()
        }

    def post(self,item,env):
        url = item['url_dev']
        if env == 'pro':
            url = item['url_pro']
        post_data_dic = item['params']
        crl = pycurl.Curl()
        crl.setopt(pycurl.VERBOSE,1)
        crl.setopt(pycurl.FOLLOWLOCATION, 1)
        crl.setopt(pycurl.MAXREDIRS, 5)
        crl.setopt(pycurl.CONNECTTIMEOUT, 60)
        crl.setopt(pycurl.TIMEOUT, 300)
        crl.setopt(pycurl.HTTPPROXYTUNNEL,1)
        crl.fp = StringIO.StringIO()
        crl.setopt(pycurl.USERAGENT, "Tester")
        crl.setopt(crl.POSTFIELDS,  urllib.urlencode(post_data_dic))
        crl.setopt(pycurl.URL, url)
        crl.setopt(pycurl.HTTPHEADER,item['header'])
        crl.setopt(crl.WRITEFUNCTION, crl.fp.write)
        crl.perform()
        return {
         "http_status" : crl.getinfo(crl.HTTP_CODE),
         "content_type" : crl.getinfo(crl.CONTENT_TYPE),
         "effective_url" : crl.getinfo(crl.EFFECTIVE_URL),
         "response" : crl.fp.getvalue()
        }



def main():
    curlService = CurlService()
    result = curlService.post()
    print result

if __name__ == "__main__":
    main()


