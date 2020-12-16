
class Cilindro:
    def __init__(self, nombre, pkeys, ikey):
        self.indx = [None]*30
        self.longi = 30
        self.nombre = nombre
        self.icode = ikey
        self.pkeys = pkeys
        self.seguiente = ikey + 1

    def _hashl(self, key):
        multi = 1
        hashvalue = 0
        for ch in key:
            hashvalue += multi * ord(ch)
            multi += 1
        return hashvalue % 30

    def _hashn(self, key):
        return key % 30

    def _rehash(self, val, i):
        return (val+i)**2 % 30

    def _createKey(self, values):
        key = ""
        for k in values:
            key += str(k)
        try:
            r = int(key)
            return r
        except:
            return key

    def hash(self, val):
        if type(val) is int:
            i = self._hashn(val)
        else:
            i = self._hashl(val)
        return i


    def insert(self, registro):
        try:
            key=[]
            for k in self.pkeys:
                key.append(registro[k])
            keyval = self._createKey(key)
            val = self.hash(keyval)
            while i<3:
                if self.indx[val] == None :
                    self.indx[val] = Registro(registro)
                    return 0
                else:
                    ke = []
                    for k in self.pkeys:
                        ke.append(self.indx[val].valores[k])
                    if self._createKey(ke) == keyval:
                        return 4
                    val = self._rehash(keyval, i)
                i+=1
            else:
                self.indx.append(registro)
                self.longi +=1
        except:
            return 1

    def update(self, register, key):
        try:
            keyval = self._createKey(key)
            val = self.hash(keyval)
            while i < 3:
                ke = []
                for k in self.pkeys:
                    ke.append(self.indx[val].valores[k])
                if self._createKey(ke) == keyval:
                    return self.indx[val].update(register)
                val = self._rehash(keyval, i)
                i += 1
            else:
                for v in range(30, self.longi):
                    ke = []
                    for k in self.pkeys:
                        ke.append(self.indx[v].valores[k])
                    if self._createKey(ke) == keyval:
                        return self.indx[v].update(register)
                else:
                    return 4
        except:
            return 1

    def delete(self, key):
        try:
            keyval = self._createKey(key)
            val = self.hash(keyval)
            while i < 3:
                ke = []
                for k in self.pkeys:
                    ke.append(self.indx[val].valores[k])
                if self._createKey(ke) == keyval:
                    self.indx[val] = None
                    return 0
                val = self._rehash(keyval, i)
                i += 1
            else:
                for v in range(30, self.longi):
                    ke = []
                    for k in self.pkeys:
                        ke.append(self.indx[v].valores[k])
                    if self._createKey(ke) == keyval:
                        self.indx.pop(v)
                        return 0
                else:
                    return 4
        except:
            return 1

    def extractRow(self, key):
        try:
            keyval = self._createKey(key)
            val = self.hash(keyval)
            while i < 3:
                ke = []
                for k in self.pkeys:
                    ke.append(self.indx[val].valores[k])
                if self._createKey(ke) == keyval:
                    return self.indx[val]
                val = self._rehash(keyval, i)
                i += 1
            else:
                for v in range(30, self.longi):
                    ke = []
                    for k in self.pkeys:
                        ke.append(self.indx[v].valores[k])
                    if self._createKey(ke) == keyval:
                        return self.indx[v]
                else:
                    return 4
        except:
            return 1

    def readAll(self):
        data = []
        for x in self.indx:
            if x is None:
                continue
            data.append(x.valores)
        return data

class Registro:
    def __init__(self, valores):
        self.valores = valores

    def update(self, register):
        for k in register:
            try:
                self.valores[k] = register[k]
            except:
                return 1
        return 0

    def alterAddColumn(self):
        pass

    def alterDropColumn(self, ind: int):
        try:
            self.valores.pop(ind)
            return 0
        except:
            return 1