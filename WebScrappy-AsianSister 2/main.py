import time
from bs4 import BeautifulSoup 
import requests
import re , os ,sys
import threading
import logging
import queue

formato = '%(name)s-%(name)s - %(message)s'
# logging.basicConfig(format=formato, level=logging.DEBUG)

# log = logging.getLogger('bsoup')

URL = "https://asiansister.com/"

##Metodos
def printProgressBar (iteration, total, prefix = 'Progress', suffix = 'Complete', decimals = 1, length = 50, fill = '█', printEnd = "\r"):

    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()

def getNameSRC_album(image_url, album=True):
    albumNameRegex   = r"images(?=\/).+\.(JPG|jpg|png|GIF)"
    imageNameRegex   = r"(?<=\/)[\d_]+[\w\d]+()\.(JPG|jpg|png|GIF)"

    regex = albumNameRegex if album else imageNameRegex
    name = re.search(regex, image_url)
    # print("nombre es: {}".format(name.group()))
    return name.group()

def create_album(album_name, album_path="album"):
    path_directory  = os.path.join(os.getcwd(), album_path)
    path_album = os.path.join(path_directory,album_name)

    if not os.path.exists(path_directory):
        os.mkdir(path_directory)
        print("\n-Directory \'{}\' created.".format(album_path))

    if not os.path.exists(path_album):
        os.mkdir(path_album)
        print("\n-Album created. \'{}\'".format(album_name))
        # print(path_album)

def download_image(url,album_name_directory):

    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
    headers={'User-Agent':user_agent,}
    # headers={'User-Agent':'whatever',} 

    img_name = getNameSRC_album(url, album=False)
    path_directory = os.path.join( os.getcwd(), 'album',album_name_directory ,img_name )
    
    try:
        #*Primera forma 
        # #!Request at server adding headers
        # img_request = urllib.request.Request(url,None, headers)

        # #!Respuesta en bruto 
        # response = urllib.request.urlopen(img_request)
        # data = response.read()


        # with open(path_directory,'wb') as f:
        #     f.write(data)
        # print("%s downloaded.!"%img_name)

        #*Segunda manera    
        data = requests.get(url,headers=headers)
        with open(path_directory,'wb') as f:
            f.write(data.content)
        # print("%s downloaded.!"%img_name)
    except Exception as e:
        # log.debug(e)
        print(e)

def download(q, album_name_directory, array_size):
    # for i,src in enumerate(src_List):

    while True:
        item_src = q.get()
        total = len(array_size)
        iteracion = total- q.qsize()
        suffix='Progress {0}/{1}'.format(iteracion, total)
        # print(itera)
        download_image(item_src, album_name_directory)
        # print(item_src)
        printProgressBar(iteracion,len(array_size), suffix)
        q.task_done()

    # for i in progressBar(array_size):
    #     download_image(q.get(),album_name_directory)
    #     q.task_done()

    
    # log.debug("Finish Thread.!")

#Funciones Principales

def main_single(uri_cosplayer=None):
    URL_COSPLAYER = uri_cosplayer if uri_cosplayer else input("[Album] Asian Sister link> ") 

    html            = requests.get(URL_COSPLAYER).content
    soup            = BeautifulSoup(html,'html.parser')
    html_imgList    = soup.find_all('img',class_='showMiniImage')
    album_name_dir  = soup.find('h1').text.strip()
    link_list       = [ URL+getNameSRC_album( src.get('dataurl')    ) for src in html_imgList ]

    create_album(album_name_dir)
    print("\nAlbum \t: %s"%album_name_dir)
    print("Size \t: %s files\n"%len(html_imgList))


    # *Primera forma de hilos
    num_threads = 4
    q = queue.Queue()

    tstart = time.time()
    for i in range(num_threads):
        x = threading.Thread(target=download, args=(q ,album_name_dir, link_list ))
        x.setDaemon(True)
        x.start()

    for i in link_list:
        q.put(i)
    q.join()
    tend = time.time()

    print("\nDownloaded %s files in: %s"%(len(html_imgList),tend-tstart))

    #*Segunda forma de multiprocesos con concurrent.futures
    # with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    #     for index in range(3):
    #         executor.submit(download, links_allList[index],album_name_dir )

def main_list(url_albumList=None):
    
    url_albumList       = url_albumList if url_albumList else input('[Albums] Asian Sister link> ')
    html                = requests.get(url_albumList)
    soup                = BeautifulSoup(html.content,"html.parser")
    album_itemsEnbruto  = soup.find_all('div', class_='itemBox')
    album_itemsList     = [URL+item.a.get('href').strip() for item in album_itemsEnbruto]

    print("%s albums to download."%len(album_itemsList))

    for url in album_itemsList:
        main_single(url)

    print("%s albums was downloaded."%len(album_itemsList))

#Funcion Principal
def main():
    arg_list = sys.argv

    if len(arg_list) > 1:
        url = arg_list[1]

        if len(arg_list) > 2:
            albums_cod  = arg_list[2]

            if albums_cod == '-s':
                main_list(url)
                return
            return    
        main_single(url)
        return 

    main_single()


if __name__ == '__main__':
    main()
    # main_single()
    # main_list()