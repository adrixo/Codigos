#!/usr/bin/python
from src.Codigo import *
import src.AlgebraLineal
import itertools
import os.path


class Hamming(Codigo):
    # Definicion: El codigo q ario de hamming de orden r Ham_q(r) es aquel cuya matriz de control tiene por filas todos los vectores de F_q2 no proporcionales

    #Si se desea cargar de archivo para no tener que gestionar la matriz de control...
    def __init__(self, q, clase=2, nombre='Hamming sin nombre', desdeArchivo=False, probabilidadErrorDeCanal=0.001):

        existeArchivo = True

        if desdeArchivo:
            archivo = "Hamming"+str(q)+"_Control.txt"

            if os.path.isfile(archivo):
                Codigo.__init__(self, clase, control=archivo, nombre=nombre)
            else:
                existeArchivo = False

        if not desdeArchivo or not existeArchivo:
            Codigo.__init__(self, clase, nombre=nombre)
            self.matrizControl = self.obtenerMatrizControlHamming(q)
            self.setLongitud('control')
            self.setDimension('control')
            self.diagonalizacionManual('control')
            self.setMatrizGeneradora()

        self.setPrarametros(palabras=False)


    def obtenerMatrizControlHamming(self, q, clase=2):
        combinaciones = map(list, itertools.product(range(clase), repeat=q))
        noProporcionales = AlgebraLineal.eliminarVectoresProporcionales(combinaciones, clase=clase)
        noProporcionales = np.bmat(np.array(combinaciones))
        return noProporcionales
