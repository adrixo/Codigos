#!/usr/bin/python
from Codigo import *


#[['x','y','z','t','s'],'x+z+t','x+z+t','y+s','2*x+2*t','3*y+3*s','4*z']
#paramet=[['x','y','z'],'x','x+z','y','2*x','3*y','4*z']
#triple control = ['x','y','z'],'x','y','z','x+y','x+z','y+z'
#paridad = [['a','b','c','d','f','g','h'],'a','b','c','d','f','g','h','a+b+c+d+f+g+h']
paramet= [['x','y','z'],'x','y','z','x+y','x+z','y+z']
codigo = Codigo(2, parametricas=paramet)

print("")
print("Codigo:")
print("")

print("Matriz generadora: ")
print(codigo.matrizGeneradora)
print("")

print("Matriz Control: ")
print(codigo.matrizControl)
print("")
print("")
print("tipo:")
print("[%d, %d, %d]" % (codigo.longitud, codigo.dimension, codigo.distancia))
print("Tasa informacion: %.2f%%" % (codigo.R))
print("distancia relativa: %.2f%%" % (codigo.g))
print("capacidad de deteccion: %d" % (codigo.s))
print("capacidad de correccion: %d" % (codigo.t))
print("Es MDS: " + str(codigo.MDS))
print("")
print("Numero de palabras: %d" % (codigo.M))
print("Palabras: ")
print(codigo.imprimirDiccionario())
print("")
