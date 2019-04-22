#!/usr/bin/python
import sys
sys.path.append('../')
from src.Codigo import *
import src.FuncionesCodigos as fc
import src.Parametricas as p

# Ejemplo de probabilidad de transmision de un codigo contenido en Pruebas_Ejemplo

codigo = Codigo(2, parametricas=p.triple_control, nombre="Triple control")
codigo.probabilidadTransmision(0.001, tipo='correccion', nPaquetes=3, verbose=True)
