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

from zlib import adler32

from seloger.contact import Contact
from seloger.photo import Photo


class Annonce:

    def __init__(self):
        self._cur = None
        self._curval = None

        self.photos = list()


    def __hash__(self):
        return adler32(self.descriptif.encode() if "descriptif" in self.__dict__ else b"",
                       adler32(self.prix.encode() if "prix" in self.__dict__ else b"",
                               adler32(self.nbPhotos.encode() if "nbPhotos" in self.__dict__ else b"0")))


    def startElement(self, tag, attrs):
        if tag == "photo":
            self._cur = Photo()
        elif tag == "contact":
            self._cur = Contact()
        elif self._cur is not None:
            if not isinstance(self._cur, str):
                self._cur.startElement(tag, attrs)
            else:
                ...
        else:
            self._cur = tag
            self._curval = ''

    def characters(self, content):
        if self._cur is not None:
            if isinstance(self._cur, str):
                self._curval += content
            else:
                self._cur.characters(content)

    def endElement(self, tag):
        if tag == "contact":
            self.__dict__[tag] = self._cur
        elif tag == "photos":
            pass
        elif tag == "photo":
            self.photos.append(self._cur)
        elif isinstance(self._cur, str) and self._cur == tag:
            self.__dict__[tag] = self._curval
        elif self._cur is not None:
            try:
                self._cur.endElement(tag)
            except:
                print(self._cur)
            return  # Skip _cur reset
        self._cur = None
