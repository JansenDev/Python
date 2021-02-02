from bs4 import BeautifulSoup
import requests
import re


#*Declarar datos

buscar = input("\nBuscar precio de Juego: ")
url2 = "https://store.steampowered.com/search/?term={}".format(buscar)

preciosDescuentosList = []
precios_descuentosList = []
descuentosList = []
preciosList=[]
nombresList=[]

#*Hacer consulta
html = requests.get(url2)
soup = BeautifulSoup(html.content , 'html.parser')

#*Obetener datos del HTML
nombresHtmlList = soup.find_all("span", class_="title")
preciosDescuentosHtmlList = soup.find_all("div", class_="search_price" )
divImgHtmlList = soup.find_all("div", class_="search_capsule" )

imgHtmlList = [tagImg.img for tagImg in divImgHtmlList]
srcList = [src.get("src") for src in imgHtmlList]

#*Parse: from "bs4.element.ResultSet" to "class.list"
nombresList = [x.text.strip() for x in nombresHtmlList]

#*Separa el 'PrecioDescuento' obtenido con RegEx 
for i in range(len(preciosDescuentosHtmlList)) :
    preciosDescuentosList.append(preciosDescuentosHtmlList[i].text.strip())
    precioEncontrado = re.findall(r"S/\.\d\d?\d?\.\d{2}",preciosDescuentosList[i])
    precios_descuentosList.append(precioEncontrado)

## Guarda Precios y Decuentos en listas separadas
# [preciosList.append(x) if len(x) == 1 else descuentosList.append(x) 
# for x in precios_descuentosList if x != [] ]

#*Guardar [precios, descuento] en preciosList
[preciosList.append(x) for x in precios_descuentosList ]

#*Imprime resultados
print("="*34)
print("\tResultados de: {}".format(buscar))
print("="*34)
for index in range(len(preciosDescuentosList)):
    print("\nNombre: {}".format(nombresList[index]))

    if len(preciosList[index]) == 1:
        print ("Descuento: {}".format(preciosList[index][0]))

    if len(preciosList[index]) == 2:
        print ("Precio: {}".format(preciosList[index][0]))
        
    if(re.search(r'^Free',preciosDescuentosList[index])):
        print ("Precio: {}".format(preciosDescuentosList[index]))

    if( len(preciosList[index]) == '' ):
        print ("Precio: No disponible")

    print ("Imagen: {}\n".format(srcList[index]))










# !  Metodo: 
# ! .strip() = devuelve una copia de la cadena eliminando tanto los caracteres iniciales como los finales. El espacio es el caracter predeterminado para eliminar.
# ! .strip(characters) = Elimina los caracteres iniciales y finales segun el parametro introducido