# encoding: UTF-8

import urllib2

def download(url, retry_num=2):
    print 'Downloading : ', url
    html = url
    try:
        html = urllib2.urlopen(url).read()
    except urllib2.URLError as e:
        print 'Download error : ', e.reason
        html = None
        if retry_num > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                return download(url, retry_num-1)
    if html is not None:
        print html
    return html

def main():
    download('http://httpstat.us/500')
    download('http://httpstat.us/200')
    download('http://www.baidu.com')

if __name__ == '__main__':
    main()