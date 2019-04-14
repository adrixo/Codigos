# -*- coding: utf-8 -*-

#Biblioteca para el manejo de matrices
import numpy as np
import itertools
import AlgebraLineal

def longitudDesdeGeneradora(matrizGeneradora):
    return matrizGeneradora.shape[1] #el numero de columnas es la longitud

def dimensionDesdeGeneradora(matrizGeneradora):
    return np.linalg.matrix_rank(matrizGeneradora) #coincide con el numero filas



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
    minimaDistancia = 31415
    i = -1
    for palabra1 in diccionario:
        i += 1
        j = -1
        for palabra2 in diccionario:
            j += 1
            if i>=j:
                continue
            distancia = distanciaHamming(palabra1,palabra2)
            if minimaDistancia > distancia:
                minimaDistancia = distancia
    return minimaDistancia

#Dado un diccionario se calcula cual es mas cerca cero
def pesoHammingCodigo(diccionario):
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

def calcularDistanciaMinimaDesdeControl():
    return 3

# se obtiene el diccionario con las palabras
def calcularTodasPalabras(clase, dimension, matrizGeneradora):
    diccionarioArray = []
    diccionario_CoDec = {}
    combinaciones = map(list, itertools.product(range(clase), repeat=dimension))
    #print(lst) #nos da todas las posibles combinaciones
    #si vamos multiplicando codificamos estas palabras:
    for palabra in combinaciones:
        codificada = codificar(palabra, matrizGeneradora, clase)
        diccionarioArray.append(codificada)
        key = ''.join(str(e) for e in palabra)
        value = ''.join(str(e) for e in codificada)
        diccionario_CoDec.update({key:value})

    return (diccionarioArray, diccionario_CoDec)


#se imprime el diccionario ordenado
def imprimirDiccionario(diccionario_CoDec):
    for decodificada, codificada in diccionario_CoDec.items():
        print(decodificada+ " => " + codificada)

def calcularSindrome(palabra, matrizControl, clase):
    sindrome = np.dot(np.array(palabra), matrizControl)
    sindrome = sindrome % clase
    sindrome = sindrome.tolist()[0]
    return sindrome

def calcularTablaSindromes(capacidadCorreccion, matrizControl, clase):
    combinacionesAux = map(list, itertools.product(range(clase), repeat=matrizControl.shape[0]))
    tablaSindromes = {}
    for e in combinacionesAux:
        if sum(e) <= capacidadCorreccion and sum(e) > 0:
            sindrome = calcularSindrome(e, matrizControl, clase)
            sindrome = ''.join(str(int(s)) for s in sindrome)
            e = ''.join(str(s) for s in e)
            tablaSindromes.update({sindrome:e})
    return tablaSindromes

def decodificacionSindromes(palabra, tablaSindromes, matrizControl, clase):
    print("Decodificando por sindromes: " + ''.join(str(s) for s in palabra))
    sindrome = calcularSindrome(palabra, matrizControl, clase)
    error = []
    if sum(sindrome) == 0:
        print("La palabra no contiene ningun error")
        return palabra
    for sin, e in tablaSindromes.items():
         sin = [int(d) for d in str(sin)]
         if sindrome == sin:
             error = [int(d) for d in str(e)]
             break

    if len(error) == 0:
        print("No se pudo decodificar por sindromes. ")
        return error

    else:
        for i in range(len(palabra)):
            palabra[i] = (palabra[i] + error[i]) % clase
        print("La palabra contenia el error " + ''.join(str(s) for s in error) + " y ha sido decodificada como " + ''.join(str(s) for s in palabra))


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

#https://es.wikipedia.org/wiki/Subespacio_vectorial
# En álgebra lineal, un subespacio vectorial es el subconjunto de un espacio vectorial, que satisface por sí mismo la definición de espacio vectorial con las mismas operaciones que V.
# Toda combinacion de palabras da como resultado otra palabra
def esCodigoLineal(diccionario, matrizControl, clase):
    for palabra1 in diccionario:
        for palabra2 in diccionario:
            palabraAux = [0 for i in range(len(palabra1))]
            for i in range(len(palabra1)):
                palabraAux[i] = (palabra1[i] + palabra2[i]) % clase
            sin = calcularSindrome(palabraAux, matrizControl, clase)
            if(sum(sin) != 0):
                #El codigo no es lineal
                return False
    return True
