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
from urllib.request import urlopen
from urllib.parse import urlencode
import xml.parsers.expat

from seloger.annonce import Annonce

class Recherche:

    def __init__(self, response):
        p = xml.parsers.expat.ParserCreate()
        p.StartElementHandler = self.startElement
        p.CharacterDataHandler = self.characters
        p.EndElementHandler = self.endElement

        self._cur = None
        self.annonces = list()

        p.ParseFile(response)


    def startElement(self, tag, attrs):
        if self._cur is not None:
            self._cur.startElement(tag, attrs)
        elif tag == "resume" or tag == "resumeSansTri" or tag == "nbTrouvees" or tag == "pageSuivante" or tag == "nbAffichables" or tag == "pageCourante" or tag == "pageMax":
            self._cur = ""
        elif tag == "annonce":
            self._cur = Annonce()


    def characters(self, content):
        if self._cur is not None:
            if isinstance(self._cur, str):
                self._cur += content
            else:
                self._cur.characters(content)


    def endElement(self, tag):
        if tag == "annonce":
            self.annonces.append(self._cur)
        elif tag == "resume" or tag == "resumeSansTri" or tag == "pageSuivante":
            self.__dict__[tag] = self._cur
        elif tag == "nbTrouvees" or tag == "nbAffichables" or tag == "pageCourante" or tag == "pageMax":
            self.__dict__[tag] = int(self._cur) if isinstance(self._cur, str) else 0
        elif self._cur is not None:
            self._cur.endElement(tag)
            return  # Skip _cur reset
        self._cur = None


def search(**criteres):
    for k in criteres:
        if isinstance(criteres[k], list):
            if criteres[k] and isinstance(criteres[k][0], Enum):
                criteres[k] = map(lambda v: v.value, criteres[k])
            criteres[k] = ','.join(map(str, criteres[k]))
        elif isinstance(criteres[k], Enum):
            criteres[k] = criteres[k].value

    if "tri" not in criteres:
        criteres["tri"] = "d_dt_crea"
    if "SEARCHpg" not in criteres:
        criteres["SEARCHpg"] = 1

    return Recherche(urlopen("http://ws.seloger.com/BaseUrl/search.xml?" + urlencode(criteres)))


def annonces(**criteres):
    pageCourante = 0
    pageMax = 1

    while pageCourante < pageMax:
        pageCourante += 1
        res = search(SEARCHpg=pageCourante, **criteres)
        if hasattr(res, "pageMax"):
            pageMax = res.pageMax
        yield from res.annonces
