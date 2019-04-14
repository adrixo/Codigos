# -*- coding: utf-8 -*-

#Biblioteca para el manejo de matrices
import numpy as np
import itertools
import AlgebraLineal
import FuncionesCodigos as fc

class Codigo:
    clase = 2 #mod 2

    nombre = ''

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
    def __init__(self, clase, parametricas=[], generadora=[], nombre='Sin nombre'):
        self.clase = clase
        self.nombre = nombre

        if len(parametricas) != 0: #si hay ecuaciones parametricas
            arrayParametricas = np.array(AlgebraLineal.obtenerParametricas(parametricas,self.clase))
            self.matrizGeneradora = np.bmat(arrayParametricas)
            self.setLongitud()
            self.setDimension()
            self.diagonalizacionManualGeneradora()

            self.setDiccionario()
            self.setDistanciaMinimaHamming()
            self.setTasaInformacion()
            self.setDistanciaRelativa()
            self.setCapacidadDeteccion()
            self.setCapacidadCorreccion()
            self.setNumeroPalabras()
            self.setCotaSingleton()
            self.setMatrizControl()

            self.calcularTablaSindromes()
            #self.decodificacionSindromes([0,1,1,1,1,1])

        elif len(generadora) != 0:
            self.matrizGeneradora = np.zeros(4)

######################################################################################

    def setLongitud(self):
        self.longitud = fc.longitudDesdeGeneradora(self.matrizGeneradora)

    def setDimension(self):
        self.dimension = fc.dimensionDesdeGeneradora(self.matrizGeneradora)

    def setDistanciaMinimaHamming(self):
        self.distancia = fc.distanciaMinimaHammingDesdeDiccionario(self.diccionario)

    def pesoHammingCodigo(self):
        print("Peso hamming: ", fc.pesoHammingCodigo(diccionario))

    def codificar(self, palabra):
        codificada = fc.codificar(palabra, self.matrizGeneradora, self.clase)
        return codificada

    def setNumeroPalabras(self):
        self.M = fc.numeroPalabras(self.clase, self.dimension)

    def setTasaInformacion(self):
        self.R = fc.tasaInformacion(self.dimension, self.longitud)

    def setDistanciaRelativa(self):
        self.g = fc.distanciaRelativa(self.distancia,self.longitud)

    def setCapacidadDeteccion(self):
        self.s = fc.capacidadDeteccion(self.distancia)

    def setCapacidadCorreccion(self):
        self.t = fc.capacidadCorreccion(self.distancia)

    def setCotaSingleton(self):
        self.MDS = fc.cotaSingleton(self.longitud, self.dimension, self.distancia)

    def setMatrizControl(self):
        self.matrizControl = fc.calcularMatrizControl(self.matrizGeneradora, self.longitud, self.dimension)

    def setMatrizGeneradora(self):
        self.matrizGeneradora = fc.calcularMatrizGeneradora(self.matrizControl, self.longitud, self.dimension)

    def diagonalizacionManualGeneradora(self):
        self.matrizGeneradora = AlgebraLineal.diagonalizacionManual(self.matrizGeneradora, self.dimension, self.clase)

    def calcularDistanciaMinimaDesdeControl(self):
        self.distancia = fc.calcularDistanciaMinimaDesdeControl()

    def setDiccionario(self):
        (self.diccionario, self.diccionario_CoDec) = fc.calcularTodasPalabras(self.clase, self.dimension, self.matrizGeneradora)

    def imprimirDiccionario(self):
        print("\n\tTabla palabras:")
        print("Decodificada => Codificada")
        fc.imprimirDiccionario(self.diccionario_CoDec)

    def calcularSindrome(self, palabra):
        return fc.calcularSindrome(palabra, self.matrizControl, self.clase)

    def decodificacionSindromes(self, palabra):
        self.calcularTablaSindromes()
        return fc.decodificacionSindromes(palabra, self.tablaSindromes, self.matrizControl, self.clase)

    def calcularTablaSindromes(self):
        self.tablaSindromes = fc.calcularTablaSindromes(self.t, self.matrizControl, self.clase)

    def imprimirTablaSindromes(self):
        print("\n\tTabla sindromes:")
        print("Sindrome => Error")
        fc.imprimirDiccionario(self.tablaSindromes)

    def imprimirInformacionCodigo(self, G=False, H=False, dic=False, sin=False):
        print("\n###########################")
        print("Codigo " + self.nombre + ': ')
        print("###########################")

        if G:
            print("\nMatriz generadora: ")
            print(self.matrizGeneradora)
            print("")

        if H:
            print("\nMatriz Control: ")
            print(self.matrizControl)
            print("")

        print("\nInformacion: ")
        print("[%d, %d, %d]" % (self.longitud, self.dimension, self.distancia))
        print("Numero de palabras: %d" % (self.M))
        print("Tasa informacion: %.2f%%" % (self.R))
        print("distancia relativa: %.2f%%" % (self.g))
        print("capacidad de deteccion: %d" % (self.s))
        print("capacidad de correccion: %d" % (self.t))
        print("Es MDS: " + str(self.MDS))

        if dic:
            print(self.imprimirDiccionario())
            print("")

        if sin:
            print(self.imprimirTablaSindromes())
            print("")

    def perforar(self, arrayPosiciones):
        return 3

    def acortar(self, arrayPosiciones):
        return 3

    def extender(self):
        return 3

    def probabilidadError(self):
        return 3

    def teoremaShanon(self):
        return 3

    def esCodigoLineal(self):
        print(fc.esCodigoLineal(self.diccionario, self.matrizControl, self.clase))
