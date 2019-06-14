#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
sys.path.append('../')
from src.Cuerpos import *

# Ejemplo de instanciación y manejo cuerpo

cinco = Cuerpo(5)
cinco.tablaSuma()
cinco.tablaMultiplicar()

seis = Cuerpo(6)
seis.tablaSuma()
seis.tablaMultiplicar()

siete = Cuerpo(7)
siete.tablaSuma()
siete.tablaMultiplicar()

print(seis.invertible(4))
print(siete.invertible(4))

veintiuno = Cuerpo(21)
veintiuno.tablaMultiplicar()
print(veintiuno.invertible(11))
