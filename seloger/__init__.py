from enum import Enum


idTypeBien = {
    "1": "appartement",
    "2": "maison",
    "3": "parking",
    "4": "terrain",
    "6": "boutique",
    "7": "local commercial",
    "8": "bureaux",
    "9": "loft",
    "11": "immeuble",
    "12": "bâtiment",
    "13": "château",
    "14": "hôtel particulier",
    "15": "programme neuf",
}


class TypeTransaction(Enum):
    LOCATION = 1
    ACHAT = 2


class TypeBien(Enum):
    APPARTEMENT = 1
    MAISON = 2
    PARKING = 3
    TERRAIN = 4
    BOUTIQUE = 6
    LOCAL_COMMERCIAL = 7
    BUREAUX = 8
    LOFT = 9
    IMMEUBLE = 11
    BATIMENT = 12
    CHATEAU = 13
    HOTEL_PARTICULIER = 14
    PROGRAMME_NEUF = 15
