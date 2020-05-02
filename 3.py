from bs4 import BeautifulSoup
#import urllib2
import requests
import re

myfile = open("dogs.txt","w+")
myfile.close()

url="http://trackinfo.com/entries-race.jsp?raceid=GBR$20140302A01"
page=urllib.request.urlopen(url)
soup = BeautifulSoup(page.read())
names=soup.findAll('a',{'href':re.compile("dog")})
myfile = open("base/dogs.txt","w+")


for eachname in names:
    d = ' '.join(eachname.string.split()) + '\n'
    print (d)
    myfile.write(d)
myfile.close()