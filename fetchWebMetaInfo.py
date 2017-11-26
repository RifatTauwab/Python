from bs4 import BeautifulSoup
import urllib
import requests

url = 'http://www.bbc.com/future/story/20171124-what-if-all-animals-had-human-intelligence'
#page = urllib.urlopen(url).read()
agent = {"User-Agent": "Mozilla/5.0"}
page = requests.get(url, headers=agent).text
soup = BeautifulSoup(page,'html.parser')

try:
    title = soup.find("title").text
except:
    title = "no title found"
        
try:
    try:
        desc = soup.find("meta", property="og:description")['content'].encode('utf-8')
    except:
        try:
            desc = soup.find(attrs={'name': 'Description'})['content'].encode('utf-8')
        except:
            desc = soup.find(attrs={'name': 'description'})['content'].encode('utf-8')
except:
    desc = "no description  found"
        
try:
    image = soup.find("meta", property="og:image")['content'].encode('utf-8')
except:
    image = "no image found"

        
try:
    try:
        keywords = soup.find(attrs={'name': 'Keywords'})['content'].encode('utf-8')
    except:
        keywords = soup.find(attrs={'name': 'keywords'})['content'].encode('utf-8')
except:
    keywords = 'NA'



print "Title : ",title
print "Image : ",image
print "Description : ",desc
print "Keywords : ",keywords
