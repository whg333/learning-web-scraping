# encoding: UTF-8

import builtwith
import whois

def main():
    webscraping = 'http://example.webscraping.com'
    baidu = 'http://www.baidu.com'
    
    parseBuiltwith(webscraping)
    parseBuiltwith(baidu)
    
    paresWhois(webscraping)
    paresWhois(baidu)
    
def parseBuiltwith(url):
    print url , ' : ' ,  str(builtwith.parse('http://example.webscraping.com'))
    
def paresWhois(url):
    print url , ' : ' , whois.whois(url)

if __name__ == '__main__':
    main()