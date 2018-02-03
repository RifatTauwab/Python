from bs4 import BeautifulSoup
import urllib
import requests
import re
import os

def get_video_link(page_link):
    try:
        Files = os.listdir("C:\Users\Md.Rifat-Ut-Tauwab\Downloads\ielts")
        html_doc = requests.get(page_link)
        plain_text = html_doc.content
        soup = BeautifulSoup(plain_text, 'html.parser')
        div = soup.find_all('div', attrs={'class': re.compile('lesson-item')})
        video_name = div[0]['id']+'.mp4'
        print video_name
        if video_name not in Files:
            print len(Files)+1
            download_video(download_url=div[0].img['src'].split('web')[0]+'web.mp4',video_name=video_name)
    except Exception as e:
        print str(e)
        print "unable to fetch information from page link ",page_link

def download_video(download_url=None,video_name=None):
    try:
        path = "C:\Users\Md.Rifat-Ut-Tauwab\Downloads\ielts\%s"%(video_name)
        urllib_obj = urllib.URLopener()
        print "downloading %s ..."%(video_name)
        urllib_obj.retrieve(download_url, path)
        print "download completed"
    except:
        print "download failed"



url = 'https://ielts.magoosh.com'
html_doc = requests.get('https://ielts.magoosh.com/lessons')

plain_text = html_doc.content
soup = BeautifulSoup(plain_text, 'html.parser')
links = soup.find_all("a", href=lambda href: href and "lessons" in href)
print 'total videos :',len(links)
#get_video_link('https://gre.magoosh.com/lessons/963-square-roots')

for link in links :
    get_video_link(url+link['href'])
    





