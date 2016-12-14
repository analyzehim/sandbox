import requests
import xml.etree.ElementTree as etree
from bs4 import BeautifulSoup



url = "http://pikabu.ru/story/perfektsionizm_v_belarusi_4685676#comments"
r = requests.get(url)
html_doc = r.content
'''
f = open("1.txt","w")
print "OK"
#print r.content
f.write(r.content)
f.close()
'''
soup = BeautifulSoup(html_doc, 'html.parser')
comment_list = soup.find('div', 'b-comment')
print comment_list





