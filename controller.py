from model import ElementiEiLeidu

class Controller:
    def __init__(self, mudel, vaade):
        self.mudel = mudel
        self.vaade = vaade

    def kuva_elemendid(self):
        elemendid = self.mudel.loe_elemendid()
        self.vaade.kuva_elemendid(elemendid)

    def kuva_element(self, nimetus):
        try:
            element = self.mudel.loe_element(nimetus)
        except ElementiEiLeidu:
            self.vaade.veateade("Elementi '{}' ei leidu".format(nimetus))
        else:
            self.vaade.kuva_element(nimetus, element)

    def kustuta_elemendid(self):
        self.mudel.kustuta_elemendid()
        self.vaade.kustuta_elemendid()
