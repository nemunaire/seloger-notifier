import json
from urllib.request import urlopen
from urllib.parse import urlencode


def get_localisation(city):
    return json.loads(urlopen("http://autocomplete.svc.groupe-seloger.com/auto/complete/0/ALL/6?" + urlencode({"text": city})).read().decode("utf-8"))
