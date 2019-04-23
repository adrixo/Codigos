#!/usr/bin/python
import sys
sys.path.append('../')
from src.Hamming.Hamming import *

#Ejemplo instanciacion codigo Hamming 4

H = Hamming(5, desdeArchivo=True)
H.imprimirInformacionCodigo(G=True, H=True)
