#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
sys.path.append('../')
from src.Criptografia import *

mensaje = str(raw_input("Mensaje-> "))
encriptado = ""
desencriptado = ""

# Ejemplo encriptacion cesar:
clavePrivada = int(raw_input("Clave para caesar-> "))
encriptado = caesarCrypt(mensaje, clavePrivada)
print("Mensaje encriptado con caesar %d: %s" % (clavePrivada, encriptado))
desencriptado = caesarDecrypt(encriptado, clavePrivada)
print("Mensaje desencriptado con caesar %d: %s" % (clavePrivada, desencriptado))
