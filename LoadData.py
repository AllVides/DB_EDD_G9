import csv

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
    
    def CargarCSV(self,pathCSV):
        with open(pathCSV) as file:
            lector=csv.reader(file,delimiter="$")
            for fila in lector:
                print("nombre base :{0} , tablas : {1}, tuplas : {2}".format(fila[0],fila[1],fila[2]))

    

d=Data()
d.CargarCSV("/home/msaban/Escritorio/DB_EDD_09/cargar.csv")