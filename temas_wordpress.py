

import requests
from bs4 import BeautifulSoup


def main():
    agente = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                            'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36'}
    peticion = requests.get(url="https://codeecuador.com", headers=agente)
    soup = BeautifulSoup(peticion.text, 'html5lib') # Parsear el arbol html para buscar los temas utilizados
    for enlace in soup.find_all('link'): # Recorrer los enlaces dentro del codigo fuente
        if '/wp-content/themes/' in enlace.get('href'): # Validamos un string mediante IF para verificar que este dentro de la etiqueta href
            tema = enlace.get('href')
            tema = tema.split('/') # Cada vez que encuentre un slash será considerado un elemento de esa lista
            if 'themes' in tema: # verificar si se encuentra el tema dentro de la lista
                posicion = tema.index('themes')  # .index busca un elemento en especifico
                theme = tema[posicion+1]
                print("\n El tema utilizado es: {}".format(theme))


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
