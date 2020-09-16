from model import Model
from view import View
from controller import Controller

kaubad = [
    {"nimetus": "leib", "hind": 0.80, "kogus": 20},
    {"nimetus": "piim", "hind": 0.50, "kogus": 15},
    {"nimetus": "vein", "hind": 5.60, "kogus": 5},
]

pood = Controller(Model(kaubad), View())

pood.kuva_elemendid()
pood.kustuta_elemendid()