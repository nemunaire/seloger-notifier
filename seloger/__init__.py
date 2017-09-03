# Basic SDK to interact with seloger.com API
# Copyright (C) 2017  Mercier Pierre-Olivier
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

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
