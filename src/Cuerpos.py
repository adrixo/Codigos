# -*- coding: utf-8 -*-
from __future__ import print_function
import aritmeticaModular as am

#objeto cuerpo:
class Cuerpo():
    clase = 2

    def __init__(self, clase):
        self.clase = clase

    def tablaSuma(self):
        print("Tabla sumar: ")
        print("  | ", end="")
        for i in range(self.clase):
            print(i, end=' ')
        print("")
        print("--+-", end="")
        for i in range(self.clase):
            print("+",end='+')
        print("")
        for i in range(self.clase):
            print(i, end=' | ')
            for j in range(self.clase):
                print(am.congruencia(i+j, self.clase), end=' ')
            print("")


    def tablaMultiplicar(self):
        print("Tabla multiplicar: ")
        print("  | ", end="")
        for i in range(self.clase):
            print(i, end=' ')
        print("")
        print("--+-", end="")
        for i in range(self.clase):
            print("+",end='+')
        print("")
        for i in range(self.clase):
            print(i, end=' | ')
            for j in range(self.clase):
                print(am.congruencia(i*j, self.clase), end=' ')
            print("")

    def invertible(self, numero, verbose=True):
        m = am.Mcd(numero, self.clase)
        if m != 1:
            if verbose:
                print("El mcd(%d, %d) es %d y por tanto no hay invertible para %d en Z/%d. " % (numero, self.clase, m, numero, self.clase))
            return self.clase/m
        else:
            return am.invertibleBruto(numero, self.clase)

    def extender(self):
        return x
