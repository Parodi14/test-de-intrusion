#!/usr/bin/env python
# _*_ coding: utf8 _*_

import requests


def main():
    palabra = "cloudflare"
    url = requests.get("https://codeecuador.com/")
    cabeceras = dict(url.headers)
    verificar = False

    for c in cabeceras:
        if palabra in cabeceras[c].lower():
            break
    if verificar == True:
        print("cloulflare presente")
    else:
        print("El sitio no tiene cloudflare")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Saliendo")
        exit()
