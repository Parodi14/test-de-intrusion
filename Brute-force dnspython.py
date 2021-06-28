#!/usr/bin/env python
# _*_ coding: utf8 _*_

""" ********************************
autor : aaron.parodip@codeecuador.com

ultima vez editado: 28/06/2021 15:15
*********************************"""


import dns.resolver


def main():
    consulta = ['A', 'NS', 'SOA', 'MF', 'MD', 'CNAME', 'MB', 'MG', 'NULL', 'WKS', 'PTR', 'TXT']
    for c in consulta:
        try:
            a = dns.resolver.resolve("facebook.com", c)
            for q in a:
                print(q)
        except:
            print("No puedo obtener la consulta")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
