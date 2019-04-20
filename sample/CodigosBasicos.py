#!/usr/bin/python
from Codigo import *
import FuncionesCodigos as fc
import Parametricas as p

#Programa de ejemplo para probar un codigo

# 1. Instanciar el codigo:
#  el segundo parametro puede ser por ejemplo:
#     a) parametricas=p.triple_control
#     b) generadora="TripleControl_Generadora.txt"
#     c) control="TripleControl_Control.txt"
codigo = Codigo(2, parametricas=p.triple_control, nombre="matriz a acortar")

# 2. Imprimir informacion del codigo:
#  Poner cualquier campo a False si no se desea imprimir
codigo.imprimirInformacionCodigo(G=True, H=True, dic=True, sin=True)

# 3. operaciones con el codigo
fc.redundanciaMinimaShanon(0.001, 10000)


#################################
# EJEMPLOS
#################################

#   Ejemplo matriz perforada que reduce su dimension
# codigo = Codigo(2, generadora="matrizPerforable_Generadora.txt", nombre="matriz a perforar")
# codigo.imprimirInformacionCodigo(G=True, H=True, dic=True, sin=True)
# codigo.perforar([2,1], verbose=True)
# codigo.imprimirInformacionCodigo(G=True, H=True, dic=True, sin=True)

#   Ejemplo basico acortar
# codigo = Codigo(2, generadora="matrizAcortable_Generadora.txt", nombre="matriz a acortar")
# codigo.imprimirInformacionCodigo(G=True, H=True, dic=True, sin=True)
# codigo.acortar([0], verbose=True)
# codigo.imprimirInformacionCodigo(G=True, H=True, dic=True, sin=True)

#   Ejemplo basico extension
#codigo = Codigo(2, generadora="matrizPerforable_Generadora.txt", nombre="matriz a extender")
#codigo.imprimirInformacionCodigo(G=True, H=True, dic=True, sin=True)
#codigo.extender(verbose=True)
#codigo.imprimirInformacionCodigo(G=True, H=True, dic=True, sin=True)
