import os
from os import listdir
import shutil
from plyer import notification
import logging


formato = f"\n%(name)s -%(levelname)s - %(asctime)s - %(message)s"
logging.basicConfig(level=logging.INFO,format=formato, datefmt='%I:%M:%S')

logger = logging.getLogger('main.py')

exts_images     = ['.png','.jpg','.ico','.jpeg','.gif']
exts_documents  = ['.doc','.pdf','.cvs','.pptx','.docx','.lslx']
exts_videos     = ['.mp4','.mkv','.wmv','.flv','.webm','.avi','.amv']
exts_music      = ['.mp3','.M4A','.opus']
exts_zips       = ['.zip','.rar']

extsList            = exts_images + exts_documents + exts_videos + exts_music + exts_zips


# PATH            = os.getcwd()
PATH            = 'C:\\Users\\segur\\Downloads' #
NEW_DIRECTORIES = ['Compress','Music','Images','Documents','Video']
ARCHIVOS        = listdir( PATH )


def main():
    logger.info( "Path: "+PATH )
    crear_directorios( PATH )
    ordenar_archivos()
    

def crear_directorios(path):

    for carpeta in NEW_DIRECTORIES:
        new_carpeta = os.path.join( path, carpeta )

        if not os.path.exists(new_carpeta):
            os.mkdir(new_carpeta)
            print('%s created. %s'%( carpeta, new_carpeta ))
        
def ordenar_archivos():
    
    message = '{0} files moved.'
    count_files_moved = 0
    for archivo in ARCHIVOS:
        name, extension = os.path.splitext(archivo)
        src     = os.path.join( PATH, archivo)

        #*Zips
        if extension in exts_zips:
            srcdst  = os.path.join( PATH, NEW_DIRECTORIES[0])
            shutil.move(src,srcdst,copy_function=shutil.copy2)
            message += "\n-%s, moved!"%archivo
            count_files_moved = count_files_moved + 1
            
        #*Music
        if extension in exts_music:
            srcdst  = os.path.join( PATH, NEW_DIRECTORIES[1])
            shutil.move(src,srcdst,copy_function=shutil.copy2)
            message += "\n-%s, moved!"%archivo
            count_files_moved = count_files_moved + 1
        
        #*Images
        if extension in exts_images:
            srcdst  = os.path.join( PATH, NEW_DIRECTORIES[2])
            shutil.move(src,srcdst,copy_function=shutil.copy2)
            message += "\n-%s, moved!"%archivo
            count_files_moved = count_files_moved + 1

        #*Documents
        if extension in exts_documents:
            srcdst  = os.path.join( PATH, NEW_DIRECTORIES[3])
            shutil.move(src,srcdst,copy_function=shutil.copy2)
            message += "\n-%s, moved!"%archivo
            count_files_moved = count_files_moved + 1

        #*Video
        if extension in exts_videos:
            srcdst  = os.path.join( PATH, NEW_DIRECTORIES[4])
            shutil.move(src,srcdst,copy_function=shutil.copy2)
            message += "\n-%s, moved!"%archivo
            count_files_moved = count_files_moved + 1

    logger.info(message.format(count_files_moved ))

if __name__ == '__main__':
    main()
