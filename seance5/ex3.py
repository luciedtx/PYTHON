class Vehicule():
    def init(self, _type, _nbplace):
        self._type = _type
        self._nbplace= _nbplace
    def get_type(self):
        return self._type
    def set_type(self, _type):
        self._type= _type
        return self._type
    def get_nbplace(self):
        return self._nbplace
    def set_nbplace(self, _nbplace):
        self._nbplace= _nbplace
        return self._nbplace