# -*- coding: utf-8 -*-

#Biblioteca para el manejo de matrices
import numpy as np
import itertools
import AlgebraLineal

#def
def distanciaHamming(palabra1,palabra2):
    distancia = 0
    for i in range(len(palabra1)):
        if palabra1[i] != palabra2[i]:
            distancia += 1
    return distancia

# Def: Distancia minima de hamming de un codigo C es la distancia minima entre dos palabras
# Dado un diccionario con todas las palabras en el codigo se calcula la minima distancia
# Entre dos de ellas
def distanciaMinimaHammingDesdeDiccionario(diccionario):
    distanciaHamming = 31415
    i = -1
    for palabra1 in diccionario:
        i += 1
        j = -1
        for palabra2 in diccionario:
            j += 1
            if i>=j:
                continue
            distancia = distanciaHamming(palabra1,palabra2)
            if distanciaHamming > distancia:
                distanciaHamming = distancia
    return distanciaHamming

#Dado un diccionario se calcula cual es mas cerca cero
def pesoHammingCodigo(self):
    return 3

#El proceso
def codificar(palabra, matrizGeneradora, clase):
    codificada = np.dot(np.array(palabra), matrizGeneradora)
    codificada = codificada % clase
    codificada = codificada.tolist()[0]
    return codificada

#M es
def numeroPalabras(clase, dimension):
    return clase**dimension

#R es
def tasaInformacion(dimension, longitud):
    return dimension/float(longitud)

#g es
def distanciaRelativa(distancia, longitud):
    return distancia/float(longitud)

#s es
def capacidadDeteccion(distancia):
    return distancia-1

#t es
def capacidadCorreccion(distancia):
    return(distancia-1)//2

#MDS es
def cotaSingleton(longitud, dimension, distancia):
    # distancia <= longitud-dimension + 1
    # distancia + dimension <= longitud + 1
    if distancia <= (longitud-dimension+1):
        return True
    else:
        return False

#Una vez tenemos definida la matriz generadora sistematica, podemos obtener la matriz de control
def calcularMatrizControl(matrizGeneradora, longitud, dimension):
    #como la matriz es sistematica descartamos la identidad que debería estar a la izquierda
    A = matrizGeneradora[:,dimension:]
    Id = np.identity(longitud - dimension) # puesto que necesitamos una matriz Id de n-k
    return np.bmat([[A],[Id]])

#Una vez tenemos definida la matriz de control sistematica, podemos obtener la matriz generadora
def calcularMatrizGeneradora(matrizControl, longitud, dimension):
    #como la matriz es sistematica descartamos la identidad que debería estar debajo
    A = matrizControl[:longitud-(longitud-dimension),:]
    Id = np.identity(dimension)
    return np.bmat([Id,A])

def calcularDistanciaMinimaDesdeControl(self):
    return 3

# se obtiene el diccionario con las palabras
def calcularTodasPalabras(clase, dimension, matrizGeneradora):
    diccionarioArray = []
    diccionario_CoDec = {}
    combinaciones = map(list, itertools.product(range(clase), repeat=dimension))
    #print(lst) #nos da todas las posibles combinaciones
    #si vamos multiplicando codificamos estas palabras:
    for palabra in combinaciones:
        codificada = self.codificar(palabra, matrizGeneradora, clase)
        diccionarioArray.append(codificada)
        key = ''.join(str(e) for e in palabra)
        value = ''.join(str(e) for e in codificada)
        diccionario_CoDec.update({key:value})

    return (diccionarioArray, diccionario_CoDec)

#se imprime el diccionario ordenado
def imprimirDiccionario(diccionario_CoDec):
    for decodificada, codificada in diccionario_CoDec.items():
        print(decodificada+" => " + codificada)

def calcularSindrome( vector):
    return vector*matrizControl

def decodificacionSindromes():
    return 3

def calcularTablaSindromes():
    return 3

def perforar( arrayPosiciones):
    return 3

def acortar( arrayPosiciones):
    return 3

def extender():
    return 3

def probabilidadError():
    return 3

def pesoHammingVector(palabra):
    peso = 0
    for i in range(len(palabra)):
        if palabra[i] != 0:
            peso += 1
    return peso

def distanciaHamming(palabra1,palabra2):
    distancia = 0
    for i in range(len(palabra1)):
        if palabra1[i] != palabra2[i]:
            distancia += 1
    return distancia

def teoremaShanon(self):
    return 3
