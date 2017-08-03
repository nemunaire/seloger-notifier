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
