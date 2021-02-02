 #!/usr/bin/python
 # -*- coding: utf-8 -*-
import urllib.request
from bs4 import BeautifulSoup
import requests
import os
import re

# url     = "https://buondua.com"        
# page    = '?start=0'
# search  ='?search=mini'


def getNameSRC_album(thumbnail_url, album=True):
    albumNameRegex   = r"[\w\-\.]+(rCong.com|album)"
    imagenNameRegex  = r"([\w\-\.])+\.(jpg|png|GIF)"

    regex = albumNameRegex if album else imagenNameRegex
    name = re.search(regex, thumbnail_url)
    # print("nombre es: {}".format(name.group()))
    return name.group()

def create_album(album_name, album_path="album"):
    path_directory  = os.path.join(os.getcwd(), album_path)
    path_album = os.path.join(path_directory,album_name)

    if not os.path.exists(path_directory):
        os.mkdir(path_directory)
        print("-Directory \'{}\' created.".format(album_path))

    if not os.path.exists(path_album):
        os.mkdir(path_album)
        print("-Album  created. \'{}\'".format(path_album))
    

def download_album(url, album_name="unknow"):
    path_directory  = os.path.join(os.getcwd(),"album") 
    album_name      = getNameSRC_album(url)
    image_name      = getNameSRC_album(url,album=False)

    thumbnail_name  = os.path.join(path_directory, album_name, image_name)
    create_album(album_name)
    try:
        print("Downloaded: "+image_name)
        urllib.request.urlretrieve(url, thumbnail_name)
    except Exception as identifier:
        print("Server failed.",identifier)
    


direction       = input("Ingresar link buondua> ")
html    = requests.get(direction).content
soup = BeautifulSoup(html,'html.parser')

nombre = "https://1.bp.blogspot.com/-gRr1GpPJZOE/YAWfTQcJyXI/AAAAAAADC3I/xlvz3-I_iYMddvTnXZG2FsoWljuSSgkGACLcBGAsYHQ/s0/YouMi-Vol.550-Victoria-Guo-Er-MrCong.com-024.jpg"

# thumbnailAlbum  = soup.find(class_='article-introimage')
# titleAlbum      = soup.find(class_='article-header')
gallery         = soup.find(class_="article-fulltext")
images          = gallery.find_all(class_="item-image")
# thumbnail_url   = thumbnailAlbum.img['src'].strip()
# album_title     = titleAlbum.h1.get_text().strip()
print("-Downloading {} files".format(len(images)))


for image in images:
    url = image['data-src']
    download_album(url)







##   Tags
# html    = requests.get(url).content
# soup    = BeautifulSoup(html,'html.parser')
# footer  = soup.find(class_='footer')
# tagsList = footer.select('a', class_='.tag .is-small')

# for tag in tagsList:
#     print (tag.span.get_text())
#     print(url+tag['href'],'\n')
