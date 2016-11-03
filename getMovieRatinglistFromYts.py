from bs4 import BeautifulSoup
import urllib
import requests
movie_dic = dict()
for page in range(10):
    if page == 0:
        html_doc = requests.get('https://yts.ag/browse-movies/0/all/all/7/latest')
    else:
        html_doc = requests.get('https://yts.ag/browse-movies/0/all/all/7/latest?page=%d'%(page))
    plain_text = html_doc.content
    soup = BeautifulSoup(plain_text, 'html.parser')
    links = soup.findAll('a', {'class': 'browse-movie-title'})
    rating = soup.findAll('h4', {'class': 'rating'})



    for i in range(len(links)):
        movie_dic[links[i].text] = rating[i].text

for key,value in movie_dic.items():
    print key+" "+value
    

