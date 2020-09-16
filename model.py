class ElementiEiLeidu(Exception):
    pass

class Model:
    def __init__(self, p_elemendid):
        self.lisa_elemendid(p_elemendid)

    def lisa_elemendid(self, p_elemendid):
        # siin luuakse globaalselt nähtav muutuja
        global elemendid
        elemendid = p_elemendid

    def loe_elemendid(self):
        return elemendid

    def loe_element(self, nimetus):
        nimetused = []
        for element in elemendid:
            nimetused.append(list(element.values())[0])
        if nimetus in nimetused:
            return elemendid[nimetused.index(nimetus)]
        else:
            raise ElementiEiLeidu

    def kustuta_elemendid(self):
        global elemendid
        elemendid.clear()