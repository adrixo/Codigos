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
    matrizControl = None
    #n-k columnas
    tablaSindromes = []

    #todas las palabras
    diccionario = []
    #Diccionario con decodificada/codificada
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

    probabilidadErrorDeCanal = 0.000001

    # Formas de dar un código:
    # 1. Ecuaciones parametricas
    # 2. Matriz generadora
    # 3. Matriz de control
    def __init__(self, clase, parametricas=[], generadora=[], control=[], nombre='Sin nombre', probabilidadErrorDeCanal=0.000001):
        self.clase = clase
        self.nombre = nombre
        self.probabilidadErrorDeCanal = probabilidadErrorDeCanal

        if len(parametricas) != 0: #si hay ecuaciones parametricas
            arrayParametricas = np.array(AlgebraLineal.obtenerParametricas(parametricas,self.clase))
            self.matrizGeneradora = np.bmat(arrayParametricas)
            self.setLongitud('generadora')
            self.setDimension('generadora')
            self.diagonalizacionManual('generadora')
            self.setMatrizControl()

        elif len(generadora) != 0:
            archivo = "../Matrices/"+generadora
            self.matrizGeneradora = np.bmat(np.loadtxt(archivo).astype(int))
            self.setLongitud('generadora')
            self.setDimension('generadora')
            self.diagonalizacionManual('generadora')
            self.setMatrizControl()

        elif len(control) != 0:
            archivo = "../Matrices/"+control
            self.matrizControl = np.bmat(np.loadtxt(archivo).astype(int))
            if self.matrizControl.shape[0] == 1:
                self.matrizControl = self.matrizControl.T
            self.setLongitud('control')
            self.setDimension('control')
            self.diagonalizacionManual('control')
            self.setMatrizGeneradora()

        else:
            print("Falta un parametro para definir el codigo.")
            return None

        self.setPrarametros()

######################################################################################

    def setLongitud(self, metodo):
        if metodo == 'generadora':
            self.longitud = fc.longitudDesdeGeneradora(self.matrizGeneradora)
        elif metodo == 'control':
            self.longitud = fc.longitudDesdeControl(self.matrizControl)
        else:
            print("Error setLongitud")

    def setDimension(self, metodo):
        if metodo == 'generadora':
            self.dimension = fc.dimensionDesdeGeneradora(self.matrizGeneradora)
        elif metodo == 'control':
            self.dimension = fc.dimensionDesdeControl(self.matrizControl)
        else:
            print("Error setDimension")

    def setPrarametros(self, dim_long='', palabras=True, tablaSindromes=True):

        #En caso de que queramos calcular nuevamente la dimension y longitud
        if dim_long == 'generadora' or dim_long == 'control':
            self.setLongitud(dim_long)
            self.setDimension(dim_long)

        if palabras:
            #En caso de que queramos calcular todas las palabras del diccionario
            self.setDiccionario()

        self.setDistanciaMinimaHamming()
        self.setTasaInformacion()
        self.setDistanciaRelativa()
        self.setCapacidadDeteccion()
        self.setCapacidadCorreccion()
        self.setNumeroPalabras()
        self.setCotaSingleton()

        if tablaSindromes:
            #En caso de que queramos calcular los sindromes
            self.calcularTablaSindromes()

    def setDistanciaMinimaHamming(self):
        if len(self.diccionario) != 0:
            self.distancia = fc.distanciaMinimaHammingDesdeDiccionario(self.diccionario)
        elif self.matrizControl is not None:
            self.distancia = fc.distanciaMinimaHammingDesdeControl(self.matrizControl, self.longitud, self.clase)
        else:
            self.distancia = 99999

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

    def diagonalizacionManual(self, tipoMatriz):
        if tipoMatriz == 'generadora':
            self.matrizGeneradora = AlgebraLineal.diagonalizacionManual(self.matrizGeneradora, self.dimension, self.longitud, self.clase, self.nombre, tipoMatriz)
        elif tipoMatriz == 'control':
            self.matrizControl = AlgebraLineal.diagonalizacionManual(self.matrizControl, self.dimension, self.longitud, self.clase, self.nombre, tipoMatriz)
        else:
            print("Error Diagonalización manual")

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

    def imprimirInformacionCodigo(self, Info=True, G=False, H=False, dic=False, sin=False):
        print("\n###########################")
        print("Codigo " + self.nombre + ': ')
        print("###########################")

        if G:
            print("\nMatriz generadora: ")
            print(self.matrizGeneradora)

        if H:
            print("\nMatriz Control: ")
            print(self.matrizControl)

        if Info:
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

        if sin:
            print(self.imprimirTablaSindromes())

        print("\n####### Fin " + self.nombre + " #########\n")

    def perforar(self, arrayPosiciones, verbose=False):
        if verbose:
            print("Perforando el codigo generado por: ")
            print(self.matrizGeneradora)
        arrayPosiciones = list(set(arrayPosiciones))
        arrayPosiciones.reverse()
        for pos in arrayPosiciones:
            if pos > self.longitud:
                print("posicion imposible", pos)
                continue
            self.matrizGeneradora = np.delete(self.matrizGeneradora, pos, 1)

            if verbose:
                print("Perforando posicion: " + str(pos))
                print(self.matrizGeneradora)

        # Llegado a este punto si se baja de dimension podria quedar algun vector lin dep a eliminar
        matrizArray = list(np.array(self.matrizGeneradora))
        matrizArray = AlgebraLineal.eliminarVectoresProporcionales(matrizArray,clase=self.clase)
        matrizArray = np.array(matrizArray)
        self.matrizGeneradora = np.bmat(matrizArray)
        if verbose:
            print("Eliminando vectores proporcionales: ")
            print(self.matrizGeneradora)

        longitudAnterior = self.longitud
        dimensionAnterior = self.dimension
        distanciaAnterior = self.distancia
        MAnterior = self.M
        RAnterior = self.R
        gAnterior = self.g

        # Se genera la nueva matriz control
        self.setLongitud('generadora')
        self.setDimension('generadora')
        self.diagonalizacionManual('generadora')
        self.setMatrizControl()

        #Nuevos valores
        self.setPrarametros()
        if verbose:
            print("\nEl codigo ha evolucionado: ")
            print("[%d->%d, %d->%d, %d->%d]" % (longitudAnterior, self.longitud, dimensionAnterior, self.dimension, distanciaAnterior, self.distancia))
            print("Numero de palabras: %d->%d" % (MAnterior, self.M))
            print("Tasa informacion: %.2f%%->%.2f%%" % (RAnterior,self.R))
            print("distancia relativa: %.2f%%->%.2f%%" % (gAnterior, self.g))
            print("")


# Se obtiene cogiendo todas las palabras que tienen 0s en las posiciones dadas, la matriz generadora seria los
    def acortar(self, arrayPosiciones, verbose=True):
        if verbose:
            print("\nAcortando el codigo de palabras: ")
            print(self.diccionario)

        arrayPosiciones = list(set(arrayPosiciones))
        arrayPosiciones.reverse()

        #Tomamos todas las palabras y eliminamos la nula
        palabraNula = [0 for i in range(self.longitud)]
        palabras = self.diccionario[:]
        i = 0
        for p in palabras:
            if p == palabraNula:
                palabras.pop(i)
                break
            i += 1
        #Para cada posicion eliminamos palabras
        palabrasAcortadas = []
        for posicion in arrayPosiciones:
            if posicion > self.longitud:
                print("posicion imposible: "+ str(posicion))
                continue

            if verbose:
                print("\nAcortando posicion: " + str(posicion))

            for p in palabras:
                if p[posicion] == 0:
                    p.pop(posicion)
                    palabrasAcortadas.append(p)
            palabras = palabrasAcortadas[:]
            palabrasAcortadas = []

        #Ahora nos quedamos con las lin. independientes que formarian base
        matrizArray = AlgebraLineal.eliminarVectoresProporcionales(palabras,clase=self.clase)
        matrizArray = np.array(matrizArray)
        self.matrizGeneradora = np.bmat(matrizArray)
        self.diagonalizacionManual('generadora')
        matrizArray = list(np.array(self.matrizGeneradora))
        matrizArray = AlgebraLineal.eliminarVectoresProporcionales(matrizArray,clase=self.clase)
        matrizArray = np.array(matrizArray)
        self.matrizGeneradora = np.bmat(matrizArray)

        if verbose:
            print("\nEliminando vectores proporcionales para obtener generadora: ")
            print(self.matrizGeneradora)

        longitudAnterior = self.longitud
        dimensionAnterior = self.dimension
        distanciaAnterior = self.distancia
        MAnterior = self.M
        RAnterior = self.R
        gAnterior = self.g

        # Se genera la nueva matriz control
        self.setLongitud('generadora')
        self.setDimension('generadora')
        self.diagonalizacionManual('generadora')
        self.setMatrizControl()

        #Nuevos valores
        self.setPrarametros()
        if verbose:
            print("\nEl codigo ha evolucionado: ")
            print("[%d->%d, %d->%d, %d->%d]" % (longitudAnterior, self.longitud, dimensionAnterior, self.dimension, distanciaAnterior, self.distancia))
            print("Numero de palabras: %d->%d" % (MAnterior, self.M))
            print("Tasa informacion: %.2f%%->%.2f%%" % (RAnterior,self.R))
            print("distancia relativa: %.2f%%->%.2f%%" % (gAnterior, self.g))
            print("")

    def extender(self, verbose=True):
        if verbose:
            print("Extendiendo el codigo generado por: ")
            print(self.matrizGeneradora)

        # En cada vector de la matriz comprobamos la paridad y se la añadimos al final
        matrizArray = list(np.array(self.matrizGeneradora))
        matrizResultado = []
        for vector in matrizArray:
            paridad = sum(vector) % self.clase
            vectorResultado = list(vector)
            vectorResultado.append(paridad)
            matrizResultado.append(vectorResultado)

        matrizArray = np.array(matrizResultado)
        self.matrizGeneradora = np.bmat(matrizArray)

        longitudAnterior = self.longitud
        dimensionAnterior = self.dimension
        distanciaAnterior = self.distancia
        MAnterior = self.M
        RAnterior = self.R
        gAnterior = self.g

        # Se genera la nueva matriz control
        self.setLongitud('generadora')
        self.setDimension('generadora')
        self.diagonalizacionManual('generadora')
        self.setMatrizControl()

        #Nuevos valores
        self.setPrarametros()
        if verbose:
            print("\nEl codigo ha evolucionado: ")
            print("[%d->%d, %d->%d, %d->%d]" % (longitudAnterior, self.longitud, dimensionAnterior, self.dimension, distanciaAnterior, self.distancia))
            print("Numero de palabras: %d->%d" % (MAnterior, self.M))
            print("Tasa informacion: %.2f%%->%.2f%%" % (RAnterior,self.R))
            print("distancia relativa: %.2f%%->%.2f%%" % (gAnterior, self.g))
            print("")


    def probabilidadTransmision(self, probabilidadError, tipo='correccion', nPaquetes=1):
        if tipo == 'correccion':
            nCombinaciones = self.t
        elif tipo == 'deteccion':
            nCombinaciones = self.s
        else:
            nCombinaciones = 0

        return fc.probabilidadTransmision(probabilidadError, self.longitud, nCombinaciones, paquetesEnviados=nPaquetes)

    def esCodigoLineal(self):
        print(fc.esCodigoLineal(self.diccionario, self.matrizControl, self.clase))
