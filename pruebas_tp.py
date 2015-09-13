__author__ = 'Matias'
import csv
import math
import operator

#Script de pruebas para prototipar TP

def obtenerdistancia(x1,y1,x2,y2):
    return math.sqrt((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1))

fields = ['Dates', 'Category', 'Descript', 'DayOfWeek', 'PdDistrict', 'Resolution', 'Address', 'X', 'Y']

#Apertura y lectura del archivo csv usando keys definidas en fields
listaDatos =[]
with open('train.csv', 'rb') as train_file:
    lectorArchivoTrain = csv.DictReader(train_file, fieldnames = fields)
    header = lectorArchivoTrain.next()
    #dato = lectorArchivoTrain.next()

    #Ejemplo de acceso a un row de datos
    #print "%s %s" %(dato['Dates'], dato['Category'])

    it = iter(lectorArchivoTrain)

    for i in it:
        listaDatos.append(i)

dic_cant_delitos = {}

for i in range(0,len(listaDatos)):

    delito = listaDatos[i]['Category']

    if(dic_cant_delitos.has_key(delito)):
        cant = dic_cant_delitos.get(delito)
        cant = cant+1
        dic_cant_delitos[delito] = cant
    else:
        dic_cant_delitos[delito] = 1



#Procesamiento

listaDistancias = []

xref = float(listaDatos[75000]['X'])
yref = float(listaDatos[75000]['Y'])

for i in range(0,len(listaDatos)):

    x1=float(listaDatos[i]['X'])
    y1=float(listaDatos[i]['Y'])

    distancia = ObtenerDistancia(xref,yref,x1,y1)

    dic = {'X':x1, 'Y':y1, 'Distancia':distancia, 'Category':listaDatos[i]['Category']}

    listaDistancias.append(dic)

lista_ordenada = sorted(listaDistancias, key=lambda k: k['Distancia'])

dic_delitos={}

#peso=(distanciaLejano-distanciaActual)/(distanciaLejando-distanciaCercano)

distanciaMasCercano = lista_ordenada[1]['Distancia']
distanciaMasLejano = lista_ordenada[1000]['Distancia']

for i in range(1,1000):

    delito = lista_ordenada[i]['Category']
    distancia = lista_ordenada[i]['Distancia']

    peso = (distanciaMasLejano-distancia)/(distanciaMasLejano-distanciaMasCercano)

    if(dic_delitos.has_key(delito)):
        pesoTotal = dic_delitos.get(delito)
        pesoTotal = pesoTotal+peso
        dic_delitos[delito]=pesoTotal
    else:
        dic_delitos[delito]=peso


print max(dic_delitos.iteritems(), key=operator.itemgetter(1))
print dic_delitos

# datosMapeados = map(lambda x:[x['Category'],1],listaDatos)
# datosReducidos = reduce(lambda x,y:if(x[0]==y[0]))
# print datosMapeados
#Escritura de archivo de salida

"""
with open('salida.csv','wb') as salida_file:
    salida_file = csv.DictWriter(salida_file, fieldnames = fields)
    salida_file.writeheader()
    salida_file.writerows(listaDatos)

print listaDatos[0]['Category']

print listaDatos[0]
print listaDatos[1]
"""
print "termine"

#prueba223445

