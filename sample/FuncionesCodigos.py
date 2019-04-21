# -*- coding: utf-8 -*-

#Biblioteca para el manejo de matrices
import numpy as np
import itertools
import AlgebraLineal
from math import factorial, log

# Dado que codificamos una palabra multiplicandola por la matriz generadora, el numero de filas será la longitud de la palabra origen y el numero de columnas será la longitud del codigo
# input: matriz generadora
# output: longitud del codigo (n columnas de la matriz generadora)
def longitudDesdeGeneradora(matrizGeneradora):
    return matrizGeneradora.shape[1]

# Dado que codificamos una palabra multiplicandola por la matriz generadora, la dimension del codigo es el numero de filas de la matriz generadora que al ser base coincide con el rango
# input: matriz generadora
# output: dimension del codigo (rango de la matriz generadora)
def dimensionDesdeGeneradora(matrizGeneradora):
    return np.linalg.matrix_rank(matrizGeneradora) #que tambien coincide con el numero filas

# La matriz de control nos indica, al ser multiplicada por una palabra, si esta pertenece al codigo, por lo que debe tener n filas = longitud codigo
# input: matriz de control
# output: longitud del codigo (n filas de matriz de control)
def longitudDesdeControl(matrizControl):
    return matrizControl.shape[0]

# Al obtener a partir de una matriz generadora su sistematica se eliminan k columnas y nos quedan n-k (digitos de redundancia) columnas. por lo que sabiendo que n filas = n :
# n = filas
# columnas = n - k => k = n - columnas
# input: matriz de control
# output: dimension del codigo
def dimensionDesdeControl(matrizControl):
    # n-k = numero columnas H
    return matrizControl.shape[0] - matrizControl.shape[1]

# Definicion: Dados dos vectores se define como distancia de hamming como el numero de coordenadas distintas
# Input: dos palabras como listas
# Output: numero de coordenadas distintas
def distanciaHamming(palabra1,palabra2):
    distancia = 0
    for i in range(len(palabra1)):
        if palabra1[i] != palabra2[i]:
            distancia += 1
    return distancia
    # Se verifican los axiomas de distancias:
    # 1. Definida positiva: La distancia siempre es igual o mayor que 0
    # 2. Simetrica: La distancia entre 1 y 2 es la misma que 2 y 1
    # 3. Desigualdad triangular: d(u,v) <= d(u,w) + d(w,v)

# Definicion: El peso de hamming de un vector es el n de sus componentes distintas de 0
# Input: una palabra como lista
# Output: numero de coordenadas distintas de 0
def pesoHammingVector(palabra):
    peso = 0
    for i in range(len(palabra)):
        if palabra[i] != 0:
            peso += 1
    return peso

# Definicion: Dad un codigo C la distancia minima de c es la menor distancia de hamming entre dos palabras del codigo
# Input: diccionario con todas las palabras de un codigo
# Output: minimo peso
def pesoHammingCodigo(diccionario):
    pesoMin = 31415
    for palabra in diccionario:
        peso = 0
        for letra in palabra:
            if letra != 0:
                peso += 1

        #ignoramos si la palabra comparada es vacia tmb
        if peso == 0:
            continue

        if peso < pesoMin:
            pesoMin = peso

    return pesoMin


# Def: Distancia minima de hamming de un codigo C es la distancia minima entre dos palabras
# Input: un diccionario con todas las palabras en el codigo se calcula la minima distancia entre dos de ellas
# output: distancia minima
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

# La distancia minima de un codigo lineal C coincide con el minimo n de filas lin. dependientes de una matriz de control
# Input: matriz de control, longitud del codigo y alfabeto
# Output: distancia minima, tras recorrerse las filas de la matriz comprobando las distintas combinaciones posibles.
def distanciaMinimaHammingDesdeControl(matrizControl, longitud, clase):
    filas = list(np.array(matrizControl))
    nCombinaciones = 1
    nFila = 0 #fila a evaluar que es combiancion de otros nCombinaciones filas
    while nCombinaciones < longitud - 1:
        # tomamos la fila
        fila = filas[nFila]
        # y probamos a ver si se puede obtener como combinacion de las demas
        filasAux = filas[:]
        filasAux.pop(nFila)

        combianciones = itertools.combinations(filasAux, nCombinaciones)
        for c in combianciones:
            filaAux = [0 for x in range(len(fila))]
            for i in range(len(c)): #por cada fila en la combinacion
                for j in range(len(filaAux)): #por cada letra en la fila
                    filaAux[j] = (filaAux[j] + c[i][j]) % clase
            #Si la combinacion da resultado a la fila hemos terminado y la distancia es nCombinaciones + 1
            fin = True

            for i in range(len(fila)):
                if fila[i] != filaAux[i]:
                    fin = False
            if fin:
                return nCombinaciones + 1

        nCombinaciones += 1
    return nCombinaciones + 1

# Formalmente el proceso de codificacion se puede expresar como una aplicacion inyectiva x: F^k -> F^n
# El codigo c asociado sera e = Im(x)
# Por lo que codificar un vector sera multiplicarlo por su matriz generadora
# input: palabra a codificar, matriz generadora y clase (alfabeto)
# output: palabra codificada (lista)
def codificar(palabra, matrizGeneradora, clase):
    codificada = np.dot(np.array(palabra), matrizGeneradora)
    codificada = codificada % clase
    codificada = codificada.tolist()[0]
    return codificada

# El numero de palabras de un codigo viene dado por el n elementos en el alfabeto elevado a la dimension
# Observacion: En codigos no lineales para cuantificar la cantidad de inf en cada vector se utiliza log clase M
# input: clase y dimension
# output:  M numero de palabras asociado a un codigo
def numeroPalabras(clase, dimension):
    return clase**dimension

# Si como se explica en codificar() podemos obtener una palabra del codigo como la multiplicacion de un vector de long k por la matriz generadora k*n
# Podemos calcular todas las palabras del codigo multiplicando todas los posibles combinaciones de vectores de longitud k por la matriz generadora
# input: clase, dimension k, matriz generadora (np.matriz)
# output: palabras del codigo(lista de listas)
#         diccionarioPython (palabra decodificada, palabra codificada)
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


# input: diccionarioPython
# output: se imprime por columans el diccionario
def imprimirDiccionario(diccionario_CoDec):
    for decodificada, codificada in diccionario_CoDec.items():
        print(decodificada+ " => " + codificada)

# La tasa de informacion R de un codigo lineal es k/n
def tasaInformacion(dimension, longitud):
    return dimension/float(longitud)

# La distancia relativa g de un codigo es d/n
def distanciaRelativa(distancia, longitud):
    return distancia/float(longitud)

# Definicion: Se dice que un codigo tiene capacidad de deteccion s si es capaz de detectar s errores en un vector y no s+1
# Esta viene definida como s = d-1
# puesto que si la distancia d separa a dos palabras c',c'' toda palabra que
# se encuentre a d distancia de c' o mas estará mas cerca de c'' que de c' y por tanto
# sera mas entendible que se produjese como un error de c'' que de c'
def capacidadDeteccion(distancia):
    return distancia-1

# Definicion: Se dice que un codigo es t-corrector si es capaz de corregir (t-1)//2 errores
# teniendo en cuenta que entre dos palabras c',c'' hay una distancia d
# si se produce un error de distancia d' solo podemos asumir su correccion si
# el d' se encuentra a menos de la mitad entre las dos palabras
# y en caso de que fuese d' = d/2 no podriamos determinar si la palabra con error
# pertenece a c' o c''
def capacidadCorreccion(distancia):
    return(distancia-1)//2

# Se pueden tomar en cuenta distintas formulas para valorar la relacion k, d en un codigo de longitud n
# La relacion mas conocida es conocida como la cota de singleton:
# donde si d <= n-k+1
# se puede decir que tenemos un codigo MDS (minimun distance separable)
def cotaSingleton(longitud, dimension, distancia):
    # distancia <= longitud-dimension + 1
    # ó
    # distancia+dimension <= longitud+1
    if distancia+dimension  <= longitud+1:
        return True
    else:
        return False
    # Como H tiene n-k columnas, n-k+1 filas siempre seria linealmente dependientes
    # entonces el min numero de filas ld es <= n-k+ y como entendemos que la distancia
    # minima en un codiog lineal coincide con el minimo numero de filas ld

# Una vez tenemos definida la matriz generadora sistematica, podemos obtener la matriz de control
# Si G = ( Id(K) | A )
#    H = ( -A.T | Id(n-k) )
# input: matriz generadora sistematica (np.matriz)
# output: matriz de control sistematica (np.matriz)
def calcularMatrizControl(matrizGeneradora, longitud, dimension):
    #como la matriz es sistematica descartamos la identidad que debería estar a la izquierda
    A = matrizGeneradora[:,dimension:]
    Id = np.identity(longitud - dimension) # puesto que necesitamos una matriz Id de n-k
    return np.bmat([[A],[Id]]).astype(int)

# Una vez tenemos definida la matriz de control sistematica, podemos obtener la matriz generadora
# si H = ( -A.T | Id(n-k) )
#    G = ( Id(K) | A )
# input: matriz de control sistematica (np.matriz)
# output: matriz generadora sistematica (np.matriz)
def calcularMatrizGeneradora(matrizControl, longitud, dimension):
    #como la matriz es sistematica descartamos la identidad que debería estar debajo
    A = matrizControl[:longitud-(longitud-dimension),:]
    Id = np.identity(dimension)
    return np.bmat([Id,A]).astype(int)

# definicion: Se llama sindrome de un vector s(v) a v*H
#   si v € Codigo s(v)={0}
# input: palabra (lista), matriz de control (np.array), clase
# output: sindrome (lista)
def calcularSindrome(palabra, matrizControl, clase):
    sindrome = np.dot(np.array(palabra), matrizControl)
    sindrome = sindrome % clase
    sindrome = sindrome.tolist()[0]
    return sindrome

# Si v es palabra del codigo S(v) = 0
# si tomamos u como v + error:  u = v + e  => S(u) = S(v) + S(e)
#   Por lo que tomando una tabla de sindromes con todos los posibles errores corregibles se puede detecar en que posicion se produjo el error
# Esta funcion obtiene los sindromes de todos los posibles errores que se pudiesen detectar y la devuelve como diccionario
# input: capacidad de deteccion (para calcular los sindromes correspondientes)
#        matriz de control (np.array)
#        clase
# output: tabla sindromes (diccionario con sindrome, error como strings)
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

# El algoritmo de decodificacion por sindromes permite detectar t errores de una palabra
# 1. se calcula el sindrome s(palabra)
# 2. si s(palabra) != {0} buscamos el sindrome en la tabla y tomamos el correspondiente error
# 3. devolvemos palabraSinErro: palabra + error
# input: palabra (lista)
#        tablaSindromes (diccionario sindrome,errror como strings)
#        matriz de control (np.matriz)
#        clase
# output; palabraCorregida (lista)
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

# nCombinaciones: Puede ser deteccion, correccion
def probabilidadTransmision(probabilidadError, longitud, nCombinaciones, paquetesEnviados=1):
    #https://es.wikipedia.org/wiki/Combinatoria
    def combinatorial(m, n):
        return factorial(m) // (factorial(n) * factorial(m - n))

    total = 0
    for i in range(0,nCombinaciones):
        total += combinatorial(longitud,i)*(probabilidadError**i)*(1-probabilidadError)**(longitud-i)
    return total**paquetesEnviados

#capacidadDelCanal
def teoremaShanon(probabilidadError):
    capacidadDelCanal = 1 + probabilidadError*log(probabilidadError,2) + (1-probabilidadError)*log(1-probabilidadError,2)
    return capacidadDelCanal

def redundanciaMinimaShanon(probabilidadError, bitsTransmitir):
    dimension = bitsTransmitir
    longitud = bitsTransmitir
    capacidadDelCanal = teoremaShanon(probabilidadError)
    while dimension/float(longitud) > capacidadDelCanal:
        longitud += 1

    print("Para transmitir %d bits de informacion por un canal binario con probabilidad de error: %f y capacidad: %f necesitamos al menos %d bits de redundancia: %d/%d = %f" % (bitsTransmitir, probabilidadError, capacidadDelCanal, longitud - dimension, dimension, longitud, dimension/float(longitud)) )
    return longitud - dimension

#https://es.wikipedia.org/wiki/Subespacio_vectorial
# En álgebra lineal, un subespacio vectorial es el subconjunto de un espacio vectorial, que satisface por sí mismo la definición de espacio vectorial con las mismas operaciones que V.
# definicion: Un codigo lineal es un subespacio vectorial
# cualesquiera dos palabras del codigo sumadas dan como resultado otra palabra de este
# input: diccionario con todas las palabras (lista de listas)
#        matriz de control (np.matriz)
#        clase (int)
# output: bool
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
