class View:
    def kuva_elemendid(self, elemendid):
        print("Kogu andmestik:")
        # teksti kujundamine:
        # https://docs.python.org/3.4/library/string.html#formatspec
        print("{:<10} | {:>10} | {:>10}".format('nimetus', 'hind', 'kogus'))
        print("------------------------------------")
        for element in elemendid:
            print("{:<10} | {:>10.2f} | {:>10}".format(element['nimetus'], element['hind'], element['kogus']))
        print("")

    def kuva_element(self, nimetus, element):
        if element:
            print("Kuvame elemendi {} andmed:".format(nimetus))
            print("{:<10} | {:>10} | {:>10}".format('nimetus', 'hind', 'kogus'))
            print("------------------------------------")
            print("{:<10} | {:>10.2f} | {:>10}".format(element['nimetus'], element['hind'], element['kogus']))
        else:
            print("Elementi {} ei eksisteeri.".format(nimetus))
        print("")

    def veateade(self, tekst):
        print("")

    def kustuta_elemendid(self):
        print("Kustutan kõik elemendid...".format())
        print("Kõik elemendid kustutatud.")
