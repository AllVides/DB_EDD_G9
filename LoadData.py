
class Data():
    
    def CargarArchivo(self,pathCSV):
        archivo=open(pathCSV,"r")
        datos=""
        for linea in archivo.readlines():
            print (linea)
            datos+=linea
            datos+="\n"

        archivo.close()
        return datos


    

    