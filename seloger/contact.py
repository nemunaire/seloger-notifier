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

class Contact:

    def __init__(self):
        self._cur = None


    def startElement(self, tag, attrs):
        if self._cur is not None:
            ...
        self._cur = ""


    def characters(self, content):
        if self._cur is not None:
            self._cur += content


    def endElement(self, tag):
        if self._cur is not None:
            self.__dict__[tag] = self._cur
        self._cur = None
