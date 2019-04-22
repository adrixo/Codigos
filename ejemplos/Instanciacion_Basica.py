#!/usr/bin/python
import sys
sys.path.append('../')
from src.Codigo import *

triple_control = [['x','y','z'],'x','y','z','x+y','x+z','y+z']

TR = Codigo(2, parametricas=triple_control, nombre="triple_control")
TR.imprimirInformacionCodigo()

TR = Codigo(2, generadora='TripleControl_Generadora.txt', nombre="triple_control")
TR.imprimirInformacionCodigo(G=True)

TR = Codigo(2, control='TripleControl_Control.txt', nombre="triple_control")
TR.imprimirInformacionCodigo(H=True)
