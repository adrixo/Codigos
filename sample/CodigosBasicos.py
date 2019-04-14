#!/usr/bin/python
from Codigo import *


triple_repeticion = [['x'],'x','x','x']
triple_control = [['x','y','z'],'x','y','z','x+y','x+z','y+z']
paridad = [['a','b','c','d','f','g','h'],'a','b','c','d','f','g','h','a+b+c+d+f+g+h']

TR = Codigo(2, parametricas=triple_repeticion, nombre="triple repeticion")
TC = Codigo(2, parametricas=triple_control, nombre="Triple control")
P = Codigo(2, parametricas=paridad, nombre="Paridad")

codigos = [TR, TC, P]

for c in codigos:
    if c.M > 20:
        c.imprimirInformacionCodigo(G=True, H=True, dic=False, sin=False)
    else:
        c.imprimirInformacionCodigo(G=True, H=True, dic=True, sin=True)
