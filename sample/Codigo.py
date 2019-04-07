# -*- coding: utf-8 -*-

#Biblioteca para el manejo de matrices
import numpy as np
import itertools
import AlgebraLineal
import FuncionesCodigos as fc

class Codigo:
    clase = 2 #mod 2

    # [n,k,d]
    longitud = 0
    dimension = 0
    distancia = 0

    matrizGeneradora = []
    #rango maximo k
    matrizControl = []
    #n-k columnas
    tablaSindromes = []

    #todas las palabras
    diccionario = []
    diccionario_CoDec = {}
    #Numero de palabras
    M = 0

    #Tasa información
    R=0
    #Distancia relativa
    g=0
    #capacidad deteccion
    s=0
    #capacidad correccion
    t=0
    #cota singleton
    MDS = False


    # Formas de dar un código:
    # 1. Ecuaciones parametricas
    # 2. Matriz generadora
    # 3. Matriz de control
    def __init__(self, clase, parametricas=[], generadora=[]):
        self.clase = clase

        if len(parametricas) != 0: #si hay ecuaciones parametricas
            #self.dimension = obtenerDimensionParametricas(parametricas)
            #self.longitud = obtenerLongitudParametricas(parametricas)
            arrayParametricas = np.array(AlgebraLineal.obtenerParametricas(parametricas,self.clase))
            self.matrizGeneradora = np.bmat(arrayParametricas)
            self.longitud = self.matrizGeneradora.shape[1] #el numero de columnas es la longitud
            self.dimension = np.linalg.matrix_rank(self.matrizGeneradora) #coincide con el numero filas
            self.calcularTodasPalabras()
            self.distanciaMinimaHamming()
            self.tasaInformacion()
            self.distanciaRelativa()
            self.capacidadDeteccion()
            self.capacidadCorreccion()
            self.numeroPalabras()
            self.cotaSingleton()
            self.matrizGeneradora = AlgebraLineal.diagonalizacionManual(self.matrizGeneradora, self.dimension, self.clase)
            self.calcularMatrizControl()

        elif len(generadora) != 0:
            self.matrizGeneradora = np.zeros(4)

    def distanciaMinimaHamming(self):
        return self.distanciaMinimaHamming_usandoDiccionario()

    # Distancia minima de hamming de un codigo C:
    # Distancia minima entre dos palabras de un código
    # Se recorre el diccionario completo comparando todas las palabras
    def distanciaMinimaHamming_usandoDiccionario(self):
        minimo = 100
        i = -1
        for palabra1 in self.diccionario:
            i += 1
            j = -1
            for palabra2 in self.diccionario:
                j += 1
                if i>=j:
                    continue
                distancia = fc.distanciaHamming(palabra1,palabra2)
                if minimo > distancia:
                    minimo = distancia
        self.distancia = minimo

    def pesoHammingCodigo(self):
        return 3

    def codificar(self, palabra):
        codificada = np.dot(np.array(palabra), self.matrizGeneradora)
        codificada = codificada % self.clase
        codificada = codificada.tolist()[0]
        return codificada

    def numeroPalabras(self):
        self.M = self.clase**self.dimension

    def tasaInformacion(self):
        self.R = self.dimension/float(self.longitud)

    def distanciaRelativa(self):
        self.g = self.distancia/float(self.longitud)

    def capacidadDeteccion(self):
        self.s = self.distancia-1

    def capacidadCorreccion(self):
        self.t = (self.distancia-1)//2

    def cotaSingleton(self):
        # distancia <= longitud-dimension + 1
        # distancia + dimension <= longitud + 1
        if self.distancia <= (self.longitud-self.dimension+1):
            self.MDS = True
        else:
            self.MDS = False

    #Una vez tenemos definida la matriz generadora sistematica, podemos obtener la matriz de control
    def calcularMatrizControl(self):
        #como la matriz es sistematica descartamos la identidad que debería estar a la izquierda
        A = self.matrizGeneradora[:,self.dimension:]
        Id = np.identity(self.longitud-self.dimension) # puesto que necesitamos una matriz Id de n-k
        self.matrizControl = np.bmat([[A],[Id]])

    #Una vez tenemos definida la matriz de control sistematica, podemos obtener la matriz generadora
    def calcularMatrizGeneradora(self):
        #como la matriz es sistematica descartamos la identidad que debería estar debajo
        A = self.matrizControl[:self.longitud-(self.longitud-self.dimension),:]
        Id = np.identity(self.dimension)
        self.matrizGeneradora = np.bmat([Id,A])

    def calcularDistanciaMinimaDesdeControl(self):
        return 3

    # se obtiene el diccionario con las palabras
    def calcularTodasPalabras(self):
        combinaciones = map(list, itertools.product(range(self.clase), repeat=self.dimension))
        #print(lst) #nos da todas las posibles combinaciones
        #si vamos multiplicando codificamos estas palabras:
        for palabra in combinaciones:
            codificada = self.codificar(palabra)
            self.diccionario.append(codificada)
            key = ''.join(str(e) for e in palabra)
            value = ''.join(str(e) for e in codificada)
            self.diccionario_CoDec.update({key:value})

    #se imprime el diccionario ordenado
    def imprimirDiccionario(self):
        for decodificada, codificada in self.diccionario_CoDec.items():
            print(decodificada+" => " + codificada)

    def calcularSindrome(self, vector):
        return vector*self.matrizControl

    def decodificacionSindromes(self):
        return 3

    def calcularTablaSindromes(self):
        return 3

    def perforar(self, arrayPosiciones):
        return 3

    def acortar(self, arrayPosiciones):
        return 3

    def extender(self):
        return 3

    def probabilidadError(self):
        return 3

    def pesoHammingVector(self,palabra):
        peso = 0
        for i in range(len(palabra)):
            if palabra[i] != 0:
                peso += 1
        return peso

    def teoremaShanon(self):
        return 3
