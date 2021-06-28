from Wappalyzer import WebPage, Wappalyzer


def main():
    wap = Wappalyzer.latest()
    try:
        web = WebPage.new_from_url("https://codeecuador.com/")
        tecnologias = wap.analyze(web)
        for t in tecnologias:
            print("\nTecnologia detectada: {}".format(t))
    except:
        print("Ha ocurrido un error")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Saliendo")
        exit()


