__author__ = 'Matias'
import csv
import math
import operator


# Script de pruebas para prototipar TP

# Calcula la distancia
def get_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1))



# Apertura y lectura del archivo csv usando keys definidas en fields

dataRowsDic = []
fields = ['Dates', 'Category', 'Descript', 'DayOfWeek', 'PdDistrict', 'Resolution', 'Address', 'X', 'Y']

with open('train.csv', 'rb') as train_file:
    trainData = csv.DictReader(train_file, fieldnames=fields)
    header = trainData.next()

    # Ejemplo de acceso a un row de datos
    # dato = lectorArchivoTrain.next()
    # print "%s %s" %(dato['Dates'], dato['Category'])

    it = iter(trainData)

    for i in it:
        dataRowsDic.append(i)

#  Genera una lista de diccionarios {'Category':nroCrimenes}

numberOfCrimes = {}

for i in range(0, len(dataRowsDic)):

    delito = dataRowsDic[i]['Category']

    if (numberOfCrimes.has_key(delito)):
        cant = numberOfCrimes.get(delito)
        cant = cant + 1
        numberOfCrimes[delito] = cant
    else:
        numberOfCrimes[delito] = 1

# Genera una lista con las distancias de cada punto al punto de referencia

distancesToRef = []

xRef = float(dataRowsDic[75000]['X'])
yRef = float(dataRowsDic[75000]['Y'])

for i in range(0, len(dataRowsDic)):

    x1 = float(dataRowsDic[i]['X'])
    y1 = float(dataRowsDic[i]['Y'])

    distancia = get_distance(xRef, yRef, x1, y1)

    dic = {'X': x1, 'Y': y1, 'Distance': distancia, 'Category': dataRowsDic[i]['Category']}

    distancesToRef.append(dic)

sortedDistances = sorted(distancesToRef, key=lambda k: k['Distance'])

crimesWeight = {}

# peso=(distanciaLejano-distanciaActual)/(distanciaLejando-distanciaCercano)

nearestPoint = sortedDistances[1]['Distance']
fartherPoint = sortedDistances[1000]['Distance']

for i in range(1, 1000):

    crimeCategory = sortedDistances[i]['Category']
    distance = sortedDistances[i]['Distance']

    weight = (fartherPoint - distance) / (fartherPoint - nearestPoint)

    if (crimesWeight.has_key(crimeCategory)):
        pesoTotal = crimesWeight.get(crimeCategory)
        pesoTotal = pesoTotal + weight
        crimesWeight[crimeCategory] = pesoTotal
    else:
        crimesWeight[crimeCategory] = weight

print max(crimesWeight.iteritems(), key=operator.itemgetter(1))
print crimesWeight

# datosMapeados = map(lambda x:[x['Category'],1],listaDatos)
# datosReducidos = reduce(lambda x,y:if(x[0]==y[0]))
# print datosMapeados
# Escritura de archivo de salida

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
