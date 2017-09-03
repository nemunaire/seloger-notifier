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

import json
from urllib.request import urlopen
from urllib.parse import urlencode


def get_localisation(city):
    return json.loads(urlopen("http://autocomplete.svc.groupe-seloger.com/auto/complete/0/ALL/6?" + urlencode({"text": city})).read().decode("utf-8"))
