#!/usr/bin/python
import sys
sys.path.append('../')
from src.Hamming.Hamming import *

#Ejemplo instanciacion codigo Hamming 4

H = Hamming( 4, nombre="Hamming 4", desdeArchivo=True)
H.imprimirInformacionCodigo(G=True, H=True)
