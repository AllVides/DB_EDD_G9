
class Cilindro:
    def __init__(self, nombre, pkeys, ikey):
        self.indice = [None]*30
        self.nombre = nombre
        self.icode = ikey
        self.pkeys = pkeys
        self.seguiente = None
        self.overflow = None

    def _hashl(self, key):
        multi = 1
        hashvalue = 0
        for ch in key:
            hashvalue += multi * ord(ch)
            multi += 1
        return hashvalue % 30

    def _hashn(self, key):
        return key % 30

    def _rehash(self, val):
        return val**2 % 30

    def insert(self, registro):
        key=""
        for k in self.pkeys:
            key+=str(k)
        try:
            

    def update(self, register, val):
        pass

    def delete(self, val):
        pass

    def extractRow(self, val):
        pass

class Registro:
    def __init__(self, valores):
        self.valores = valores

    def alterAddColumn(self):
        pass

    def alterDropColumn(self, ind: int):
        try:
            self.valores.pop(ind)
            return 0
        except:
            return 1