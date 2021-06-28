#!/usr/bin/env python
# _*_ coding: utf8 _*_

import dns.resolver
from os import path


def main():
    if path.exists('subdominios.txt'):
        wordlist = open('subdominios.txt', 'r')
        wordlist = wordlist.read().split('\n')
        lista = []
        for s in wordlist:
            try:
                a = dns.resolver.resolve('{}.google.com'.format(s), 'A')
                lista.append('{}.google.com'.format(s))

            except:
                pass
        if len(lista) > 0:
            print('Numero de subdominions posibles:{}'.format(len(lista)))
            for e in lista:
                print(e)
        else:
            print("No se encontraron subdominios")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
