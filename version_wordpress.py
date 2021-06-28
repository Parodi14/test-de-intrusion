#!usr/bin/env python
# _*_ coding: utf8 _*_

"""
***Script para analizar versión de wordpress a través de python***
Realizado por: aaron.parodip@codeecuador.com
ultima vez editado: 22/6/2021
"""

import requests
from bs4 import BeautifulSoup


def main():
    url = "https://codeecuador.com"
    cabecera = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64 '
                              'AppleWebKit/537.36 (KHTML, like Gecko)Chrome/80.0.3987.149 Safari/537.36'}
    peticion = requests.get(url=url, headers=cabecera)
    soup = BeautifulSoup(peticion.text,'html5lib')
    for v in soup.find_all('meta'):
        if v.get('name') == 'generator':
            version = v.get('content')
            print("\n La versión de wordpress es: {}".format(version))


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Saliendo")
        exit()
